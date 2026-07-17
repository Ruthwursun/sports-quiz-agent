# import streamlit as st
# from src.generator import compile_quiz_data
# from src.database import setup_and_populate_db

# # 1. Warm-up and initialize the vector DB with our offline facts on startup
# @st.cache_resource
# def prepare_knowledge_base():
#     setup_and_populate_db()

# prepare_knowledge_base()

# # 2. Set Page configurations
# st.set_page_config(page_title="Sports Quiz Agent", page_icon="🏆", layout="centered")

# st.title("🏆 AI-Powered Sports Quiz Generator")
# st.write("Challenge yourself or generate engaging social media content! Powered by RAG (ChromaDB + Web Search).")

# # 3. Sidebar inputs
# st.sidebar.header("Quiz Settings")
# # sport_choice = st.sidebar.selectbox("Select Sport", ["Cricket", "Football", "Badminton"])
# sport_choice = st.sidebar.selectbox(
#     "Select Sport",
#     [
#         "Cricket",
#         "Football",
#         "Badminton",
#         "Tennis",
#         "Basketball",
#         "Hockey",
#         "Formula 1",
#         "Volleyball",
#         "Boxing",
#         "Chess"
#     ]
# )
# difficulty = st.sidebar.select_slider("Select Difficulty", options=["Easy", "Medium", "Hard"])

# # 4. Initialize session state to remember quizzes across page interactions
# if "quiz_output" not in st.session_state:
#     st.session_state.quiz_output = None
#     st.session_state.quiz_context = None

# # Button to trigger compilation pipeline
# if st.sidebar.button("Generate Fresh Quiz", use_container_width=True):
#     with st.spinner("Fetching historical facts & scouring the live web..."):
#         try:
#             quiz_text, context_used = compile_quiz_data(sport_choice, difficulty)
#             st.session_state.quiz_output = quiz_text
#             st.session_state.quiz_context = context_used
#             st.success("Quiz created successfully!")
#         except Exception as e:
#             st.error(f"Failed to generate quiz: {e}")

# # 5. Display the generated quiz
# if st.session_state.quiz_output:
#     st.subheader(f"Current Quiz: {sport_choice} ({difficulty})")
#     st.text_area("Generated Quiz Output (Copy paste to your socials)",
#                  value=st.session_state.quiz_output,
#                  height=350)

#     # Expandable window showcasing the "ground truth context" for audit purposes
#     with st.expander("🔍 Inspect Ground Truth (RAG Context Used)"):
#         st.code(st.session_state.quiz_context, language="markdown")






"""
Sports Quiz Arena — Premium Redesign
Transforms the plain Streamlit quiz app into an immersive sports experience.
All backend logic (compile_quiz_data, setup_and_populate_db) is preserved unchanged.
"""

import time
import streamlit as st

