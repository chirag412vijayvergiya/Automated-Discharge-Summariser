"""HITL visual system — CSS + pipeline stepper (spec G/H)."""

from __future__ import annotations

CUSTOM_CSS = r"""


@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

:root {
  --ink: #f4f4f5;
  --muted: #a1a1aa;
  --line: #27272a;
  --surface: #141416;
  --canvas: #0a0a0b;
  --teal: #2dd4bf;
  --teal-deep: #2dd4bf;
  --ok: #34d399;
  --warn: #fbbf24;
  --bad: #f87171;
  --info: #818cf8;
  --shadow: 0 1px 0 rgba(255,255,255,0.04), 0 8px 24px rgba(0,0,0,0.45);
  --shadow-hover: 0 1px 0 rgba(255,255,255,0.06), 0 12px 28px rgba(0,0,0,0.55);
  --radius: 12px;
  --sb-bg: #070708;
  --sb-card: #141416;
  --sb-text: #fafafa;
  --sb-muted: #a1a1aa;
  --sb-accent: #2dd4bf;
  --sb-border: #27272a;
  --sb-hover: rgba(45,212,191,0.10);
  --sb-active: rgba(45,212,191,0.18);
  --font: "Plus Jakarta Sans", "Segoe UI", sans-serif;
  --display: "Plus Jakarta Sans", "Segoe UI", sans-serif;
  --mono: "JetBrains Mono", ui-monospace, Menlo, Consolas, monospace;
}


html, body, .stApp, [data-testid="stAppViewContainer"],
[data-testid="stSidebar"], [data-testid="stMarkdownContainer"],
button, input, textarea, select, label, p,
.stTextInput, .stSelectbox, .stRadio, .stButton, .stChatMessage,
[data-testid="stChatInput"], [data-baseweb="input"], [data-baseweb="select"],
[data-baseweb="textarea"], [data-baseweb="tab"],
[data-testid="stChatMessageContent"],
[data-testid="stWidgetLabel"] {
  font-family: var(--font) !important;
}
/* Keep Streamlit Material icons visible (do not inherit Plus Jakarta) */
[data-testid="stIconMaterial"],
[data-testid="stChatMessageAvatarUser"],
[data-testid="stChatMessageAvatarAssistant"],
[data-testid="stChatMessageAvatarCustom"],
[data-testid="stChatMessageAvatarUser"] *,
[data-testid="stChatMessageAvatarAssistant"] *,
[data-testid="stChatMessageAvatarCustom"] *,
[data-testid="stBaseButton-headerNoPadding"] [data-testid="stIconMaterial"],
button [data-testid="stIconMaterial"],
span[data-testid="stIconMaterial"] {
  font-family: "Material Symbols Rounded" !important;
  -webkit-text-fill-color: currentColor !important;
  color: inherit !important;
  font-style: normal !important;
  font-weight: 400 !important;
  speak: never;
  line-height: 1 !important;
  letter-spacing: normal !important;
  text-transform: none !important;
  display: inline-block !important;
  visibility: visible !important;
  opacity: 1 !important;
}
html, body, .stApp, [data-testid="stAppViewContainer"] {
  color: var(--ink) !important;
}
.stApp {
  background:
    radial-gradient(900px 480px at 85% -5%, rgba(45,212,191,0.07), transparent 55%),
    radial-gradient(700px 420px at 0% 100%, rgba(129,140,248,0.05), transparent 50%),
    var(--canvas) !important;
  color-scheme: dark !important;
}
.block-container {
  padding-top: 4.25rem !important;
  padding-bottom: 2.5rem !important;
  padding-left: 2rem !important;
  padding-right: 2rem !important;
  max-width: 1260px !important;
}

/* Headings — high contrast */
[data-testid="stAppViewContainer"] h1,
[data-testid="stAppViewContainer"] h2,
[data-testid="stAppViewContainer"] h3,
[data-testid="stMarkdownContainer"] h1,
[data-testid="stMarkdownContainer"] h2,
[data-testid="stMarkdownContainer"] h3,
.page-title {
  color: var(--ink) !important;
  -webkit-text-fill-color: var(--ink) !important;
  opacity: 1 !important;
  font-family: var(--display) !important;
}
.page-title {
  font-size: 1.75rem !important;
  font-weight: 700 !important;
  margin: 0 !important;
  letter-spacing: -0.02em;
  line-height: 1.2 !important;
}
.page-lede {
  color: var(--muted) !important;
  -webkit-text-fill-color: var(--muted) !important;
  font-size: 0.95rem !important;
  margin: 0.4rem 0 0 !important;
  line-height: 1.5 !important;
}
.page-header {
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  padding: 1.25rem 1.5rem;
  margin-bottom: 1.25rem;
  box-shadow: var(--shadow);
  border-left: 3px solid var(--teal);
}

/* Sidebar — clinical console rail */
section[data-testid="stSidebar"] {
  background:
    linear-gradient(180deg, #070708 0%, #070708 48%, #050506 100%) !important;
  border-right: 1px solid #27272a;
  width: 288px !important;
  min-width: 288px !important;
  max-width: 288px !important;
  overflow-x: hidden !important;
}
section[data-testid="stSidebar"] > div {
  overflow-x: hidden !important;
  width: 100% !important;
  max-width: 288px !important;
}
section[data-testid="stSidebar"] [data-testid="stSidebarContent"] {
  padding: 1.35rem 1rem 1.5rem !important;
  overflow-x: hidden !important;
  overflow-y: auto !important;
  width: 100% !important;
  max-width: 100% !important;
  box-sizing: border-box !important;
}
/* Keep nav pinned — hide Streamlit's collapse / expand chevron */
[data-testid="collapsedControl"],
[data-testid="stSidebarCollapseButton"],
[data-testid="stExpandSidebarButton"],
button[kind="header"][data-testid="baseButton-header"],
section[data-testid="stSidebar"] [data-testid="stSidebarCollapseButton"],
div[data-testid="stSidebarCollapsedControl"] {
  display: none !important;
  visibility: hidden !important;
  pointer-events: none !important;
  width: 0 !important;
  height: 0 !important;
}

/* —— Branding —— */
section[data-testid="stSidebar"] .brand-kicker {
  font-size: 0.68rem; letter-spacing: 0.16em; text-transform: uppercase;
  font-weight: 700; color: var(--sb-accent) !important;
  -webkit-text-fill-color: var(--sb-accent) !important; margin-bottom: 0.4rem;
}
section[data-testid="stSidebar"] .brand-title {
  font-family: var(--display) !important; font-size: 1.85rem !important;
  font-weight: 700 !important; color: #fafafa !important;
  -webkit-text-fill-color: #fafafa !important; margin: 0 !important; line-height: 1.1;
  letter-spacing: -0.02em;
}
section[data-testid="stSidebar"] .brand-sub {
  color: var(--sb-muted) !important; -webkit-text-fill-color: var(--sb-muted) !important;
  font-size: 0.82rem !important; margin-top: 0.4rem; font-weight: 500;
  line-height: 1.4; max-width: 16rem;
}
.brand-lockup {
  padding: 0.15rem 0.15rem 1rem;
  margin-bottom: 1.15rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
}

/* —— Section labels —— */
.nav-group-label {
  font-size: 0.7rem; letter-spacing: 0.11em; text-transform: uppercase;
  font-weight: 600; color: #71717a !important;
  -webkit-text-fill-color: #71717a !important;
  margin: 1rem 0.15rem 0.5rem;
  padding: 0;
}

/* —— Selected patient card (compact) —— */
.patient-card {
  background: var(--sb-card);
  border: 1px solid var(--sb-border);
  border-radius: 9px;
  padding: 0.55rem 0.75rem;
  margin-bottom: 0.55rem;
}
.patient-card-id {
  color: var(--sb-text) !important; -webkit-text-fill-color: var(--sb-text) !important;
  font-size: 0.98rem; font-weight: 700; line-height: 1.2;
  white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
}
.patient-card-name {
  color: var(--sb-muted) !important; -webkit-text-fill-color: var(--sb-muted) !important;
  font-size: 0.82rem; margin-top: 0.12rem; font-weight: 500; line-height: 1.3;
  white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
}
.patient-card-empty {
  border-style: dashed;
}
.patient-card-empty-msg {
  color: var(--sb-muted) !important; -webkit-text-fill-color: var(--sb-muted) !important;
  font-size: 0.82rem; font-weight: 500;
}

section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] span,
section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
  color: var(--sb-text) !important;
  -webkit-text-fill-color: var(--sb-text) !important;
}

/* —— Dark search field (blends with sidebar) —— */
section[data-testid="stSidebar"] .stTextInput {
  position: relative !important;
  margin: 0 0 0.35rem !important;
}
section[data-testid="stSidebar"] .stTextInput::before {
  content: "";
  position: absolute;
  left: 0.8rem;
  top: 50%;
  width: 0.8rem;
  height: 0.8rem;
  transform: translateY(-50%);
  z-index: 3;
  pointer-events: none;
  background-repeat: no-repeat;
  background-size: contain;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' fill='none' viewBox='0 0 24 24' stroke='%2394a3b8' stroke-width='2.2'%3E%3Ccircle cx='11' cy='11' r='7'/%3E%3Cpath stroke-linecap='round' d='M20 20l-3.5-3.5'/%3E%3C/svg%3E");
}
section[data-testid="stSidebar"] div[data-baseweb="input"],
section[data-testid="stSidebar"] [data-baseweb="input"] {
  background: transparent !important;
}
section[data-testid="stSidebar"] div[data-baseweb="input"] > div,
section[data-testid="stSidebar"] [data-baseweb="input"] > div {
  background-color: #18181b !important;
  background-image: none !important;
  border: 1px solid #3f3f46 !important;
  border-radius: 9px !important;
  min-height: 2.5rem !important;
  max-height: 2.5rem !important;
  transition: border-color 160ms ease, box-shadow 160ms ease !important;
  box-shadow: none !important;
}
section[data-testid="stSidebar"] div[data-baseweb="input"] > div:hover,
section[data-testid="stSidebar"] [data-baseweb="input"] > div:hover {
  border-color: #52525b !important;
}
section[data-testid="stSidebar"] div[data-baseweb="input"]:focus-within > div,
section[data-testid="stSidebar"] [data-baseweb="input"]:focus-within > div {
  border-color: var(--sb-accent) !important;
  box-shadow: 0 0 0 2px rgba(20, 184, 166, 0.22) !important;
}
section[data-testid="stSidebar"] .stTextInput input,
section[data-testid="stSidebar"] input[type="text"],
section[data-testid="stSidebar"] input {
  background: #18181b !important;
  background-color: #18181b !important;
  color: #1f1f23 !important;
  -webkit-text-fill-color: #1f1f23 !important;
  caret-color: #1f1f23 !important;
  border: none !important;
  box-shadow: none !important;
  padding-left: 2.1rem !important;
  padding-right: 0.75rem !important;
  font-size: 0.88rem !important;
  font-weight: 500 !important;
  line-height: 1.3 !important;
}
/* Defeat Streamlit light-theme white fill on nested BaseWeb wrappers */
section[data-testid="stSidebar"] .stTextInput [class*="st-"],
section[data-testid="stSidebar"] .stTextInput div {
  background-color: transparent !important;
}
section[data-testid="stSidebar"] .stTextInput [data-baseweb="input"] > div {
  background-color: #18181b !important;
}
section[data-testid="stSidebar"] .stTextInput input::placeholder,
section[data-testid="stSidebar"] input::placeholder {
  color: #71717a !important;
  -webkit-text-fill-color: #71717a !important;
  opacity: 1 !important;
  font-weight: 400 !important;
}
/* Hide Streamlit “Press Enter to apply” / instruction chrome in sidebar search */
section[data-testid="stSidebar"] [data-testid="InputInstructions"],
section[data-testid="stSidebar"] .stTextInput [data-testid="InputInstructions"],
section[data-testid="stSidebar"] .stTextInput [data-baseweb="input"] + div {
  display: none !important;
}

.sb-empty-hint {
  margin: 0.25rem 0 0.55rem;
  padding: 0.55rem 0.75rem;
  border-radius: 10px;
  border: 1px solid #3f3f46;
  background: #18181b !important;
  color: #71717a !important;
  -webkit-text-fill-color: #71717a !important;
  font-size: 0.78rem !important;
  font-weight: 500;
  text-align: left;
}
.sb-suggest-label {
  font-size: 0.62rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  font-weight: 600;
  color: #71717a !important;
  -webkit-text-fill-color: #71717a !important;
  margin: 0.35rem 0 0.3rem;
}

section[data-testid="stSidebar"] .stSelectbox,
section[data-testid="stSidebar"] .stRadio,
section[data-testid="stSidebar"] [data-testid="stVerticalBlock"] {
  max-width: 100% !important;
  overflow-x: hidden !important;
}

/* —— Navigation (text-only radio, prior style) —— */
section[data-testid="stSidebar"] .stRadio [role="radiogroup"] {
  gap: 0.38rem !important;
}
section[data-testid="stSidebar"] .stRadio label {
  padding: 0.72rem 0.85rem !important;
  border-radius: 9px !important;
  border: 1px solid transparent !important;
  border-left: 3px solid transparent !important;
  margin-bottom: 0 !important;
  transition: background 160ms ease, border-color 160ms ease, color 160ms ease;
  white-space: normal !important;
  word-break: break-word !important;
  max-width: 100% !important;
  box-sizing: border-box !important;
  font-size: 0.95rem !important;
  font-weight: 500 !important;
  letter-spacing: 0.01em;
  line-height: 1.35 !important;
  color: #d4d4d8 !important;
  -webkit-text-fill-color: #d4d4d8 !important;
}
section[data-testid="stSidebar"] .stRadio label:hover {
  background: rgba(45, 212, 191, 0.08) !important;
  border-color: rgba(63, 63, 70, 0.9) !important;
  color: #fafafa !important;
  -webkit-text-fill-color: #fafafa !important;
}
section[data-testid="stSidebar"] .stRadio label:has(input:checked) {
  background: rgba(45, 212, 191, 0.14) !important;
  border-color: rgba(45, 212, 191, 0.28) !important;
  border-left-color: var(--sb-accent) !important;
  font-weight: 600 !important;
  color: #fafafa !important;
  -webkit-text-fill-color: #fafafa !important;
  box-shadow: inset 0 0 0 1px rgba(45, 212, 191, 0.08);
}
section[data-testid="stSidebar"] .stRadio label > div:first-child {
  margin-right: 0.55rem !important;
}
section[data-testid="stSidebar"] .stRadio [data-testid="stWidgetLabel"] {
  display: none !important;
}

/* Kill empty / light chrome boxes in the dark sidebar */
section[data-testid="stSidebar"] [data-testid="stVerticalBlockBorderWrapper"],
section[data-testid="stSidebar"] [data-testid="stExpander"],
section[data-testid="stSidebar"] [data-testid="stAlert"],
section[data-testid="stSidebar"] .stAlert,
section[data-testid="stSidebar"] div[data-testid="stDecoration"],
section[data-testid="stSidebar"] header,
section[data-testid="stSidebar"] [data-testid="stHeader"] {
  background: transparent !important;
  border: none !important;
  box-shadow: none !important;
}
section[data-testid="stSidebar"] hr {
  border: none !important;
  border-top: 1px solid rgba(148, 163, 184, 0.16) !important;
  background: transparent !important;
  margin: 1rem 0 !important;
}

/* Search match rows (dark suggestion panel — no white chrome) */
section[data-testid="stSidebar"] .stButton {
  margin-bottom: 0.25rem !important;
  background: transparent !important;
}
section[data-testid="stSidebar"] .stButton > button {
  background: #1a1a1e !important;
  color: #e4e4e7 !important;
  -webkit-text-fill-color: #e4e4e7 !important;
  border: 1px solid #3f3f46 !important;
  border-radius: 8px !important;
  min-height: 2.35rem !important;
  padding: 0.4rem 0.7rem !important;
  text-align: left !important;
  justify-content: flex-start !important;
  white-space: nowrap !important;
  overflow: hidden !important;
  text-overflow: ellipsis !important;
  font-size: 0.84rem !important;
  font-weight: 500 !important;
  box-shadow: none !important;
}
section[data-testid="stSidebar"] .stButton > button:hover {
  border-color: var(--sb-accent) !important;
  background: rgba(45, 212, 191, 0.12) !important;
  color: #fafafa !important;
  -webkit-text-fill-color: #fafafa !important;
}
section[data-testid="stSidebar"] .stButton > button[kind="primary"],
section[data-testid="stSidebar"] .stButton > button[data-testid="baseButton-primary"] {
  background: rgba(45, 212, 191, 0.16) !important;
  border-color: rgba(45, 212, 191, 0.35) !important;
  color: #5eead4 !important;
  -webkit-text-fill-color: #5eead4 !important;
}
/* LangFuse tracing link in sidebar */
section[data-testid="stSidebar"] [data-testid="stLinkButton"] > a,
section[data-testid="stSidebar"] .stLinkButton > a {
  background: rgba(45, 212, 191, 0.14) !important;
  border: 1px solid rgba(45, 212, 191, 0.35) !important;
  border-radius: 8px !important;
  color: #5eead4 !important;
  -webkit-text-fill-color: #5eead4 !important;
  font-weight: 600 !important;
  font-size: 0.88rem !important;
  min-height: 2.45rem !important;
  box-shadow: none !important;
  justify-content: center !important;
}
section[data-testid="stSidebar"] [data-testid="stLinkButton"] > a:hover,
section[data-testid="stSidebar"] .stLinkButton > a:hover {
  background: rgba(45, 212, 191, 0.22) !important;
  border-color: var(--sb-accent) !important;
  color: #fafafa !important;
  -webkit-text-fill-color: #fafafa !important;
}
/* Kill light-theme white wrappers around search suggestions + iframe */
section[data-testid="stSidebar"] [data-testid="stElementContainer"],
section[data-testid="stSidebar"] [data-testid="element-container"],
section[data-testid="stSidebar"] [data-testid="stVerticalBlockBorderWrapper"],
section[data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div {
  background: transparent !important;
  background-color: transparent !important;
  box-shadow: none !important;
}
section[data-testid="stSidebar"] div[data-testid="stElementContainer"]:has(.stButton),
section[data-testid="stSidebar"] div[data-testid="stElementContainer"]:has(.sb-empty-hint),
section[data-testid="stSidebar"] div[data-testid="stElementContainer"]:has(.sb-suggest-label) {
  background: #18181b !important;
  background-color: #18181b !important;
  border-left: 1px solid #3f3f46 !important;
  border-right: 1px solid #3f3f46 !important;
  padding-left: 0.35rem !important;
  padding-right: 0.35rem !important;
}
section[data-testid="stSidebar"] div[data-testid="stElementContainer"]:has(.sb-suggest-label) {
  border-top: 1px solid #3f3f46 !important;
  border-top-left-radius: 10px !important;
  border-top-right-radius: 10px !important;
  padding-top: 0.35rem !important;
  margin-top: 0.25rem !important;
}
section[data-testid="stSidebar"] div[data-testid="stElementContainer"]:has(.stButton):last-of-type,
section[data-testid="stSidebar"] div[data-testid="stElementContainer"]:has(.sb-empty-hint) {
  border-bottom: 1px solid #3f3f46 !important;
  border-bottom-left-radius: 10px !important;
  border-bottom-right-radius: 10px !important;
  padding-bottom: 0.35rem !important;
  margin-bottom: 0.45rem !important;
}
section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"]:empty,
section[data-testid="stSidebar"] .element-container:has(> div:empty) {
  display: none !important;
  margin: 0 !important;
  padding: 0 !important;
  min-height: 0 !important;
}
section[data-testid="stSidebar"] [data-testid="stWidgetLabel"] {
  display: none !important;
}
/* Live search iframe — kill Streamlit's default white component chrome */
section[data-testid="stSidebar"] .stCustomComponentV1,
section[data-testid="stSidebar"] div[data-testid="stElementContainer"]:has(iframe),
section[data-testid="stSidebar"] div[data-testid="element-container"]:has(iframe),
section[data-testid="stSidebar"] iframe {
  background: #070708 !important;
  background-color: #070708 !important;
  border: none !important;
  box-shadow: none !important;
  width: 100% !important;
  max-width: 100% !important;
  overflow: hidden !important;
}
section[data-testid="stSidebar"] iframe {
  min-height: 44px !important;
  height: 44px !important;
  max-height: 44px !important;
  color-scheme: dark !important;
}
section[data-testid="stSidebar"] .stCustomComponentV1 {
  margin: 0 0 0.25rem !important;
  padding: 0 !important;
  background: #070708 !important;
}
section[data-testid="stSidebar"] div[data-testid="stElementContainer"]:has(iframe) {
  border: none !important;
  border-radius: 0 !important;
  padding: 0 !important;
  margin: 0 !important;
  background: #070708 !important;
}

/* Status strip — premium metric cards */
.status-strip {
  display: grid;
  grid-template-columns: repeat(6, minmax(0, 1fr));
  gap: 1rem;
  margin-top: 0.25rem;
  margin-bottom: 1rem;
}
.status-cell {
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  padding: 1rem 1.05rem;
  min-height: 5.25rem;
  box-shadow: var(--shadow);
  transition: box-shadow 180ms ease, transform 180ms ease, border-color 180ms ease;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  gap: 0.45rem;
}
.status-cell:hover {
  box-shadow: var(--shadow-hover);
  transform: translateY(-1px);
  border-color: #3f3f46;
}
.status-label {
  font-size: 0.72rem; text-transform: uppercase; letter-spacing: 0.08em;
  color: var(--muted) !important; -webkit-text-fill-color: var(--muted) !important;
  font-weight: 650;
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
}
.status-icon {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 1.15rem;
  height: 1.15rem;
  border-radius: 6px;
  background: rgba(45,212,191,0.10);
  color: var(--teal) !important;
  -webkit-text-fill-color: var(--teal) !important;
  font-size: 0.58rem;
  font-weight: 700;
  letter-spacing: 0;
  text-transform: none;
  flex: 0 0 auto;
}
.status-value {
  font-size: 1.05rem; font-weight: 700; margin-top: 0;
  color: var(--ink) !important; -webkit-text-fill-color: var(--ink) !important;
  line-height: 1.25;
  word-break: break-word;
}
.status-value.ok { color: var(--ok) !important; -webkit-text-fill-color: var(--ok) !important; }
.status-value.warn { color: var(--warn) !important; -webkit-text-fill-color: var(--warn) !important; }
.status-value.bad { color: var(--bad) !important; -webkit-text-fill-color: var(--bad) !important; }
.status-value.teal { color: var(--teal-deep) !important; -webkit-text-fill-color: var(--teal-deep) !important; }

.chip {
  display: inline-flex; align-items: center;
  padding: 0.22rem 0.6rem; border-radius: 999px;
  font-size: 0.78rem; font-weight: 700; letter-spacing: 0.02em;
}
.chip.badge-ok { background: rgba(52,211,153,0.12); color: var(--ok) !important; -webkit-text-fill-color: var(--ok) !important; }
.chip.badge-warn { background: rgba(251,191,36,0.10); color: var(--warn) !important; -webkit-text-fill-color: var(--warn) !important; }
.chip.badge-bad { background: rgba(248,113,113,0.12); color: var(--bad) !important; -webkit-text-fill-color: var(--bad) !important; }
.chip.badge-mute { background: #1f1f23; color: var(--muted) !important; -webkit-text-fill-color: var(--muted) !important; }
.chip.badge-sea { background: rgba(45,212,191,0.10); color: var(--teal-deep) !important; -webkit-text-fill-color: var(--teal-deep) !important; }

/* Pipeline — workflow pills */
.pipeline-track {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.45rem;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  padding: 0.85rem 1rem;
  margin-bottom: 1.5rem;
  box-shadow: var(--shadow);
}
.pipe-sep {
  width: 12px; height: 1px;
  background: #3f3f46;
  flex: 0 0 auto;
}
.pipe-pill {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  padding: 0.4rem 0.75rem;
  border-radius: 999px;
  font-size: 0.8rem;
  font-weight: 600;
  background: #18181b;
  color: var(--muted) !important;
  -webkit-text-fill-color: var(--muted) !important;
  border: 1px solid transparent;
  transition: background 160ms ease, color 160ms ease, border-color 160ms ease;
}
.pipe-pill .pipe-icon { font-size: 0.72rem; line-height: 1; }
.pipe-pill.done {
  background: rgba(52,211,153,0.12);
  color: var(--ok) !important; -webkit-text-fill-color: var(--ok) !important;
  border-color: rgba(52,211,153,0.35);
}
.pipe-pill.active {
  background: rgba(45,212,191,0.10);
  color: var(--teal-deep) !important; -webkit-text-fill-color: var(--teal-deep) !important;
  border-color: #99f6e4;
}
.pipe-pill.blocked {
  background: rgba(248,113,113,0.12);
  color: var(--bad) !important; -webkit-text-fill-color: var(--bad) !important;
  border-color: rgba(248,113,113,0.35);
}
.pipe-pill.skipped {
  background: rgba(251,191,36,0.10);
  color: var(--warn) !important; -webkit-text-fill-color: var(--warn) !important;
}
.pipe-pill.pending {
  background: #18181b;
  color: #71717a !important; -webkit-text-fill-color: #71717a !important;
}

/* legacy pipeline-line kept for safety */
.pipeline-line { display: none; }

.card {
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  padding: 1.15rem 1.25rem;
  margin-bottom: 1rem;
  box-shadow: var(--shadow);
}
.badge {
  display: inline-flex;
  align-items: center;
  height: 1.7rem;
  padding: 0 0.7rem;
  border-radius: 999px;
  font-size: 0.75rem;
  font-weight: 700;
  margin: 0;
  letter-spacing: 0.01em;
  line-height: 1;
}
.badge-ok { background: rgba(52,211,153,0.12); color: #34d399 !important; -webkit-text-fill-color: #34d399 !important; }
.badge-warn { background: rgba(251,191,36,0.10); color: #fbbf24 !important; -webkit-text-fill-color: #fbbf24 !important; }
.badge-bad { background: rgba(248,113,113,0.12); color: #f87171 !important; -webkit-text-fill-color: #f87171 !important; }
.badge-mute { background: #1f1f23; color: #a1a1aa !important; -webkit-text-fill-color: #a1a1aa !important; }
.badge-info { background: rgba(129,140,248,0.12); color: var(--info) !important; -webkit-text-fill-color: var(--info) !important; }
.badge-sea { background: rgba(45,212,191,0.10); color: var(--teal-deep) !important; -webkit-text-fill-color: var(--teal-deep) !important; }

.val-status-card {
  margin-top: 0.25rem;
  margin-bottom: 1.5rem;
  padding: 1rem 1.15rem;
}
.badge-row {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  align-items: center;
}
.rules-row {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.55rem;
  margin-top: 0.85rem;
  padding-top: 0.75rem;
  border-top: 1px solid var(--line);
}
.rules-label {
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--muted) !important;
  -webkit-text-fill-color: var(--muted) !important;
}
.rules-hash,
code.rules-hash {
  font-family: var(--mono) !important;
  font-size: 0.78rem !important;
  line-height: 1.4 !important;
  color: #d4d4d8 !important;
  -webkit-text-fill-color: #d4d4d8 !important;
  background: #18181b !important;
  border: 1px solid var(--line) !important;
  border-radius: 8px !important;
  padding: 0.35rem 0.55rem !important;
  word-break: break-all;
  max-width: 100%;
  display: inline-block;
}

.section-label {
  font-family: var(--font) !important;
  font-size: 1.05rem !important;
  font-weight: 700 !important;
  color: var(--ink) !important;
  -webkit-text-fill-color: var(--ink) !important;
  margin: 1.5rem 0 0.75rem !important;
  letter-spacing: -0.01em;
}

.finding {
  border: 1px solid var(--line);
  border-left: 3px solid var(--teal);
  background: #121214;
  border-radius: 0 12px 12px 0;
  padding: 0.95rem 1.1rem;
  margin-bottom: 0.75rem;
  box-shadow: var(--shadow);
}
.finding.critical {
  border-left-color: var(--bad);
  background: rgba(248,113,113,0.08);
}
.finding.warning {
  border-left-color: var(--warn);
  background: rgba(251,191,36,0.08);
}
.finding.info {
  border-left-color: var(--info);
  background: rgba(129,140,248,0.08);
}
.finding-head {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.45rem;
  margin-bottom: 0.35rem;
}
.finding-sev {
  font-size: 0.78rem;
  font-weight: 700;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  color: var(--ink) !important;
  -webkit-text-fill-color: var(--ink) !important;
}
.finding.critical .finding-sev {
  color: var(--bad) !important;
  -webkit-text-fill-color: var(--bad) !important;
}
.finding.warning .finding-sev {
  color: var(--warn) !important;
  -webkit-text-fill-color: var(--warn) !important;
}
.finding-action {
  font-size: 0.75rem;
  font-weight: 600;
  color: var(--muted) !important;
  -webkit-text-fill-color: var(--muted) !important;
}
.finding-rule {
  font-family: var(--mono) !important;
  font-size: 0.82rem;
  font-weight: 600;
  color: var(--ink) !important;
  -webkit-text-fill-color: var(--ink) !important;
  margin-bottom: 0.35rem;
  word-break: break-word;
}
.finding-msg {
  font-size: 0.9rem;
  line-height: 1.55;
  color: #a1a1aa !important;
  -webkit-text-fill-color: #a1a1aa !important;
}

.gap-panel {
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 12px;
  padding: 1rem 1.1rem;
  margin-bottom: 1rem;
  min-height: 5.5rem;
  box-shadow: var(--shadow);
}
.gap-panel-title {
  font-size: 0.92rem;
  font-weight: 700;
  color: var(--ink) !important;
  -webkit-text-fill-color: var(--ink) !important;
  margin-bottom: 0.65rem;
}
.gap-list {
  margin: 0 0 0 1.05rem !important;
  padding: 0 !important;
}
.gap-list li {
  margin: 0.35rem 0 !important;
  color: var(--ink) !important;
  -webkit-text-fill-color: var(--ink) !important;
  font-size: 0.9rem;
  line-height: 1.45;
}

.empty-state {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  border-radius: 10px;
  padding: 0.75rem 0.9rem;
  font-size: 0.88rem;
  font-weight: 600;
  line-height: 1.4;
}
.empty-ok {
  background: rgba(52,211,153,0.10);
  color: #34d399 !important;
  -webkit-text-fill-color: #34d399 !important;
  border: 1px solid rgba(52,211,153,0.35);
}
.empty-icon {
  font-size: 0.85rem;
  line-height: 1;
}
.empty-text { font-weight: 600; }

.artifact-row {
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
  gap: 0.55rem;
  margin-bottom: 0.55rem;
}
.artifact-kind {
  font-size: 0.78rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--muted) !important;
  -webkit-text-fill-color: var(--muted) !important;
  min-width: 3.5rem;
}
.artifact-uri,
code.artifact-uri {
  font-family: var(--mono) !important;
  font-size: 0.78rem !important;
  background: #18181b !important;
  border: 1px solid var(--line) !important;
  border-radius: 8px !important;
  padding: 0.3rem 0.5rem !important;
  color: #d4d4d8 !important;
  -webkit-text-fill-color: #d4d4d8 !important;
  word-break: break-all;
  max-width: 100%;
}

/* Metrics row — keep horizontal, polish type */
div[data-testid="stMetric"] {
  background: transparent !important;
  padding: 0.15rem 0.25rem 0.35rem !important;
}
div[data-testid="stMetric"] label,
div[data-testid="stMetric"] [data-testid="stMetricLabel"] {
  font-size: 0.72rem !important;
  font-weight: 650 !important;
  letter-spacing: 0.06em !important;
  text-transform: uppercase !important;
  color: var(--muted) !important;
  -webkit-text-fill-color: var(--muted) !important;
}
div[data-testid="stMetric"] [data-testid="stMetricValue"] {
  font-size: 1.45rem !important;
  font-weight: 700 !important;
  color: var(--ink) !important;
  -webkit-text-fill-color: var(--ink) !important;
  line-height: 1.2 !important;
}
div[data-testid="stHorizontalBlock"] {
  gap: 1rem !important;
  margin-bottom: 0.35rem !important;
}

/* Expanders — Audit artifacts / More case fields / Audit notes */
div[data-testid="stExpander"] {
  background: var(--surface) !important;
  border: 1px solid var(--line) !important;
  border-radius: 12px !important;
  box-shadow: var(--shadow) !important;
  margin: 0.65rem 0 0.85rem !important;
  overflow: hidden;
}
div[data-testid="stExpander"] details {
  border: none !important;
}
div[data-testid="stExpander"] summary {
  padding: 0.7rem 1rem !important;
  display: flex !important;
  align-items: center !important;
  gap: 0.5rem !important;
}
div[data-testid="stExpander"] summary,
div[data-testid="stExpander"] [data-testid="stExpanderToggleIcon"] {
  color: var(--ink) !important;
}
div[data-testid="stExpander"] summary span,
div[data-testid="stExpander"] summary p {
  font-weight: 700 !important;
  color: #f4f4f5 !important;
  -webkit-text-fill-color: #f4f4f5 !important;
  font-size: 0.95rem !important;
  line-height: 1.25 !important;
}
div[data-testid="stExpander"] [data-testid="stExpanderDetails"],
div[data-testid="stExpander"] .streamlit-expanderContent {
  padding: 0.15rem 1rem 0.9rem !important;
}

/* Code / JSON blocks */
[data-testid="stCode"],
pre, code {
  border-radius: 10px !important;
}
[data-testid="stCode"] {
  background: #18181b !important;
  border: 1px solid var(--line) !important;
  padding: 0.75rem 0.9rem !important;
  max-height: 280px;
  overflow: auto !important;
  font-size: 0.8rem !important;
}

/* Discharge Summary — hero letter */
.summary-hero {
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 14px;
  padding: 1.85rem 2rem 1.5rem;
  margin: 0 0 1.25rem;
  box-shadow: var(--shadow);
}
.summary-hero-head {
  margin-bottom: 1.35rem;
  padding-bottom: 1.15rem;
  border-bottom: 1px solid var(--line);
}
.summary-hero-kicker {
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--teal) !important;
  -webkit-text-fill-color: var(--teal) !important;
  margin-bottom: 0.45rem;
}
.summary-hero-title {
  font-family: var(--display) !important;
  font-size: 1.75rem !important;
  font-weight: 700 !important;
  color: var(--ink) !important;
  -webkit-text-fill-color: var(--ink) !important;
  margin: 0 !important;
  letter-spacing: -0.02em;
  line-height: 1.2 !important;
}
.summary-hero-lede {
  margin: 0.45rem 0 0 !important;
  color: var(--muted) !important;
  -webkit-text-fill-color: var(--muted) !important;
  font-size: 0.95rem !important;
  line-height: 1.5 !important;
}
.summary-hero-body {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
.summary-block {
  background: #121214;
  border: 1px solid var(--line);
  border-radius: 12px;
  padding: 1.1rem 1.2rem 1rem;
}
.summary-block-title {
  font-family: var(--font) !important;
  font-size: 1.25rem !important;
  font-weight: 600 !important;
  color: var(--ink) !important;
  -webkit-text-fill-color: var(--ink) !important;
  margin: 0 0 0.7rem !important;
  letter-spacing: -0.01em;
}
.summary-block-body {
  color: var(--ink) !important;
  font-size: 0.98rem !important;
  line-height: 1.65 !important;
}
.summary-block-body p {
  margin: 0 0 0.55rem !important;
  color: var(--ink) !important;
}
.summary-block-body p:last-child { margin-bottom: 0 !important; }
.summary-block-body ul {
  margin: 0.15rem 0 0.25rem 1.15rem !important;
  padding: 0 !important;
}
.summary-block-body li {
  margin: 0.35rem 0 !important;
  color: var(--ink) !important;
  padding-left: 0.15rem;
}
.summary-block-body strong {
  color: var(--teal-deep) !important;
  font-weight: 650 !important;
}
.summary-block-body code {
  background: #1f1f23;
  border-radius: 6px;
  padding: 0.1rem 0.35rem;
  font-size: 0.88em;
}

/* legacy summary classes unused */
.summary-letter, .summary-section { display: none; }

/* HITL Corrections — zones + workflow chrome */
.hitl-zone {
  background: transparent;
  border: none;
  border-radius: 0;
  padding: 0;
  margin: 1.5rem 0 0.5rem;
  box-shadow: none;
}
.hitl-zone.hitl2,
.hitl-zone.hitl1,
.hitl-zone.clear {
  border-top: none;
  padding-top: 0;
}
.hitl-zone-head {
  display: flex !important;
  flex-direction: row !important;
  align-items: center !important;
  flex-wrap: wrap !important;
  gap: 0.45rem !important;
  margin-bottom: 0.2rem !important;
}
.hitl-zone-head .label,
.hitl-editor-block .ttl .label,
.hitl-section-title,
.corr-group-title {
  font-family: var(--font) !important;
  font-size: 1.2rem !important;
  font-weight: 700 !important;
  color: var(--ink) !important;
  -webkit-text-fill-color: var(--ink) !important;
  margin-right: 0.1rem !important;
  letter-spacing: -0.015em;
  line-height: 1.25 !important;
}
.hitl-zone-head .sep,
.hitl-editor-block .ttl .sep {
  color: var(--muted) !important; -webkit-text-fill-color: var(--muted) !important;
  font-weight: 600; margin: 0 0.1rem;
}
.hitl-zone-head .tag,
.hitl-editor-block .tag,
.hitl-issue-top .tag,
.corr-group-head .tag {
  display: inline-flex !important;
  align-items: center !important;
  font-size: 0.66rem !important; font-weight: 700 !important;
  letter-spacing: 0.06em; text-transform: uppercase;
  padding: 0.18rem 0.5rem !important; border-radius: 999px !important;
  margin-left: 0.1rem !important;
  height: 1.35rem;
}
.tag-hitl2 { background: rgba(248,113,113,0.18); color: var(--bad) !important; -webkit-text-fill-color: var(--bad) !important; }
.tag-hitl1 { background: rgba(251,191,36,0.16); color: #fb923c !important; -webkit-text-fill-color: #fb923c !important; }
.tag-shared { background: rgba(129,140,248,0.16); color: #a5b4fc !important; -webkit-text-fill-color: #a5b4fc !important; }
.hitl-zone-lede,
.hitl-section-lede {
  color: var(--muted) !important; -webkit-text-fill-color: var(--muted) !important;
  font-size: 0.88rem !important; margin: 0 0 0.75rem !important; line-height: 1.4 !important;
}

.hitl-overview {
  display: grid;
  grid-template-columns: minmax(0, 1.2fr) minmax(0, 1fr);
  gap: 1rem;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 12px;
  padding: 1.1rem 1.25rem;
  margin: 0 0 1.25rem;
  box-shadow: var(--shadow);
  border-left: 3px solid var(--teal);
}
.hitl-overview-kicker {
  font-size: 0.7rem; font-weight: 700; letter-spacing: 0.1em;
  text-transform: uppercase; color: var(--teal) !important;
  -webkit-text-fill-color: var(--teal) !important; margin-bottom: 0.25rem;
}
.hitl-overview-title {
  font-family: var(--display) !important;
  font-size: 1.5rem !important; font-weight: 700 !important;
  color: var(--ink) !important; -webkit-text-fill-color: var(--ink) !important;
  letter-spacing: -0.02em; margin: 0 !important; line-height: 1.2;
}
.hitl-overview-lede {
  margin: 0.35rem 0 0 !important; color: var(--muted) !important;
  -webkit-text-fill-color: var(--muted) !important; font-size: 0.88rem !important;
  line-height: 1.45 !important;
}
.hitl-overview-metrics {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 0.6rem;
}
.hitl-ov-metric {
  background: #18181b;
  border: 1px solid var(--line);
  border-radius: 10px;
  padding: 0.65rem 0.75rem;
}
.hitl-ov-metric .k {
  font-size: 0.68rem; font-weight: 700; letter-spacing: 0.06em;
  text-transform: uppercase; color: var(--muted) !important;
  -webkit-text-fill-color: var(--muted) !important;
}
.hitl-ov-metric .v {
  margin-top: 0.2rem; font-size: 1.15rem; font-weight: 700;
  color: var(--ink) !important; -webkit-text-fill-color: var(--ink) !important;
  line-height: 1.2;
}
.hitl-ov-metric .v.tone-bad { color: var(--bad) !important; -webkit-text-fill-color: var(--bad) !important; }
.hitl-ov-metric .v.tone-warn { color: var(--warn) !important; -webkit-text-fill-color: var(--warn) !important; }

.hitl-issue-card {
  background: var(--surface);
  border: 1px solid var(--line);
  border-left: 3px solid var(--line);
  border-radius: 0 12px 12px 0;
  padding: 0.85rem 1rem;
  margin: 0 0 0.55rem;
  box-shadow: var(--shadow);
}
.hitl-issue-card.critical {
  border-left-color: var(--bad);
  background: rgba(248,113,113,0.08);
}
.hitl-issue-card.warning {
  border-left-color: #fbbf24;
  background: rgba(251,191,36,0.08);
}
.hitl-issue-top {
  display: flex; flex-wrap: wrap; align-items: center; gap: 0.4rem;
  margin-bottom: 0.35rem;
}
.hitl-issue-title {
  font-size: 0.98rem; font-weight: 700;
  color: var(--ink) !important; -webkit-text-fill-color: var(--ink) !important;
}
.hitl-kv {
  display: grid;
  grid-template-columns: 7.75rem minmax(0, 1fr);
  gap: 0.2rem 0.65rem;
  margin-top: 0.25rem;
  align-items: start;
}
.hitl-kv .k {
  font-size: 0.7rem; font-weight: 700; letter-spacing: 0.04em;
  text-transform: uppercase; color: var(--muted) !important;
  -webkit-text-fill-color: var(--muted) !important; padding-top: 0.1rem;
}
.hitl-kv .v {
  font-size: 0.88rem; line-height: 1.4;
  color: var(--ink) !important; -webkit-text-fill-color: var(--ink) !important;
}
.hitl-kv .v.muted { color: var(--muted) !important; -webkit-text-fill-color: var(--muted) !important; }
.hitl-kv .v.mono {
  font-family: var(--mono) !important;
  font-size: 0.8rem;
}
.hitl-kv .v.sev-critical { color: var(--bad) !important; -webkit-text-fill-color: var(--bad) !important; font-weight: 700; }
.hitl-kv .v.sev-warning { color: #fb923c !important; -webkit-text-fill-color: #fb923c !important; font-weight: 700; }

.hitl-alert {
  display: flex; gap: 0.55rem; align-items: flex-start;
  border: 1px solid var(--line); border-radius: 10px;
  padding: 0.55rem 0.75rem; margin: 0 0 0.55rem;
  background: #18181b;
}
.hitl-alert.bad { background: rgba(248,113,113,0.10); border-color: rgba(248,113,113,0.35); }
.hitl-alert.warn { background: rgba(251,191,36,0.10); border-color: rgba(251,191,36,0.35); }
.hitl-alert-icon {
  width: 1.25rem; height: 1.25rem; border-radius: 999px;
  display: inline-flex; align-items: center; justify-content: center;
  font-size: 0.7rem; font-weight: 800; flex: 0 0 auto;
  background: rgba(248,113,113,0.18); color: var(--bad) !important;
}
.hitl-alert.warn .hitl-alert-icon { background: rgba(251,191,36,0.18); color: #fbbf24 !important; }
.hitl-alert-title {
  font-size: 0.86rem; font-weight: 700;
  color: var(--ink) !important; -webkit-text-fill-color: var(--ink) !important;
}
.hitl-alert-body {
  font-size: 0.8rem; color: var(--muted) !important;
  -webkit-text-fill-color: var(--muted) !important; line-height: 1.35; margin-top: 0.1rem;
}

.hitl-section-title {
  margin: 1.5rem 0 0.25rem !important;
}
.hitl-section-lede {
  margin: 0 0 0.75rem !important;
}

/* Corrections panels — st.container(border=True) + compact header */
div[data-testid="stVerticalBlockBorderWrapper"] {
  margin: 0 0 0.85rem !important;
  border-radius: 12px !important;
  border-color: var(--line) !important;
  background: var(--surface) !important;
}
div[data-testid="stVerticalBlockBorderWrapper"] > div[data-testid="stVerticalBlock"] {
  gap: 0.35rem !important;
  padding: 0.2rem 0.15rem 0.45rem !important;
}
.corr-panel-mark {
  display: none !important;
  height: 0 !important;
  margin: 0 !important;
  padding: 0 !important;
}
.corr-group-banner {
  background: transparent;
  border: none;
  border-radius: 0;
  padding: 0.35rem 0 0.5rem;
  margin: 0;
  border-bottom: 1px solid var(--line);
  box-shadow: none;
}
.corr-group-head {
  display: flex; flex-wrap: wrap; align-items: center; gap: 0.4rem;
}
.corr-group-hint {
  margin-top: 0.25rem; font-size: 0.82rem; line-height: 1.35;
  color: var(--muted) !important; -webkit-text-fill-color: var(--muted) !important;
}
.corr-opt-label {
  font-size: 0.78rem; font-weight: 700; letter-spacing: 0.06em;
  text-transform: uppercase; color: var(--muted) !important;
  -webkit-text-fill-color: var(--muted) !important;
  margin: 0.65rem 0 0.25rem;
}
.audit-card-lede {
  color: var(--muted) !important; -webkit-text-fill-color: var(--muted) !important;
  font-size: 0.84rem; margin: 0 0 0.55rem; line-height: 1.4;
}
.hitl-clear-banner {
  display: flex; gap: 0.55rem; align-items: flex-start;
  background: rgba(52,211,153,0.10); border: 1px solid rgba(52,211,153,0.35); border-radius: 12px;
  padding: 0.85rem 1rem; margin: 0.85rem 0 0.75rem;
}
.empty-state {
  margin: 0 0 0.55rem !important;
  padding: 0.6rem 0.8rem !important;
}

/* Label → input proximity + consistent control height */
[data-testid="stAppViewContainer"] div[data-testid="stWidgetLabel"] {
  margin-bottom: 0.2rem !important;
  padding-bottom: 0 !important;
  min-height: 0 !important;
}
[data-testid="stAppViewContainer"] div[data-testid="stWidgetLabel"] p,
[data-testid="stAppViewContainer"] div[data-testid="stWidgetLabel"] label {
  font-size: 0.82rem !important;
  font-weight: 600 !important;
  color: #a1a1aa !important;
  -webkit-text-fill-color: #a1a1aa !important;
  line-height: 1.25 !important;
}
[data-testid="stAppViewContainer"] .stTextInput,
[data-testid="stAppViewContainer"] .stSelectbox,
[data-testid="stAppViewContainer"] .stTextArea,
[data-testid="stAppViewContainer"] .stCheckbox,
[data-testid="stAppViewContainer"] .stNumberInput,
[data-testid="stAppViewContainer"] .stDateInput {
  margin-bottom: 0.45rem !important;
}
[data-testid="stAppViewContainer"] .stTextInput > div > div,
[data-testid="stAppViewContainer"] .stSelectbox > div > div,
[data-testid="stAppViewContainer"] .stNumberInput > div > div,
[data-testid="stAppViewContainer"] .stDateInput > div > div {
  min-height: 2.5rem !important;
}
[data-testid="stAppViewContainer"] .stTextInput input,
[data-testid="stAppViewContainer"] .stNumberInput input,
[data-testid="stAppViewContainer"] .stDateInput input,
[data-testid="stAppViewContainer"] .stSelectbox [data-baseweb="select"] > div {
  min-height: 2.5rem !important;
  border-radius: 10px !important;
  font-size: 0.95rem !important;
}
[data-testid="stAppViewContainer"] .stTextArea textarea {
  border-radius: 10px !important;
  font-size: 0.95rem !important;
  line-height: 1.45 !important;
  min-height: 6.5rem !important;
}

/* —— Upload New Patients (standalone, premium minimal) —— */
.upload-page {
  max-width: 880px;
  margin: 0 auto 0.55rem;
  text-align: center;
}
.upload-page-title {
  font-family: var(--display) !important;
  font-size: 1.65rem !important;
  font-weight: 700 !important;
  color: var(--ink) !important;
  -webkit-text-fill-color: var(--ink) !important;
  letter-spacing: -0.02em;
  margin: 0 0 0.2rem !important;
  line-height: 1.2 !important;
}
.upload-page-lede {
  color: var(--muted) !important;
  -webkit-text-fill-color: var(--muted) !important;
  font-size: 0.9rem !important;
  line-height: 1.4 !important;
  margin: 0 auto !important;
  max-width: 30rem;
}
.upload-field-title {
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: #a1a1aa !important;
  -webkit-text-fill-color: #a1a1aa !important;
  margin: 0 0 0.35rem;
  text-align: center;
}
.upload-formats-note {
  margin: 0.35rem 0 0.55rem !important;
  text-align: center;
  font-size: 0.78rem !important;
  color: #71717a !important;
  -webkit-text-fill-color: #71717a !important;
  line-height: 1.35 !important;
}
.upload-cta-mark { display: none !important; height: 0 !important; margin: 0 !important; padding: 0 !important; }

.upload-success-banner {
  max-width: 880px;
  margin: 0.85rem auto 0;
  display: flex;
  align-items: flex-start;
  gap: 0.7rem;
  padding: 0.85rem 1.05rem;
  border-radius: 12px;
  background: rgba(52,211,153,0.12);
  border: 1px solid rgba(52,211,153,0.35);
  box-shadow: 0 1px 2px rgba(15, 23, 42, 0.03);
  text-align: left;
}
.upload-success-check {
  flex: 0 0 auto;
  width: 1.55rem;
  height: 1.55rem;
  border-radius: 999px;
  background: #34d399;
  color: #141416 !important;
  -webkit-text-fill-color: #141416 !important;
  font-size: 0.85rem;
  font-weight: 700;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  margin-top: 0.05rem;
}
.upload-success-banner strong {
  display: block;
  color: #6ee7b7 !important;
  -webkit-text-fill-color: #6ee7b7 !important;
  font-size: 0.95rem;
  font-weight: 700;
  line-height: 1.3;
}
.upload-success-meta {
  display: block;
  margin-top: 0.2rem;
  color: #34d399 !important;
  -webkit-text-fill-color: #34d399 !important;
  font-size: 0.8rem;
  line-height: 1.35;
  word-break: break-word;
}

/* Main upload container */
[data-testid="stAppViewContainer"] div[data-testid="stVerticalBlockBorderWrapper"]:has(.upload-card-mark) {
  max-width: 880px;
  margin-left: auto !important;
  margin-right: auto !important;
  border-radius: 14px !important;
  border: 1px solid var(--line) !important;
  background: var(--surface) !important;
  box-shadow: 0 1px 2px rgba(15, 23, 42, 0.03), 0 8px 24px rgba(15, 23, 42, 0.04) !important;
}
[data-testid="stAppViewContainer"] div[data-testid="stVerticalBlockBorderWrapper"]:has(.upload-card-mark) > div[data-testid="stVerticalBlock"] {
  gap: 0.35rem !important;
  padding: 1.55rem 1.85rem 1.4rem !important; /* ~25–30px */
}
.upload-card-mark { display: none !important; height: 0 !important; margin: 0 !important; padding: 0 !important; }

/* Patient ID — tighter under subtitle */
[data-testid="stAppViewContainer"] div[data-testid="stVerticalBlockBorderWrapper"]:has(.upload-card-mark) [data-testid="stTextInput"] {
  margin-bottom: 0.45rem !important;
}
[data-testid="stAppViewContainer"] div[data-testid="stVerticalBlockBorderWrapper"]:has(.upload-card-mark) [data-testid="stTextInput"] label p {
  font-size: 0.8rem !important;
  font-weight: 600 !important;
  color: #a1a1aa !important;
  -webkit-text-fill-color: #a1a1aa !important;
}
[data-testid="stAppViewContainer"] div[data-testid="stVerticalBlockBorderWrapper"]:has(.upload-card-mark) [data-testid="stTextInput"] input {
  border-radius: 10px !important;
  min-height: 2.55rem !important;
}

/* Drop zones — compact, centered, premium (Streamlit 1.61: Upload btn + limit text) */
[data-testid="stAppViewContainer"] div[data-testid="stVerticalBlockBorderWrapper"]:has(.upload-card-mark) .stFileUploader {
  margin-bottom: 0 !important;
}
[data-testid="stAppViewContainer"] div[data-testid="stVerticalBlockBorderWrapper"]:has(.upload-card-mark) [data-testid="stFileUploaderDropzone"] {
  min-height: 4.1rem !important;
  padding: 0.7rem 0.75rem !important;
  border-radius: 12px !important;
  border: 1.5px dashed #3f3f46 !important;
  background: linear-gradient(180deg, #18181b 0%, #1f1f23 100%) !important;
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  justify-content: center !important;
  gap: 0.35rem !important;
  transition: border-color 160ms ease, background 160ms ease, box-shadow 160ms ease !important;
}
[data-testid="stAppViewContainer"] div[data-testid="stVerticalBlockBorderWrapper"]:has(.upload-card-mark) [data-testid="stFileUploaderDropzone"]:hover {
  border-color: #2dd4bf !important;
  background: linear-gradient(180deg, rgba(45,212,191,0.10) 0%, rgba(45,212,191,0.08) 100%) !important;
  box-shadow: 0 0 0 3px rgba(15, 118, 110, 0.08) !important;
}
/* Drag-over: Streamlit sets inset primary shadow via isDragActive */
[data-testid="stAppViewContainer"] div[data-testid="stVerticalBlockBorderWrapper"]:has(.upload-card-mark) [data-testid="stFileUploaderDropzone"]:focus-within {
  border-color: #2dd4bf !important;
  border-style: solid !important;
  background: rgba(45,212,191,0.10) !important;
  box-shadow: 0 0 0 3px rgba(15, 118, 110, 0.12) !important;
}

/* Hide Streamlit's long "200MB per file • TXT, PDF…" — we render a short hint ourselves */
[data-testid="stAppViewContainer"]:has(.upload-page) [data-testid="stFileUploaderDropzoneInstructions"],
[data-testid="stAppViewContainer"]:has(.upload-card-mark) [data-testid="stFileUploaderDropzoneInstructions"] {
  display: none !important;
}

.upload-slot-hint {
  margin: 0.25rem 0 0;
  text-align: center;
  font-size: 0.72rem;
  font-weight: 500;
  letter-spacing: 0.03em;
  color: #71717a !important;
  -webkit-text-fill-color: #71717a !important;
  line-height: 1.3;
}
.upload-selected {
  margin: 0.3rem 0 0;
  text-align: center;
  padding: 0.4rem 0.55rem;
  border-radius: 8px;
  background: rgba(52,211,153,0.12);
  border: 1px solid rgba(52,211,153,0.35);
  color: #6ee7b7 !important;
  -webkit-text-fill-color: #6ee7b7 !important;
  font-size: 0.84rem;
  font-weight: 600;
  word-break: break-word;
  line-height: 1.3;
}

/* Larger Upload control + icon, centered */
[data-testid="stAppViewContainer"] div[data-testid="stVerticalBlockBorderWrapper"]:has(.upload-card-mark) [data-testid="stFileUploaderDropzone"] button {
  border-radius: 9px !important;
  font-size: 0.82rem !important;
  font-weight: 650 !important;
  padding: 0.4rem 0.85rem !important;
  min-height: 2.15rem !important;
  border-color: #3f3f46 !important;
  color: #2dd4bf !important;
  background: #141416 !important;
  box-shadow: 0 1px 2px rgba(15, 23, 42, 0.04) !important;
}
[data-testid="stAppViewContainer"] div[data-testid="stVerticalBlockBorderWrapper"]:has(.upload-card-mark) [data-testid="stFileUploaderDropzone"] button:hover {
  border-color: #2dd4bf !important;
  background: rgba(45,212,191,0.10) !important;
}
[data-testid="stAppViewContainer"] div[data-testid="stVerticalBlockBorderWrapper"]:has(.upload-card-mark) [data-testid="stFileUploaderDropzone"] button svg,
[data-testid="stAppViewContainer"] div[data-testid="stVerticalBlockBorderWrapper"]:has(.upload-card-mark) [data-testid="stFileUploaderDropzone"] button [data-testid="stIconMaterial"] {
  width: 1.35rem !important;
  height: 1.35rem !important;
  font-size: 1.35rem !important;
  color: #2dd4bf !important;
}

/* Selected file chip — ✓ filename (Streamlit 1.61 renders files inside the dropzone) */
[data-testid="stAppViewContainer"] div[data-testid="stVerticalBlockBorderWrapper"]:has(.upload-card-mark) [data-testid="stFileUploaderFile"],
[data-testid="stAppViewContainer"] div[data-testid="stVerticalBlockBorderWrapper"]:has(.upload-card-mark) .uploadedFile {
  margin: 0 !important;
  width: 100% !important;
  padding: 0.45rem 0.55rem !important;
  border-radius: 10px !important;
  background: rgba(52,211,153,0.12) !important;
  border: 1px solid rgba(52,211,153,0.35) !important;
}
[data-testid="stAppViewContainer"] div[data-testid="stVerticalBlockBorderWrapper"]:has(.upload-card-mark) [data-testid="stFileUploaderFileName"]::before,
[data-testid="stAppViewContainer"] div[data-testid="stVerticalBlockBorderWrapper"]:has(.upload-card-mark) .uploadedFileName::before {
  content: "✓ ";
  color: #6ee7b7;
  font-weight: 700;
}
[data-testid="stAppViewContainer"] div[data-testid="stVerticalBlockBorderWrapper"]:has(.upload-card-mark) [data-testid="stFileUploaderFileName"],
[data-testid="stAppViewContainer"] div[data-testid="stVerticalBlockBorderWrapper"]:has(.upload-card-mark) .uploadedFileName {
  color: #6ee7b7 !important;
  -webkit-text-fill-color: #6ee7b7 !important;
  font-weight: 600 !important;
  font-size: 0.84rem !important;
  word-break: break-word;
  white-space: normal !important;
}
[data-testid="stAppViewContainer"] div[data-testid="stVerticalBlockBorderWrapper"]:has(.upload-card-mark) [data-testid="stFileUploaderFile"] small,
[data-testid="stAppViewContainer"] div[data-testid="stVerticalBlockBorderWrapper"]:has(.upload-card-mark) [data-testid="stFileUploaderFileSize"],
[data-testid="stAppViewContainer"] div[data-testid="stVerticalBlockBorderWrapper"]:has(.upload-card-mark) .uploadedFileSize {
  display: none !important;
}
/* When a file is present, soft solid border on the zone */
[data-testid="stAppViewContainer"] div[data-testid="stVerticalBlockBorderWrapper"]:has(.upload-card-mark) .stFileUploader:has([data-testid="stFileUploaderFile"]) [data-testid="stFileUploaderDropzone"],
[data-testid="stAppViewContainer"] div[data-testid="stVerticalBlockBorderWrapper"]:has(.upload-card-mark) .stFileUploader:has(.uploadedFile) [data-testid="stFileUploaderDropzone"] {
  border-style: solid !important;
  border-color: rgba(52,211,153,0.35) !important;
  background: rgba(52,211,153,0.10) !important;
  min-height: 3.6rem !important;
}

/* Primary CTA — more prominent */
[data-testid="stAppViewContainer"] div[data-testid="stVerticalBlockBorderWrapper"]:has(.upload-card-mark) .stButton {
  margin-top: 0.1rem !important;
}
[data-testid="stAppViewContainer"] div[data-testid="stVerticalBlockBorderWrapper"]:has(.upload-card-mark) .stButton > button[kind="primary"],
[data-testid="stAppViewContainer"] div[data-testid="stVerticalBlockBorderWrapper"]:has(.upload-card-mark) .stButton > button[data-testid="baseButton-primary"] {
  min-height: 2.85rem !important;
  border-radius: 10px !important;
  font-size: 0.95rem !important;
  font-weight: 700 !important;
  letter-spacing: 0.01em !important;
  background: linear-gradient(180deg, #2dd4bf 0%, #0f766e 100%) !important;
  border: none !important;
  box-shadow: 0 1px 2px rgba(15, 23, 42, 0.08), 0 6px 16px rgba(15, 118, 110, 0.22) !important;
}
[data-testid="stAppViewContainer"] div[data-testid="stVerticalBlockBorderWrapper"]:has(.upload-card-mark) .stButton > button[kind="primary"]:hover:not(:disabled),
[data-testid="stAppViewContainer"] div[data-testid="stVerticalBlockBorderWrapper"]:has(.upload-card-mark) .stButton > button[data-testid="baseButton-primary"]:hover:not(:disabled) {
  background: linear-gradient(180deg, #5eead4 0%, #2dd4bf 100%) !important;
  box-shadow: 0 2px 4px rgba(15, 23, 42, 0.1), 0 8px 20px rgba(15, 118, 110, 0.28) !important;
}
[data-testid="stAppViewContainer"] div[data-testid="stVerticalBlockBorderWrapper"]:has(.upload-card-mark) .stButton > button:disabled {
  opacity: 0.45 !important;
  box-shadow: none !important;
}

/* legacy issue styles kept for safety */
.hitl-issue {
  border: 1px solid rgba(248,113,113,0.35);
  border-left: 4px solid var(--bad);
  background: rgba(248,113,113,0.10);
  border-radius: 0 10px 10px 0;
  padding: 0.75rem 0.95rem;
  margin-bottom: 0.65rem;
}
.hitl-issue .rule {
  font-weight: 700; color: var(--bad) !important;
  -webkit-text-fill-color: var(--bad) !important; font-size: 0.9rem;
}
.hitl-issue .fix {
  color: var(--ink) !important; -webkit-text-fill-color: var(--ink) !important;
  font-size: 0.86rem; margin-top: 0.3rem;
}
.hitl-issue .msg {
  color: var(--muted) !important; -webkit-text-fill-color: var(--muted) !important;
  font-size: 0.78rem; margin-top: 0.3rem; line-height: 1.4;
}
.hitl-soft {
  border: 1px solid rgba(251,191,36,0.35);
  border-left: 4px solid #fbbf24;
  background: rgba(251,191,36,0.10);
  border-radius: 0 10px 10px 0;
  padding: 0.65rem 0.9rem;
  margin-bottom: 0.55rem;
  color: var(--ink) !important; -webkit-text-fill-color: var(--ink) !important;
  font-size: 0.86rem;
}
.hitl-soft .covered {
  color: var(--muted) !important; -webkit-text-fill-color: var(--muted) !important;
  font-size: 0.78rem; margin-top: 0.2rem;
}
.hitl-clear {
  border: 1px solid rgba(52,211,153,0.35);
  background: rgba(52,211,153,0.10);
  border-radius: 10px;
  padding: 0.85rem 1rem;
  color: var(--ok) !important; -webkit-text-fill-color: var(--ok) !important;
  font-weight: 600; font-size: 0.9rem;
}
.hitl-editor-block {
  margin: 0.75rem 0 0.35rem;
  padding-top: 0.55rem;
  border-top: 1px solid var(--line);
}
.hitl-editor-block:first-of-type { border-top: none; padding-top: 0.1rem; }
.hitl-editor-block .ttl {
  display: flex !important; align-items: center !important; flex-wrap: wrap !important;
  gap: 0.35rem !important;
  font-weight: 700; font-size: 0.95rem;
  color: var(--ink) !important; -webkit-text-fill-color: var(--ink) !important;
  margin-bottom: 0.15rem;
}
.hitl-editor-block .sub {
  color: var(--muted) !important; -webkit-text-fill-color: var(--muted) !important;
  font-size: 0.8rem; margin-bottom: 0.45rem;
}
.hitl-actions {
  margin-top: 1.15rem;
  padding-top: 0.85rem;
  border-top: 1px solid var(--line);
  position: sticky;
  bottom: 0;
  z-index: 30;
  background: linear-gradient(180deg, rgba(247,249,252,0) 0%, var(--canvas) 22%, var(--canvas) 100%);
  padding-bottom: 0.25rem;
}
.hitl-actions-label {
  font-size: 0.7rem; font-weight: 700; letter-spacing: 0.08em;
  text-transform: uppercase; color: var(--muted) !important;
  -webkit-text-fill-color: var(--muted) !important;
  margin-bottom: 0.45rem;
}

/* Data editor polish */
div[data-testid="stDataFrame"],
div[data-testid="stDataEditor"] {
  border: 1px solid var(--line) !important;
  border-radius: 10px !important;
  overflow: hidden !important;
  background: var(--surface) !important;
  box-shadow: none !important;
  margin: 0.35rem 0 0.35rem !important;
}

@media (max-width: 900px) {
  .hitl-overview { grid-template-columns: 1fr; gap: 0.75rem; padding: 1rem; }
  .hitl-kv { grid-template-columns: 1fr; gap: 0.1rem; }
  .hitl-zone { margin: 1.15rem 0 0.4rem; }
  .hitl-section-title { margin: 1.15rem 0 0.2rem !important; }
  .hitl-actions { margin-top: 0.85rem; }
}

.doc-preview {
  white-space: pre-wrap;
  background: #070708;
  color: #e4e4e7 !important;
  -webkit-text-fill-color: #e4e4e7 !important;
  border-radius: 8px;
  padding: 0.85rem 1rem;
  max-height: 420px;
  overflow: auto;
  font-size: 0.85rem;
  line-height: 1.5;
  font-family: var(--mono) !important;
}

/* Buttons — equal-feel primary actions */
div[data-testid="stButton"] > button,
div[data-testid="stDownloadButton"] > button {
  border-radius: 10px !important;
  font-weight: 600 !important;
  font-size: 0.92rem !important;
  padding: 0.65rem 1.1rem !important;
  min-height: 2.75rem !important;
  border: 1px solid var(--line) !important;
  background: var(--surface) !important;
  color: var(--ink) !important;
  -webkit-text-fill-color: var(--ink) !important;
  box-shadow: var(--shadow) !important;
  transition: transform 160ms ease, box-shadow 160ms ease, background 160ms ease, border-color 160ms ease !important;
}
div[data-testid="stButton"] > button:hover,
div[data-testid="stDownloadButton"] > button:hover {
  transform: translateY(-1px) !important;
  box-shadow: var(--shadow-hover) !important;
  border-color: #3f3f46 !important;
}
div[data-testid="stButton"] > button[kind="primary"],
div[data-testid="stButton"] > button[data-testid="baseButton-primary"],
div[data-testid="stDownloadButton"] > button[kind="primary"],
div[data-testid="stDownloadButton"] > button[data-testid="baseButton-primary"] {
  background: var(--teal) !important;
  color: #042f2e !important;
  -webkit-text-fill-color: #042f2e !important;
  border: 1px solid var(--teal) !important;
}
div[data-testid="stButton"] > button[kind="primary"]:hover,
div[data-testid="stButton"] > button[data-testid="baseButton-primary"]:hover,
div[data-testid="stDownloadButton"] > button[kind="primary"]:hover,
div[data-testid="stDownloadButton"] > button[data-testid="baseButton-primary"]:hover {
  background: var(--teal-deep) !important;
  border-color: var(--teal-deep) !important;
}

header[data-testid="stHeader"] {
  background: #0a0a0b !important;
  border-bottom: 1px solid #27272a !important;
}
#MainMenu, footer { visibility: hidden; }

@media (max-width: 1100px) {
  .status-strip { grid-template-columns: repeat(3, minmax(0, 1fr)); }
  .summary-hero { padding: 1.5rem 1.35rem 1.25rem; }
}
@media (max-width: 700px) {
  .block-container {
    padding-left: 1rem !important;
    padding-right: 1rem !important;
  }
  .status-strip { grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 0.75rem; }
  .status-cell { min-height: 4.5rem; padding: 0.85rem 0.9rem; }
  .page-title, .summary-hero-title { font-size: 1.45rem !important; }
  .pipe-sep { display: none; }
  div[data-testid="stMetric"] [data-testid="stMetricValue"] {
    font-size: 1.2rem !important;
  }
  .rules-hash, code.rules-hash { font-size: 0.72rem !important; }
}



/* —— Dark theme polish overrides —— */
html, body, .stApp { color-scheme: dark !important; }
[data-testid="stAppViewContainer"] .stTextInput input,
[data-testid="stAppViewContainer"] .stNumberInput input,
[data-testid="stAppViewContainer"] .stDateInput input,
[data-testid="stAppViewContainer"] .stTextArea textarea,
[data-testid="stAppViewContainer"] .stSelectbox [data-baseweb="select"] > div {
  background-color: #18181b !important;
  color: #f4f4f5 !important;
  border-color: #27272a !important;
}
div[data-testid="stMetric"] {
  background: var(--surface) !important;
  border: 1px solid var(--line) !important;
  border-radius: var(--radius) !important;
  padding: 0.75rem 0.9rem !important;
}
[data-testid="stChatMessage"] {
  background: var(--surface) !important;
  border: 1px solid var(--line) !important;
}

/* RAG chat — assistant left, user right (Streamlit 1.61+) */
div[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) {
  display: flex !important;
  flex-direction: row-reverse !important;
  align-items: flex-start !important;
  justify-content: flex-start !important;
  margin-left: auto !important;
  margin-right: 0 !important;
  width: fit-content !important;
  max-width: min(78%, 42rem) !important;
  background: rgba(45, 212, 191, 0.14) !important;
  border: 1px solid rgba(45, 212, 191, 0.32) !important;
  border-radius: 14px 14px 4px 14px !important;
  padding: 0.75rem 0.95rem !important;
  gap: 0.65rem !important;
}
div[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarAssistant"]) {
  display: flex !important;
  flex-direction: row !important;
  align-items: flex-start !important;
  justify-content: flex-start !important;
  margin-left: 0 !important;
  margin-right: auto !important;
  width: fit-content !important;
  max-width: min(85%, 48rem) !important;
  background: #141416 !important;
  border: 1px solid #27272a !important;
  border-radius: 14px 14px 14px 4px !important;
  padding: 0.75rem 0.95rem !important;
  gap: 0.65rem !important;
}
[data-testid="stChatMessageAvatarUser"],
[data-testid="stChatMessageAvatarAssistant"] {
  flex: 0 0 auto !important;
  width: 2rem !important;
  height: 2rem !important;
  min-width: 2rem !important;
  min-height: 2rem !important;
  border-radius: 999px !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  visibility: visible !important;
  opacity: 1 !important;
}
[data-testid="stChatMessageAvatarUser"] {
  background: #ef4444 !important;
  color: #ffffff !important;
  -webkit-text-fill-color: #ffffff !important;
}
[data-testid="stChatMessageAvatarAssistant"] {
  background: #f97316 !important;
  color: #ffffff !important;
  -webkit-text-fill-color: #ffffff !important;
}
[data-testid="stChatMessageAvatarUser"] [data-testid="stIconMaterial"],
[data-testid="stChatMessageAvatarAssistant"] [data-testid="stIconMaterial"] {
  font-family: "Material Symbols Rounded" !important;
  color: #ffffff !important;
  -webkit-text-fill-color: #ffffff !important;
  font-size: 1.15rem !important;
}
div[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) [data-testid="stChatMessageContent"],
div[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarAssistant"]) [data-testid="stChatMessageContent"] {
  text-align: left !important;
}
div[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) [data-testid="stMarkdownContainer"] p,
div[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) [data-testid="stChatMessageContent"] {
  color: #ecfdf5 !important;
  -webkit-text-fill-color: #ecfdf5 !important;
}
/* Keep each bubble on its own row spanning the chat column */
div[data-testid="stVerticalBlock"]:has(> div [data-testid="stChatMessage"]) > div:has([data-testid="stChatMessage"]) {
  display: flex !important;
  width: 100% !important;
}
div[data-testid="stVerticalBlock"] > div:has([data-testid="stChatMessageAvatarUser"]) {
  justify-content: flex-end !important;
}
div[data-testid="stVerticalBlock"] > div:has([data-testid="stChatMessageAvatarAssistant"]) {
  justify-content: flex-start !important;
}
.stTabs [data-baseweb="tab-list"] {
  background: var(--surface) !important;
  border: 1px solid var(--line) !important;
  border-radius: 10px !important;
  padding: 0.25rem !important;
}
.stTabs [aria-selected="true"] {
  background: rgba(45,212,191,0.14) !important;
  color: #5eead4 !important;
}
div[data-testid="stButton"] > button[kind="primary"],
div[data-testid="stButton"] > button[data-testid="baseButton-primary"],
div[data-testid="stDownloadButton"] > button[kind="primary"],
div[data-testid="stDownloadButton"] > button[data-testid="baseButton-primary"] {
  background: #14b8a6 !important;
  color: #042f2e !important;
  -webkit-text-fill-color: #042f2e !important;
  border: 1px solid #2dd4bf !important;
}
div[data-testid="stButton"] > button[kind="primary"]:hover,
div[data-testid="stButton"] > button[data-testid="baseButton-primary"]:hover,
div[data-testid="stDownloadButton"] > button[kind="primary"]:hover,
div[data-testid="stDownloadButton"] > button[data-testid="baseButton-primary"]:hover {
  background: #2dd4bf !important;
  border-color: #5eead4 !important;
}
header[data-testid="stHeader"] {
  background: rgba(10,10,11,0.85) !important;
  backdrop-filter: blur(8px);
}
.doc-preview {
  background: #050506 !important;
  color: #d4d4d8 !important;
  -webkit-text-fill-color: #d4d4d8 !important;
  border: 1px solid var(--line) !important;
}
[data-testid="stCode"] {
  background: #18181b !important;
  border: 1px solid var(--line) !important;
  color: #e4e4e7 !important;
}
div[data-testid="stDataFrame"],
div[data-testid="stDataEditor"] {
  background: var(--surface) !important;
  border: 1px solid var(--line) !important;
}
.hitl-actions {
  background: linear-gradient(180deg, rgba(10,10,11,0) 0%, var(--canvas) 22%, var(--canvas) 100%) !important;
}
.status-value.teal { color: #5eead4 !important; -webkit-text-fill-color: #5eead4 !important; }
.chip.badge-ok, .badge-ok { background: rgba(52,211,153,0.14) !important; color: #34d399 !important; -webkit-text-fill-color: #34d399 !important; border: 1px solid rgba(52,211,153,0.3); }
.chip.badge-warn, .badge-warn { background: rgba(251,191,36,0.14) !important; color: #fbbf24 !important; -webkit-text-fill-color: #fbbf24 !important; border: 1px solid rgba(251,191,36,0.3); }
.chip.badge-bad, .badge-bad { background: rgba(248,113,113,0.14) !important; color: #f87171 !important; -webkit-text-fill-color: #f87171 !important; border: 1px solid rgba(248,113,113,0.3); }
.chip.badge-mute, .badge-mute { background: rgba(161,161,170,0.12) !important; color: #a1a1aa !important; -webkit-text-fill-color: #a1a1aa !important; border: 1px solid var(--line); }
.chip.badge-sea, .badge-sea { background: rgba(45,212,191,0.14) !important; color: #5eead4 !important; -webkit-text-fill-color: #5eead4 !important; border: 1px solid rgba(45,212,191,0.35); }

/* Visibility + header clearance (theme fixes) */
section[data-testid="stSidebar"] .brand-title,
section[data-testid="stSidebar"] .brand-title * {
  color: #fafafa !important;
  -webkit-text-fill-color: #fafafa !important;
  opacity: 1 !important;
}
section[data-testid="stSidebar"] .stRadio label:hover,
section[data-testid="stSidebar"] .stRadio label:has(input:checked) {
  color: #fafafa !important;
  -webkit-text-fill-color: #fafafa !important;
}
header[data-testid="stHeader"] {
  background: #0a0a0b !important;
  border-bottom: 1px solid #27272a !important;
  z-index: 999 !important;
}
[data-testid="stAppViewContainer"] > .main {
  padding-top: 0 !important;
}
[data-testid="stAppViewContainer"] .block-container {
  padding-top: 4.25rem !important;
}
section[data-testid="stSidebar"] .stRadio [role="radiogroup"] {
  gap: 0.3rem !important;
  padding: 0 !important;
  margin: 0 !important;
}
section[data-testid="stSidebar"] .stRadio label {
  margin-left: 0 !important;
  margin-right: 0 !important;
  width: 100% !important;
}
section[data-testid="stSidebar"] .patient-card {
  margin-left: 0;
  margin-right: 0;
}
.upload-success-check {
  color: #042f2e !important;
  -webkit-text-fill-color: #042f2e !important;
}
div[data-testid="stButton"] > button[kind="primary"],
div[data-testid="stButton"] > button[data-testid="baseButton-primary"],
div[data-testid="stDownloadButton"] > button[kind="primary"],
div[data-testid="stDownloadButton"] > button[data-testid="baseButton-primary"] {
  color: #042f2e !important;
  -webkit-text-fill-color: #042f2e !important;
}
"""

