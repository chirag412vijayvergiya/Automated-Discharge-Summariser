"""Secondary analytics helpers for HITL Page 2 (SSoT §3.5).

Prefer calling Secondary MCP when it is up; fall back to local pure-Python
builders so the dashboard never crashes if :8201 is offline.
"""

from __future__ import annotations

import json
import re

from mcp_servers.secondary.tools.generate_risk_heatmap import build_heatmap
from mcp_servers.secondary.tools.get_population_benchmarks import get_benchmark
from shared.logger import get_logger
from shared.settings import get_service

logger = get_logger("hitl_analytics")

_ELICIT_FIELDS_RE = re.compile(r"\(([^)]+)\)")


def _fields_from_elicitation_message(message: str) -> list[str]:
    """Parse '… (age, attending_physician)' from the elicitation gate note."""
    match = _ELICIT_FIELDS_RE.search(message or "")
    if not match:
        return []
    inner = match.group(1).strip()
    if not inner or "no fields listed" in inner.lower():
        return []
    return [part.strip() for part in inner.split(",") if part.strip()]


def expand_findings_for_heatmap(
    findings: list[dict] | None,
    *,
    missing_fields: list[str] | None = None,
) -> list[dict]:
    """Split batched elicitation findings into one heatmap row per soft field.

    Validator keeps one ``elicitation_decline`` / ``elicitation_cancel`` finding
    (SSoT §3.7 batch). For the heatmap we expand that into per-field Info rows
    so reviewers see age, attending, etc. separately. Scoring / gate still use
    the original finding list.
    """
    out: list[dict] = []
    fallback_fields = [
        str(f).strip() for f in (missing_fields or []) if str(f).strip()
    ]
    for finding in findings or []:
        rule = str(finding.get("rule_id") or "")
        if not rule.startswith("elicitation_"):
            out.append(dict(finding))
            continue
        action = rule[len("elicitation_") :]
        fields = list(fallback_fields) or _fields_from_elicitation_message(
            str(finding.get("message") or "")
        )
        if not fields:
            out.append(dict(finding))
            continue
        blocking = bool(finding.get("blocking"))
        severity = str(finding.get("severity") or "info")
        for field in fields:
            out.append(
                {
                    "rule_id": "missing_soft_field",
                    "severity": severity,
                    "message": (
                        f"Soft field '{field}' unresolved "
                        f"(elicitation {action})."
                    ),
                    "field": field,
                    "weight": 0,
                    "blocking": blocking,
                }
            )
    return out


def heatmap_from_findings(findings: list[dict]) -> dict:
    """Always-available local heatmap (same logic as Secondary tool)."""
    return build_heatmap(findings or [])


def benchmarks_for(service_line: str) -> dict:
    """Always-available local population benchmarks."""
    line = (service_line or "General Medicine").strip() or "General Medicine"
    row = get_benchmark(line)
    return {"service_line": line, **row}


async def try_secondary_heatmap(findings: list[dict]) -> tuple[dict, str]:
    """Call Secondary MCP generate_risk_heatmap; fall back locally on error."""
    try:
        from fastmcp import Client

        svc = get_service("secondary_mcp")
        url = (
            f"http://{svc.get('host', '127.0.0.1')}:"
            f"{int(svc.get('port', 8201))}"
            f"{svc.get('transport_path', '/analyticstools')}"
        )
        async with Client(url) as client:
            result = await client.call_tool(
                "generate_risk_heatmap",
                {"findings": findings},
                raise_on_error=False,
            )
        text = ""
        for block in getattr(result, "content", []) or []:
            if getattr(block, "text", None):
                text = block.text
                break
        if text:
            return json.loads(text), "secondary_mcp"
    except Exception as exc:
        logger.info("Secondary heatmap unavailable (%s) — using local builder", exc)
    return heatmap_from_findings(findings), "local"


def load_heatmap(
    findings: list[dict],
    *,
    missing_fields: list[str] | None = None,
    expand_elicitation: bool = True,
) -> tuple[dict, str]:
    """Sync wrapper for Streamlit: Secondary MCP heatmap with local fallback."""
    import asyncio

    rows = list(findings or [])
    if expand_elicitation:
        rows = expand_findings_for_heatmap(rows, missing_fields=missing_fields)
    try:
        return asyncio.run(try_secondary_heatmap(rows))
    except Exception as exc:
        logger.info("Heatmap load failed (%s) — using local builder", exc)
        return heatmap_from_findings(rows), "local"


async def try_secondary_benchmarks(service_line: str) -> tuple[dict, str]:
    """Call Secondary MCP get_population_benchmarks; fall back locally."""
    try:
        from fastmcp import Client

        svc = get_service("secondary_mcp")
        url = (
            f"http://{svc.get('host', '127.0.0.1')}:"
            f"{int(svc.get('port', 8201))}"
            f"{svc.get('transport_path', '/analyticstools')}"
        )
        async with Client(url) as client:
            result = await client.call_tool(
                "get_population_benchmarks",
                {"service_line": service_line or "General Medicine"},
                raise_on_error=False,
            )
        text = ""
        for block in getattr(result, "content", []) or []:
            if getattr(block, "text", None):
                text = block.text
                break
        if text:
            return json.loads(text), "secondary_mcp"
    except Exception as exc:
        logger.info("Secondary benchmarks unavailable (%s) — using local", exc)
    return benchmarks_for(service_line), "local"