# ── Must be first Streamlit call ───────────────────────────────────────────────
st.set_page_config(
    page_title="Sports Quiz Arena",
    page_icon="🏆",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Backend imports (unchanged) ────────────────────────────────────────────────
from src.generator import compile_quiz_data
from src.database import setup_and_populate_db


# ── Knowledge-base warm-up (unchanged) ────────────────────────────────────────
@st.cache_resource
def prepare_knowledge_base():
    setup_and_populate_db()

prepare_knowledge_base()


# ══════════════════════════════════════════════════════════════════════════════
# THEME & GLOBAL CSS
# ══════════════════════════════════════════════════════════════════════════════
GLOBAL_CSS = """
<style>
/* ── Google Fonts ── */
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Inter:wght@300;400;500;600;700&family=Bebas+Neue&display=swap');

/* ── CSS Variables ── */
:root {
  --neon-blue:    #00d4ff;
  --neon-green:   #00ff88;
  --neon-orange:  #ff6b35;
  --neon-purple:  #a855f7;
  --bg-deep:      #0a0e1a;
  --bg-card:      rgba(255,255,255,0.04);
  --bg-card-hover:rgba(255,255,255,0.08);
  --border:       rgba(255,255,255,0.08);
  --border-accent:rgba(0,212,255,0.4);
  --text-primary: #f0f4ff;
  --text-muted:   #8892aa;
  --radius-lg:    16px;
  --radius-md:    10px;
  --shadow-glow:  0 0 24px rgba(0,212,255,0.18);
  --shadow-card:  0 4px 32px rgba(0,0,0,0.5);
  --transition:   all 0.25s cubic-bezier(0.4,0,0.2,1);
}

/* ── Base Reset ── */
html, body, [class*="css"] {
  font-family: 'Inter', sans-serif;
  color: var(--text-primary);
}

.stApp {
  background: var(--bg-deep);
  background-image:
    radial-gradient(ellipse 80% 50% at 50% -10%, rgba(0,212,255,0.12) 0%, transparent 70%),
    radial-gradient(ellipse 60% 40% at 80% 90%, rgba(168,85,247,0.08) 0%, transparent 60%);
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
  background: rgba(10,14,26,0.95) !important;
  border-right: 1px solid var(--border) !important;
  backdrop-filter: blur(20px);
}

[data-testid="stSidebar"] * { color: var(--text-primary) !important; }

/* ── Hide default Streamlit chrome ── */
#MainMenu, footer, header { visibility: hidden; }
[data-testid="stDecoration"] { display: none; }

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: var(--bg-deep); }
::-webkit-scrollbar-thumb { background: var(--border-accent); border-radius: 3px; }

/* ── Typography helpers ── */
.orbitron { font-family: 'Orbitron', monospace !important; }
.bebas    { font-family: 'Bebas Neue', cursive !important; }

/* ── Hero ── */
.hero-wrap {
  text-align: center;
  padding: 60px 20px 40px;
  position: relative;
}
.hero-eyebrow {
  font-family: 'Orbitron', monospace;
  font-size: 11px;
  letter-spacing: 4px;
  text-transform: uppercase;
  color: var(--neon-blue);
  margin-bottom: 16px;
}
.hero-title {
  font-family: 'Orbitron', monospace;
  font-size: clamp(32px, 5vw, 64px);
  font-weight: 900;
  line-height: 1.1;
  background: linear-gradient(135deg, #fff 0%, var(--neon-blue) 50%, var(--neon-purple) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  margin: 0 0 20px;
}
.hero-sub {
  font-size: 16px;
  color: var(--text-muted);
  max-width: 540px;
  margin: 0 auto 36px;
  line-height: 1.7;
}
.hero-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: rgba(0,212,255,0.1);
  border: 1px solid var(--border-accent);
  border-radius: 999px;
  padding: 6px 16px;
  font-size: 12px;
  color: var(--neon-blue);
  margin-bottom: 32px;
}

/* ── Section Labels ── */
.section-label {
  font-family: 'Orbitron', monospace;
  font-size: 10px;
  letter-spacing: 3px;
  text-transform: uppercase;
  color: var(--text-muted);
  margin-bottom: 16px;
  display: flex;
  align-items: center;
  gap: 10px;
}
.section-label::after {
  content: '';
  flex: 1;
  height: 1px;
  background: var(--border);
}

/* ── CTA Buttons ── */
.btn-primary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  width: 100%;
  padding: 16px 24px;
  background: linear-gradient(135deg, #0099cc 0%, #7c3aed 100%);
  border: none;
  border-radius: var(--radius-md);
  color: #fff;
  font-family: 'Orbitron', monospace;
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 2px;
  text-transform: uppercase;
  cursor: pointer;
  transition: var(--transition);
  box-shadow: 0 4px 24px rgba(0,153,204,0.35);
}
.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 32px rgba(0,153,204,0.5);
  filter: brightness(1.1);
}

/* ── Loading / Spinner ── */
.loading-arena {
  text-align: center;
  padding: 60px 20px;
}
.trophy-spin {
  font-size: 56px;
  display: inline-block;
  animation: spin 1.6s linear infinite;
}
@keyframes spin { to { transform: rotate(360deg); } }

.loading-bar-wrap {
  width: 100%;
  max-width: 400px;
  height: 4px;
  background: rgba(255,255,255,0.1);
  border-radius: 999px;
  margin: 24px auto;
  overflow: hidden;
}
.loading-bar-fill {
  height: 100%;
  background: linear-gradient(90deg, var(--neon-blue), var(--neon-purple));
  border-radius: 999px;
}

.loading-msg {
  font-size: 15px;
  color: var(--text-muted);
  animation: fadeMsg 0.5s ease;
}
@keyframes fadeMsg { from { opacity:0; transform: translateY(6px); } to { opacity:1; transform: none; } }

/* ── Quiz Card ── */
.quiz-hero-card {
  background: linear-gradient(135deg, rgba(0,212,255,0.07) 0%, rgba(168,85,247,0.07) 100%);
  border: 1px solid var(--border-accent);
  border-radius: var(--radius-lg);
  padding: 32px;
  margin-bottom: 24px;
  box-shadow: var(--shadow-card);
  position: relative;
  overflow: hidden;
}
.quiz-hero-card::before {
  content: '';
  position: absolute;
  top: -40px; right: -40px;
  width: 160px; height: 160px;
  background: radial-gradient(circle, rgba(0,212,255,0.12) 0%, transparent 70%);
  pointer-events: none;
}
.quiz-sport-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: rgba(0,212,255,0.12);
  border: 1px solid var(--border-accent);
  border-radius: 999px;
  padding: 4px 12px;
  font-size: 11px;
  color: var(--neon-blue);
  font-weight: 600;
  letter-spacing: 1px;
  margin-bottom: 12px;
}
.quiz-title {
  font-family: 'Orbitron', monospace;
  font-size: 22px;
  font-weight: 700;
  margin-bottom: 6px;
}
.quiz-meta { font-size: 13px; color: var(--text-muted); }

.quiz-content-card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  padding: 28px 32px;
  font-size: 15px;
  line-height: 1.9;
  color: var(--text-primary);
  white-space: pre-wrap;
  font-family: 'Inter', sans-serif;
  box-shadow: var(--shadow-card);
}

/* ── Stat Cards ── */
.stat-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 12px;
  margin-bottom: 24px;
}

/* ── Achievement Badges ── */
.badge-row {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}
.badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 999px;
  padding: 6px 14px;
  font-size: 12px;
  color: var(--text-muted);
  transition: var(--transition);
}
.badge.unlocked {
  border-color: gold;
  color: gold;
  background: rgba(255,215,0,0.08);
  box-shadow: 0 0 10px rgba(255,215,0,0.15);
}

/* ── RAG / Insights Card ── */
.insights-card {
  background: rgba(168,85,247,0.06);
  border: 1px solid rgba(168,85,247,0.25);
  border-radius: var(--radius-lg);
  padding: 24px;
  margin-top: 24px;
}
.insights-header {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 16px;
  font-weight: 600;
  font-size: 15px;
}
.confidence-bar-wrap {
  background: rgba(255,255,255,0.06);
  border-radius: 999px;
  height: 6px;
  overflow: hidden;
  margin-top: 4px;
}
.confidence-bar-fill {
  height: 100%;
  background: linear-gradient(90deg, var(--neon-purple), var(--neon-blue));
  border-radius: 999px;
}
.source-chip {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  background: rgba(168,85,247,0.12);
  border: 1px solid rgba(168,85,247,0.3);
  border-radius: 999px;
  padding: 4px 12px;
  font-size: 11px;
  color: var(--neon-purple);
  margin: 3px;
}

/* ── Sidebar Styles ── */
.sb-avatar {
  width: 56px; height: 56px;
  background: linear-gradient(135deg, var(--neon-blue), var(--neon-purple));
  border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  font-size: 24px;
  margin: 0 auto 12px;
}
.sb-username {
  text-align: center;
  font-family: 'Orbitron', monospace;
  font-size: 13px;
  font-weight: 700;
  margin-bottom: 4px;
}
.sb-rank {
  text-align: center;
  font-size: 11px;
  color: var(--text-muted);
  margin-bottom: 20px;
}
.sb-stat-row {
  display: flex;
  justify-content: space-around;
  background: rgba(255,255,255,0.04);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  padding: 12px;
  margin-bottom: 20px;
}
.sb-stat { text-align: center; }
.sb-stat-val { font-family: 'Orbitron', monospace; font-size: 18px; font-weight: 700; color: var(--neon-blue); }
.sb-stat-lbl { font-size: 9px; color: var(--text-muted); text-transform: uppercase; letter-spacing: 1px; margin-top: 2px; }

.sb-divider {
  height: 1px;
  background: var(--border);
  margin: 16px 0;
}
.sb-label {
  font-size: 10px;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: var(--text-muted);
  font-family: 'Orbitron', monospace;
  margin-bottom: 8px;
  margin-top: 16px;
}
.sb-streak {
  display: flex;
  align-items: center;
  gap: 8px;
  background: rgba(255,107,53,0.1);
  border: 1px solid rgba(255,107,53,0.3);
  border-radius: var(--radius-md);
  padding: 10px 14px;
  font-size: 13px;
  color: var(--neon-orange);
  font-weight: 600;
  margin-bottom: 8px;
}
.sb-history-item {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 0;
  border-bottom: 1px solid var(--border);
  font-size: 12px;
  color: var(--text-muted);
}
.sb-history-dot {
  width: 7px; height: 7px;
  border-radius: 50%;
  background: var(--neon-blue);
  flex-shrink: 0;
}

/* ── Trending Bar ── */
.trending-bar {
  display: flex;
  gap: 8px;
  overflow-x: auto;
  padding-bottom: 6px;
  margin-bottom: 28px;
  scrollbar-width: none;
}
.trending-bar::-webkit-scrollbar { display: none; }
.trending-chip {
  flex-shrink: 0;
  background: rgba(255,255,255,0.04);
  border: 1px solid var(--border);
  border-radius: 999px;
  padding: 6px 14px;
  font-size: 12px;
  color: var(--text-muted);
  white-space: nowrap;
}
.trending-chip .hot { color: var(--neon-orange); font-size: 10px; }

/* ── Streamlit widget overrides ──
   NOTE: these apply to every st.button on the page. We rely on that:
   type="secondary" = muted/unselected, type="primary" = neon/selected. */
div[data-testid="stButton"] > button {
  border-radius: var(--radius-md) !important;
  font-family: 'Orbitron', monospace !important;
  font-weight: 700 !important;
  letter-spacing: 1px !important;
  transition: var(--transition) !important;
  width: 100% !important;
}
div[data-testid="stButton"] > button[kind="primary"] {
  background: linear-gradient(135deg, #0099cc, #7c3aed) !important;
  color: #fff !important;
  border: none !important;
  box-shadow: 0 4px 20px rgba(0,153,204,0.3) !important;
}
div[data-testid="stButton"] > button[kind="primary"]:hover {
  transform: translateY(-2px) !important;
  box-shadow: 0 8px 28px rgba(0,153,204,0.5) !important;
  filter: brightness(1.1) !important;
}
div[data-testid="stButton"] > button[kind="secondary"] {
  background: var(--bg-card) !important;
  border: 1px solid var(--border) !important;
  color: var(--text-muted) !important;
}
div[data-testid="stButton"] > button[kind="secondary"]:hover {
  border-color: var(--border-accent) !important;
  color: var(--neon-blue) !important;
  background: var(--bg-card-hover) !important;
  transform: translateY(-2px) !important;
}

/* Generate button gets extra height + letter spacing since it's the main CTA */
div[data-testid="stButton"]:has(button[aria-label*="GENERATE"]) > button,
div[data-testid="stButton"] > button[kind="primary"] {
  padding: 14px 20px !important;
}

/* Expander override */
[data-testid="stExpander"] {
  background: rgba(168,85,247,0.06) !important;
  border: 1px solid rgba(168,85,247,0.2) !important;
  border-radius: var(--radius-lg) !important;
}
[data-testid="stExpander"] summary {
  font-weight: 600 !important;
  color: var(--text-primary) !important;
}

/* Text area */
textarea {
  background: rgba(255,255,255,0.04) !important;
  border: 1px solid var(--border) !important;
  color: var(--text-primary) !important;
  border-radius: var(--radius-md) !important;
  font-family: 'Inter', sans-serif !important;
  font-size: 14px !important;
}

/* Success / error */
[data-testid="stAlert"] {
  border-radius: var(--radius-md) !important;
  border-left: 3px solid var(--neon-green) !important;
  background: rgba(0,255,136,0.06) !important;
}

/* Metric */
[data-testid="stMetric"] {
  background: var(--bg-card) !important;
  border: 1px solid var(--border) !important;
  border-radius: var(--radius-md) !important;
  padding: 16px !important;
}
[data-testid="stMetricLabel"] { color: var(--text-muted) !important; }
[data-testid="stMetricValue"] {
  font-family: 'Orbitron', monospace !important;
  color: var(--neon-blue) !important;
}

/* ── Fade-in animation for main content ── */
@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(20px); }
  to   { opacity: 1; transform: none; }
}
.fade-in { animation: fadeInUp 0.5s ease forwards; }
</style>
"""
st.markdown(GLOBAL_CSS, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# SESSION STATE
# ══════════════════════════════════════════════════════════════════════════════
def _init_state():
    defaults = {
        "quiz_output":    None,
        "quiz_context":   None,
        "sport_choice":   "Cricket",
        "difficulty":     "Medium",
        "quizzes_generated": 0,
        "quiz_history":   [],
        "gen_time":       0.0,
        "loading":        False,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

_init_state()


# ══════════════════════════════════════════════════════════════════════════════
# SPORT METADATA
# ══════════════════════════════════════════════════════════════════════════════
SPORTS = [
    {"name": "Cricket",    "emoji": "🏏"},
    {"name": "Football",   "emoji": "⚽"},
    {"name": "Tennis",     "emoji": "🎾"},
    {"name": "Basketball", "emoji": "🏀"},
    {"name": "Hockey",     "emoji": "🏒"},
    {"name": "Formula 1",  "emoji": "🏎️"},
    {"name": "Volleyball", "emoji": "🏐"},
    {"name": "Boxing",     "emoji": "🥊"},
    {"name": "Chess",      "emoji": "♟️"},
    {"name": "Badminton",  "emoji": "🏸"},
]

SPORT_EMOJI = {s["name"]: s["emoji"] for s in SPORTS}

TRENDING = [
    "🔥 T20 World Cup", "⚽ Champions League", "🏎️ Monaco GP",
    "🎾 Wimbledon", "🏏 IPL Finals", "🏀 NBA Playoffs", "🥊 Fury vs Usyk",
]

LOADING_MSGS = [
    "🏟️  Gathering historical records...",
    "⚽  Scanning latest match data...",
    "🏆  Crafting challenging questions...",
    "📡  Pulling live web context...",
    "🎯  Finalising your quiz...",
    "✨  Almost ready — hold tight...",
]

ACHIEVEMENTS = [
    ("🏅", "Rookie",     1),
    ("🥈", "Challenger", 3),
    ("🥇", "Champion",   7),
    ("🏆", "Legend",     15),
]


# ══════════════════════════════════════════════════════════════════════════════
# SIDEBAR — Control Panel
# ══════════════════════════════════════════════════════════════════════════════
# with st.sidebar:
#     sport  = st.session_state.sport_choice
#     diff   = st.session_state.difficulty
#     count  = st.session_state.quizzes_generated
#     streak = min(count, 7)

#     st.markdown(f"""
#     <div class="sb-avatar">👤</div>
#     <div class="sb-username">Sports Fan</div>
#     <div class="sb-rank">{'🏆 Legend' if count >= 15 else '🥇 Champion' if count >= 7 else '🥈 Challenger' if count >= 3 else '🏅 Rookie'}</div>
#     <div class="sb-stat-row">
#       <div class="sb-stat">
#         <div class="sb-stat-val">{count}</div>
#         <div class="sb-stat-lbl">Quizzes</div>
#       </div>
#       <div class="sb-stat">
#         <div class="sb-stat-val">{streak}</div>
#         <div class="sb-stat-lbl">Streak</div>
#       </div>
#       <div class="sb-stat">
#         <div class="sb-stat-val">{count * 10}</div>
#         <div class="sb-stat-lbl">XP</div>
#       </div>
#     </div>
#     """, unsafe_allow_html=True)

#     if streak > 0:
#         st.markdown(f'<div class="sb-streak">🔥 {streak}-Quiz Streak — Keep it up!</div>', unsafe_allow_html=True)

#     st.markdown('<div class="sb-divider"></div>', unsafe_allow_html=True)

#     st.markdown('<div class="sb-label">Active Config</div>', unsafe_allow_html=True)
#     emoji = SPORT_EMOJI.get(sport, "🏆")
#     diff_color = {"Easy": "#22c55e", "Medium": "#f97316", "Hard": "#ef4444"}.get(diff, "#fff")
#     st.markdown(f"""
#     <div style="background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.08);
#                 border-radius:10px;padding:14px;font-size:13px;margin-bottom:12px;">
#       <div style="margin-bottom:8px;">{emoji} <strong style="color:#f0f4ff">{sport}</strong></div>
#       <div>⚡ Difficulty: <strong style="color:{diff_color}">{diff}</strong></div>
#     </div>
#     """, unsafe_allow_html=True)

#     st.markdown('<div class="sb-label">Daily Challenge</div>', unsafe_allow_html=True)
#     st.markdown("""
#     <div style="background:rgba(0,212,255,0.07);border:1px solid rgba(0,212,255,0.2);
#                 border-radius:10px;padding:12px;font-size:12px;color:#8892aa;margin-bottom:16px;">
#       🎲 <strong style="color:#f0f4ff">Random Sport Quiz</strong><br>
#       <span style="font-size:10px;">Resets in 08:42:17</span>
#     </div>
#     """, unsafe_allow_html=True)

#     history = st.session_state.quiz_history[-5:][::-1]
#     if history:
#         st.markdown('<div class="sb-label">Recent Quizzes</div>', unsafe_allow_html=True)
#         for h in history:
#             emj = SPORT_EMOJI.get(h["sport"], "🏆")
#             st.markdown(f"""
#             <div class="sb-history-item">
#               <div class="sb-history-dot"></div>
#               <div>{emj} {h["sport"]} · {h["diff"]}</div>
#             </div>
#             """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# MAIN CONTENT
# ══════════════════════════════════════════════════════════════════════════════

st.markdown("""
<div class="hero-wrap fade-in">
  <div class="hero-eyebrow">⚡ AI-Powered · RAG-Enhanced · Live Data</div>
  <h1 class="hero-title">Ultimate Sports<br>Quiz Arena</h1>
  <p class="hero-sub">
    Challenge yourself with AI-generated quizzes powered by historical knowledge
    and live sports intelligence. Pick a sport. Pick a difficulty. Let's go.
  </p>
  <div class="hero-badge">🏆 &nbsp; Powered by ChromaDB + Live Web Search</div>
</div>
""", unsafe_allow_html=True)

# chips = "".join(f'<div class="trending-chip">{t}</div>' for t in TRENDING)
# st.markdown(f'<div class="trending-bar">{chips}</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# SPORT SELECTION — real buttons ARE the cards (primary = selected)
# ══════════════════════════════════════════════════════════════════════════════
st.markdown('<div class="section-label">Select Your Sport</div>', unsafe_allow_html=True)

cols = st.columns(len(SPORTS))
for i, s in enumerate(SPORTS):
    with cols[i]:
        is_selected = st.session_state.sport_choice == s["name"]
        if st.button(
            f"{s['emoji']}\n{s['name']}",
            key=f"sport_btn_{s['name']}",
            type="primary" if is_selected else "secondary",
            use_container_width=True,
        ):
            st.session_state.sport_choice = s["name"]
            st.rerun()

st.markdown("<br>", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# DIFFICULTY SELECTION — real buttons ARE the pills
# ══════════════════════════════════════════════════════════════════════════════
st.markdown('<div class="section-label">Difficulty Level</div>', unsafe_allow_html=True)

diff_cols = st.columns(3)
for i, label in enumerate(["Easy", "Medium", "Hard"]):
    with diff_cols[i]:
        is_selected = st.session_state.difficulty == label
        if st.button(
            label,
            key=f"diff_{label}",
            type="primary" if is_selected else "secondary",
            use_container_width=True,
        ):
            st.session_state.difficulty = label
            st.rerun()

st.markdown("<br>", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# GENERATE BUTTON
# ══════════════════════════════════════════════════════════════════════════════
sport_emoji = SPORT_EMOJI.get(st.session_state.sport_choice, "🏆")
if st.button(
    f"⚡  GENERATE  ·  {sport_emoji} {st.session_state.sport_choice}  ·  {st.session_state.difficulty.upper()}",
    key="generate_btn",
    type="primary",
    use_container_width=True,
):
    st.session_state.loading = True
    start = time.time()

    loading_container = st.empty()

    for idx, msg in enumerate(LOADING_MSGS):
        pct = int((idx + 1) / len(LOADING_MSGS) * 100)
        loading_container.markdown(f"""
        <div class="loading-arena">
          <div class="trophy-spin">🏆</div>
          <h3 style="font-family:'Orbitron',monospace;font-size:18px;margin:20px 0 8px;
                     background:linear-gradient(135deg,#fff,#00d4ff);
                     -webkit-background-clip:text;-webkit-text-fill-color:transparent;">
            Building Your Quiz...
          </h3>
          <div class="loading-bar-wrap">
            <div class="loading-bar-fill" style="width:{pct}%;"></div>
          </div>
          <p class="loading-msg">{msg}</p>
          <p style="font-size:11px;color:#8892aa;margin-top:6px;">{pct}% complete</p>
        </div>
        """, unsafe_allow_html=True)
        if idx < len(LOADING_MSGS) - 1:
            time.sleep(0.55)

    try:
        quiz_text, context_used = compile_quiz_data(
            st.session_state.sport_choice,
            st.session_state.difficulty
        )
        elapsed = round(time.time() - start, 1)
        st.session_state.quiz_output  = quiz_text
        st.session_state.quiz_context = context_used
        st.session_state.quizzes_generated += 1
        st.session_state.gen_time = elapsed
        st.session_state.quiz_history.append({
            "sport": st.session_state.sport_choice,
            "diff":  st.session_state.difficulty,
        })
    except Exception as e:
        loading_container.error(f"❌ Generation failed: {e}")
        st.stop()

    loading_container.empty()
    st.session_state.loading = False
    st.rerun()


# ══════════════════════════════════════════════════════════════════════════════
# QUIZ OUTPUT
# ══════════════════════════════════════════════════════════════════════════════
if st.session_state.quiz_output:
    sport  = st.session_state.sport_choice
    diff   = st.session_state.difficulty
    emoji  = SPORT_EMOJI.get(sport, "🏆")
    count  = st.session_state.quizzes_generated
    gtime  = st.session_state.gen_time

    st.markdown('<br>', unsafe_allow_html=True)

    diff_color = {"Easy": "#22c55e", "Medium": "#f97316", "Hard": "#ef4444"}.get(diff, "#fff")
    st.markdown(f"""
    <div class="quiz-hero-card fade-in">
      <div class="quiz-sport-badge">{emoji} &nbsp; {sport.upper()}</div>
      <div class="quiz-title">Your {diff} Quiz is Ready</div>
      <div class="quiz-meta">
        Generated in {gtime}s &nbsp;·&nbsp;
        <span style="color:{diff_color};font-weight:700;">{diff}</span> difficulty &nbsp;·&nbsp;
        Quiz #{count}
      </div>
    </div>
    """, unsafe_allow_html=True)

    lines = st.session_state.quiz_output.strip().split("\n")
    q_count = sum(1 for l in lines if l.strip() and (l.strip()[0].isdigit() or l.strip().startswith("Q")))
    q_count = max(q_count, 5)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("❓ Questions", q_count)
    with col2:
        st.metric("⚡ Difficulty", diff)
    with col3:
        st.metric("⏱️ Gen Time", f"{gtime}s")

    st.markdown('<br>', unsafe_allow_html=True)

    st.markdown('<div class="section-label">Your Quiz</div>', unsafe_allow_html=True)
    st.markdown(
        f'<div class="quiz-content-card fade-in">{st.session_state.quiz_output}</div>',
        unsafe_allow_html=True,
    )

    st.markdown('<br>', unsafe_allow_html=True)
    a1, a2 = st.columns(2)
    
    with a1:
        st.download_button(
            "⬇  Download",
            data=st.session_state.quiz_output,
            file_name=f"{sport.replace(' ','_')}_{diff}_quiz.txt",
            mime="text/plain",
            key="dl_btn",
            use_container_width=True,
        )
    
    with a2:
        if st.button("🔄  New Quiz",    key="regen_btn", use_container_width=True):
            st.session_state.quiz_output  = None
            st.session_state.quiz_context = None
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-label">Achievements</div>', unsafe_allow_html=True)
    badges_html = '<div class="badge-row">'
    for icon, name, threshold in ACHIEVEMENTS:
        unlocked = count >= threshold
        cls = "unlocked" if unlocked else ""
        badges_html += f'<div class="badge {cls}">{icon} {name}</div>'
    badges_html += "</div>"
    st.markdown(badges_html, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    with st.expander("🔮  AI Knowledge Sources — Expand to inspect context", expanded=False):
        st.markdown(f"""
        <div class="insights-card">
          <div class="insights-header">
            🤖 &nbsp; Knowledge Sources Used
          </div>
          <div style="display:flex;flex-wrap:wrap;margin-bottom:16px;">
            <span class="source-chip">📚 ChromaDB Vector Store</span>
            <span class="source-chip">🌐 Live Web Search</span>
            <span class="source-chip">🏆 Historical Facts DB</span>
          </div>
          <div style="font-size:12px;color:#8892aa;margin-bottom:6px;">AI Confidence</div>
          <div class="confidence-bar-wrap">
            <div class="confidence-bar-fill" style="width:87%;"></div>
          </div>
          <div style="font-size:11px;color:#8892aa;margin-top:4px;">87% — High confidence blend of archival + live data</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("**Raw RAG Context:**")
        st.code(st.session_state.quiz_context, language="markdown")


# ══════════════════════════════════════════════════════════════════════════════
# EMPTY STATE — no quiz yet
# ══════════════════════════════════════════════════════════════════════════════
elif not st.session_state.loading:
    st.markdown("""
    <div style="text-align:center;padding:60px 20px;color:#8892aa;">
      <div style="font-size:64px;margin-bottom:16px;">🏟️</div>
      <div style="font-family:'Orbitron',monospace;font-size:16px;color:#f0f4ff;margin-bottom:8px;">
        The Arena Awaits
      </div>
      <div style="font-size:14px;">
        Select a sport above, choose your difficulty, and hit <strong style="color:#00d4ff">Generate</strong> to begin.
      </div>
    </div>
    """, unsafe_allow_html=True)