PIPELINE_STEPS: tuple[tuple[str, str], ...] = (
    ("monitor", "Monitor"),
    ("extract", "Extract"),
    ("normalize", "Normalize"),
    ("validate", "Validate"),
    ("index", "Index"),
    ("gate", "Gate"),
    ("summary_or_hitl", "Summary"),
)

PATIENT_NAMES: dict[str, str] = {
    "P1019": "Thomas Wright",
    "P1020": "Diego Morales",
    "P1021": "Rohan Gupta",
    "P1022": "Daan Bakker",
    "P1023": "Grace Bennett",
    "P1024": "Bram de Vries",
}


_NAV_LABELS: dict[str, str] = {
    "RAG Q&A": "RAG Assistant",
    "Upload new patients": "Upload New Patients",
}


def nav_label(page: str) -> str:
    """Text-only nav labels (no icons)."""
    return _NAV_LABELS.get(page, page)


def selected_patient_card_html(patient_id: str, patient_name: str = "") -> str:
    """Compact selected-patient card for the sidebar."""
    from html import escape

    pid = (patient_id or "").strip()
    if not pid:
        return (
            '<div class="patient-card patient-card-empty">'
            '<div class="patient-card-empty-msg">No patient selected</div>'
            "</div>"
        )
    name = (patient_name or "").strip()
    if not name:
        try:
            from dashboard.components.common import patient_display_name

            name = patient_display_name(pid)
        except Exception:
            name = PATIENT_NAMES.get(pid, "Patient")
    return (
        '<div class="patient-card">'
        f'<div class="patient-card-id">{escape(pid)}</div>'
        f'<div class="patient-card-name" title="{escape(name)}">{escape(name)}</div>'
        "</div>"
    )


def patient_card_html(patient_id: str, patient_name: str) -> str:
    return selected_patient_card_html(patient_id, patient_name)



_UNSET = object()


def pipeline_step_states(
    pipeline_result: dict | None,
    *,
    validation: object = _UNSET,
    summary: object = _UNSET,
) -> list[tuple[str, str, str, str]]:
    """Derive stepper UI state from pipeline outcomes (not just stages_run).

    Returns list of (key, label, state, mark) where state is one of:
    done | active | pending | blocked | skipped
    """
    result = pipeline_result or {}
    stages = list(result.get("stages_run") or [])
    if validation is _UNSET:
        validation_d: dict = result.get("validation") or {}
    else:
        validation_d = validation if isinstance(validation, dict) else {}
    if summary is _UNSET:
        summary_obj = result.get("summary")
    else:
        summary_obj = summary

    if validation_d:
        blocked = bool(validation_d.get("discharge_blocked"))
        needs_hitl = bool(validation_d.get("needs_hitl"))
        allow_summary = not (blocked or needs_hitl)
    else:
        gate = result.get("gate") or {}
        allow_summary = gate.get("allow_summary")
        blocked = bool(result.get("discharge_blocked"))
        needs_hitl = bool(result.get("needs_hitl"))
        if allow_summary is None:
            allow_summary = not (blocked or needs_hitl)

    gate_closed = (allow_summary is False) or blocked or (
        needs_hitl and summary_obj is None
    )
    gate_ran = "gate" in stages or "validate" in stages or bool(validation_d)

    out: list[tuple[str, str, str, str]] = []
    for key, label in PIPELINE_STEPS:
        ran = key in stages
        if key == "gate":
            if not gate_ran:
                state, mark = "pending", "○"
            elif gate_closed:
                state, mark = "blocked", "✕"
            else:
                state, mark = "done", "✓"
        elif key == "summary_or_hitl":
            if summary_obj is not None:
                state, mark = "done", "✓"
            elif gate_closed:
                state, mark = "skipped", "–"
            elif gate_ran or ran:
                state, mark = "active", "●"
            else:
                state, mark = "pending", "○"
        else:
            if ran:
                state, mark = "done", "✓"
            else:
                state, mark = "pending", "○"
        out.append((key, label, state, mark))
    return out


def inject_styles() -> None:
    import streamlit as st

    st.markdown(f"<style>{CUSTOM_CSS}</style>", unsafe_allow_html=True)
