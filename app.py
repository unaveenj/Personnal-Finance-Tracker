import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Naveen's Finance",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── DESIGN SYSTEM ─────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500;9..40,600;9..40,700&display=swap');

:root {
  --primary:  #004D40;
  --accent:   #00BFA5;
  --bg:       #F2F6F5;
  --card:     #FFFFFF;
  --sidebar:  #00352C;
  --text:     #1C3A35;
  --muted:    #7A9E98;
  --border:   #DDE9E7;
  --green:    #1B5E20;
  --red:      #B71C1C;
  --amber:    #E65100;
  --blue:     #0D47A1;
  --grid:     #EFF4F3;
}

html, body, [class*="css"] {
  font-family: 'DM Sans', sans-serif !important;
  color: var(--text);
}

.main, .stApp { background: var(--bg) !important; }
.block-container { padding: 2.2rem 2.8rem 4rem !important; max-width: 1400px; }

/* ── Sidebar ── */
[data-testid="stSidebar"] {
  background: var(--sidebar) !important;
  border-right: none !important;
}
[data-testid="stSidebar"] * { color: #CDEAE7 !important; }
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 { color: #FFFFFF !important; }
[data-testid="stSidebar"] .stSelectbox label,
[data-testid="stSidebar"] .stRadio > label {
  color: #8ABFBA !important;
  font-size: 10px !important;
  letter-spacing: 1.5px !important;
  text-transform: uppercase !important;
  font-weight: 600 !important;
}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label {
  color: #CDEAE7 !important;
  font-size: 14px !important;
  font-weight: 500 !important;
  letter-spacing: 0 !important;
  text-transform: none !important;
  padding: 6px 0 !important;
}
[data-testid="stSidebar"] hr {
  border-color: rgba(255,255,255,0.12) !important;
  margin: 12px 0 !important;
}
[data-testid="stSidebar"] .stButton > button {
  background: #00695C !important;
  color: #FFFFFF !important;
  border: 1px solid #00897B !important;
  border-radius: 8px !important;
  width: 100% !important;
  font-size: 13px !important;
  font-weight: 600 !important;
  padding: 8px 12px !important;
}
[data-testid="stSidebar"] .stButton > button:hover {
  background: #00897B !important;
  border-color: #00BFA5 !important;
}

/* ── Metric cards ── */
[data-testid="metric-container"] {
  background: var(--card) !important;
  border-radius: 14px !important;
  padding: 20px 22px !important;
  border: 1px solid var(--border) !important;
  box-shadow: 0 2px 12px rgba(0,77,64,0.07) !important;
}
[data-testid="metric-container"] > label {
  font-size: 10px !important;
  font-weight: 700 !important;
  letter-spacing: 1.8px !important;
  text-transform: uppercase !important;
  color: var(--muted) !important;
}
[data-testid="stMetricValue"] > div {
  font-family: 'DM Serif Display', serif !important;
  font-size: 26px !important;
  color: var(--text) !important;
  font-weight: 400 !important;
}
[data-testid="stMetricDelta"] { font-size: 12px !important; }

/* ── Page header ── */
.page-title {
  font-family: 'DM Serif Display', serif;
  font-size: 34px; color: var(--primary);
  font-weight: 400; margin: 0 0 2px 0; line-height: 1.15;
}
.page-subtitle {
  font-size: 13px; color: var(--muted);
  margin-bottom: 28px; font-weight: 400;
}

/* ── Section title ── */
.section-title {
  font-family: 'DM Serif Display', serif;
  font-size: 18px; color: var(--primary);
  margin: 28px 0 14px 0;
  display: flex; align-items: center; gap: 8px;
}
.section-title::after {
  content: ''; flex: 1; height: 1px;
  background: var(--border); margin-left: 8px;
}

/* ── Insight / recommendation cards ── */
.insight-card {
  background: var(--card); border-radius: 14px;
  padding: 20px 24px; border-left: 3px solid var(--accent);
  box-shadow: 0 2px 10px rgba(0,77,64,0.06); margin-bottom: 12px;
}
.insight-title { font-size: 15px; font-weight: 600; color: var(--text); }
.insight-body  { font-size: 13px; color: #556B67; line-height: 1.75; margin-top: 6px; }
.insight-save  { font-size: 13px; font-weight: 600; color: var(--green); margin-top: 10px; }

/* ── Month comparison movers ── */
.mover-up   { color: #B71C1C; font-weight: 700; }
.mover-down { color: #1B5E20; font-weight: 700; }

/* ── Badges ── */
.badge {
  display: inline-block; padding: 3px 10px;
  border-radius: 100px; font-size: 10px;
  font-weight: 700; letter-spacing: 0.5px;
}
.badge-high { background: #FEE2E2; color: #991B1B; }
.badge-med  { background: #FEF3C7; color: #92400E; }
.badge-info { background: #DBEAFE; color: #1E3A8A; }
.badge-good { background: #DCFCE7; color: #166534; }

/* ── Subscription pills ── */
.pill { padding: 3px 12px; border-radius: 100px; font-size: 11px; font-weight: 600; }
.pill-cut  { background: #FEE2E2; color: #991B1B; }
.pill-keep { background: #DCFCE7; color: #166534; }
.pill-rev  { background: #FEF3C7; color: #92400E; }

/* ── Table ── */
[data-testid="stDataFrame"] { border-radius: 12px !important; overflow: hidden; }
[data-testid="stDataFrame"] th { background: var(--bg) !important; }

/* ── Streamlit overrides ── */
#MainMenu { visibility: hidden; }
footer    { visibility: hidden; }
header    { visibility: hidden; }
</style>
""", unsafe_allow_html=True)


# ── GOOGLE SHEETS DATA ────────────────────────────────────────────────────────
_SHEET_ID  = "1MNP2rXuL21JHFUof8GduNucAxCDcBazH"
_GID       = "379184043"
GSHEET_URL = (
    f"https://docs.google.com/spreadsheets/d/{_SHEET_ID}"
    f"/export?format=csv&gid={_GID}"
)

@st.cache_data(ttl=300)
def load_data():
    try:
        df = pd.read_csv(GSHEET_URL)
    except Exception as e:
        st.error(
            "**Cannot load Google Sheet.**\n\n"
            "Open your sheet → Share → General Access → "
            "**Anyone with the link → Viewer**, then click Refresh.\n\n"
            f"`{e}`"
        )
        st.stop()
    df.columns           = df.columns.str.strip()
    st.write("DEBUG columns:", df.columns.tolist())
    df["Date"]           = pd.to_datetime(df["Date"], errors="coerce")
    df["Amount"]         = pd.to_numeric(
        df["Amount"].astype(str).str.replace("S$", "", regex=False).str.replace(",", ""),
        errors="coerce"
    ).fillna(0).round(2)
    df["Month"]          = df["Date"].dt.strftime("%b %Y")
    df["Week"]           = df["Date"].dt.to_period("W").apply(lambda p: p.start_time)
    df["Category"]       = df["Category"].fillna("Misc")
    df["Payment Method"] = df.get("Payment Method", pd.Series(dtype=str)).fillna("—")
    df["Notes"]          = df.get("Notes", pd.Series(dtype=str)).fillna("")
    df["Description"]    = df.get("Description", pd.Series(dtype=str)).fillna("")
    return df

df_all  = load_data()
exp_all = df_all[df_all["Type"] == "Expense"]
inc_all = df_all[df_all["Type"] == "Income"]
MONTHS  = sorted(df_all["Month"].unique().tolist(),
                 key=lambda m: pd.to_datetime(m, format="%b %Y"))
N_MONTHS = max(len(MONTHS), 1)

# ── CHART DEFAULTS ────────────────────────────────────────────────────────────
PALETTE = ["#004D40","#00695C","#00897B","#26A69A","#4DB6AC",
           "#80CBC4","#0D47A1","#1565C0","#E65100","#F57C00","#B71C1C"]

def base_layout(**extra):
    return dict(
        plot_bgcolor="white", paper_bgcolor="white",
        font=dict(family="DM Sans", color="#1C3A35"),
        margin=dict(l=0, r=0, t=24, b=0),
        **extra
    )

def styled_yaxis(prefix="S$"):
    return dict(gridcolor="#EFF4F3", zeroline=False,
                tickprefix=prefix, tickfont_size=11)

def styled_xaxis():
    return dict(gridcolor="#EFF4F3", tickfont_size=11)


# ── HELPERS ───────────────────────────────────────────────────────────────────
def prev_month_stats(month_str):
    """Return (prev_inc, prev_exp, prev_label) or (None, None, None)."""
    if month_str not in MONTHS:
        return None, None, None
    idx = MONTHS.index(month_str)
    if idx == 0:
        return None, None, None
    prev = MONTHS[idx - 1]
    p    = df_all[df_all["Month"] == prev]
    return (
        p[p["Type"] == "Income"]["Amount"].sum(),
        p[p["Type"] == "Expense"]["Amount"].sum(),
        prev,
    )

def prog_bar(pct, color="#004D40"):
    fill = min(pct, 100)
    return (
        f"<div style='background:#EFF4F3;border-radius:6px;height:9px;overflow:hidden'>"
        f"<div style='width:{fill:.0f}%;height:100%;background:{color};border-radius:6px'></div>"
        f"</div>"
    )

def small_label(text):
    return f"<small style='color:#7A9E98;font-weight:600;letter-spacing:1px'>{text.upper()}</small>"

def forecast_card(label, monthly_saving, avg_inc, note, color):
    rate = monthly_saving / avg_inc * 100 if avg_inc > 0 else 0
    return f"""
    <div style='background:white;border-radius:14px;padding:24px 20px;
                border:1px solid #DDE9E7;box-shadow:0 2px 12px rgba(0,77,64,0.07);text-align:center'>
      <div style='font-size:10px;font-weight:700;letter-spacing:1.5px;
                  text-transform:uppercase;color:#7A9E98;margin-bottom:10px'>{label}</div>
      <div style='font-family:DM Serif Display,serif;font-size:30px;color:{color}'>
        S${monthly_saving:,.0f}
      </div>
      <div style='font-size:12px;color:#7A9E98;margin-top:2px'>/month · {rate:.1f}% savings rate</div>
      <div style='margin-top:16px;padding-top:14px;border-top:1px solid #EFF4F3;
                  display:flex;justify-content:space-around'>
        <div>
          <div style='font-size:10px;color:#7A9E98;letter-spacing:0.5px'>6 MONTHS</div>
          <div style='font-size:16px;font-weight:600;color:{color}'>S${monthly_saving*6:,.0f}</div>
        </div>
        <div>
          <div style='font-size:10px;color:#7A9E98;letter-spacing:0.5px'>12 MONTHS</div>
          <div style='font-size:16px;font-weight:600;color:{color}'>S${monthly_saving*12:,.0f}</div>
        </div>
      </div>
      <div style='margin-top:12px;font-size:11px;color:#9ABFBA;font-style:italic;line-height:1.5'>{note}</div>
    </div>"""

def rec_card(priority, title, body, action, impact_annual):
    badge_bg  = {"high":"#FEE2E2","med":"#FEF3C7","info":"#DBEAFE","good":"#DCFCE7"}
    badge_col = {"high":"#991B1B","med":"#92400E","info":"#1E3A8A","good":"#166534"}
    label_map = {"high":"HIGH IMPACT","med":"MEDIUM","info":"INFO","good":"GOOD NEWS"}
    bg  = badge_bg.get(priority, "#F3F4F6")
    col = badge_col.get(priority, "#374151")
    lbl = label_map.get(priority, priority.upper())
    impact_html = (
        f"<div style='margin-top:10px;font-size:12px;font-weight:600;color:#1B5E20'>"
        f"💰 Annual impact: S${impact_annual:,.0f}</div>"
        if impact_annual > 0 else ""
    )
    return f"""
    <div style='background:white;border-radius:14px;padding:18px 22px;
                border-left:3px solid {col};
                box-shadow:0 2px 10px rgba(0,77,64,0.06);margin-bottom:12px'>
      <div style='display:flex;align-items:center;gap:10px;margin-bottom:6px'>
        <span style='background:{bg};color:{col};padding:2px 10px;border-radius:100px;
                     font-size:10px;font-weight:700;letter-spacing:0.5px'>{lbl}</span>
        <span style='font-size:15px;font-weight:600;color:#1C3A35'>{title}</span>
      </div>
      <div style='font-size:13px;color:#556B67;line-height:1.75'>{body}</div>
      <div style='margin-top:8px;font-size:12px;font-weight:600;color:#004D40'>
        → {action}
      </div>
      {impact_html}
    </div>"""


def smart_recommendations(exp_df, inc_df, selected_month, top_n=None):
    """
    Analyse actual spending data and return prioritised, actionable recommendations.
    Works for both a specific month view and All Time.
    """
    recs = []
    avg_inc_mo = inc_all["Amount"].sum() / N_MONTHS
    avg_exp_mo = exp_all["Amount"].sum() / N_MONTHS
    all_rate   = (avg_inc_mo - avg_exp_mo) / avg_inc_mo * 100 if avg_inc_mo > 0 else 0
    cat_avg    = (exp_all.groupby("Category")["Amount"].sum() / N_MONTHS).to_dict()

    # ── 1. Categories over-budget vs historical average (month view only) ──
    if selected_month != "All Time":
        cat_curr = exp_df.groupby("Category")["Amount"].sum().to_dict()
        for cat, curr in sorted(cat_curr.items(), key=lambda x: -x[1]):
            avg = cat_avg.get(cat, 0)
            if avg > 0 and curr > avg * 1.25 and curr - avg > 40:
                over     = curr - avg
                pct_over = (curr / avg - 1) * 100
                recs.append(dict(
                    priority="high" if over > 150 else "med",
                    title=f"{cat} is {pct_over:.0f}% above your average",
                    body=(
                        f"You spent <b>S${curr:,.0f}</b> on {cat} in {selected_month}, "
                        f"vs your monthly average of S${avg:,.0f}. "
                        f"That's S${over:,.0f} extra. "
                        f"{'Consider whether this is a one-off — if recurring, it will drag your savings rate down.' if pct_over > 50 else 'Worth keeping an eye on.'}"
                    ),
                    action=f"Review {cat} transactions for {selected_month}",
                    impact=over * 12,
                ))

    # ── 2. Consistently rising category (3-month trend) ──
    if len(MONTHS) >= 3:
        recent = MONTHS[-3:]
        for cat in exp_all["Category"].unique():
            vals = [
                exp_all[(exp_all["Month"]==m) & (exp_all["Category"]==cat)]["Amount"].sum()
                for m in recent
            ]
            if all(vals[i] < vals[i+1] for i in range(len(vals)-1)) and vals[-1] > 30:
                rise = vals[-1] - vals[0]
                recs.append(dict(
                    priority="med",
                    title=f"{cat} has been rising 3 months in a row",
                    body=(
                        f"{cat} spending: S${vals[0]:,.0f} → S${vals[1]:,.0f} → S${vals[2]:,.0f}. "
                        f"That's a S${rise:,.0f} increase over 3 months. "
                        f"Identify what changed — new habit, price increase, or scope creep?"
                    ),
                    action=f"Set a monthly ceiling for {cat} spending",
                    impact=rise * 12,
                ))

    # ── 3. Redundant subscriptions ──
    sub_cuts_list = [
        ("AVG Antivirus", 82.62, "Windows Defender is ranked #1 — you're paying for nothing"),
        ("ChatGPT",       28.59, "You already have Claude — cancel the duplicate"),
        ("Spotify",       17.46, "YouTube Premium already includes YouTube Music"),
    ]
    sub_total = sum(a for _, a, _ in sub_cuts_list)
    detail    = "; ".join(f"{n} (S${a:.0f})" for n, a, _ in sub_cuts_list)
    recs.append(dict(
        priority="high",
        title="Cancel 3 redundant subscriptions — zero lifestyle change",
        body=(
            f"{detail}. "
            f"These three overlap with tools you already have (Claude, YouTube Premium, Windows Defender). "
            f"Cancelling takes 10 minutes."
        ),
        action=f"Cancel today → save S${sub_total:.0f}/month",
        impact=sub_total * 12,
    ))

    # ── 4. Investment gap ──
    idle_monthly = avg_inc_mo * (all_rate / 100)
    if idle_monthly > 500:
        recs.append(dict(
            priority="high",
            title="Your savings aren't working hard enough",
            body=(
                f"With a {all_rate:.0f}% savings rate, you're generating ~S${idle_monthly:,.0f}/month of surplus. "
                f"Sitting in a current account earns ~0.05%. "
                f"Investing S${idle_monthly:,.0f}/month at 7% p.a. (VWRA) compounds to "
                f"<b>S${idle_monthly * 12 * 10 * 1.07**5:,.0f}</b> in 10 years."
            ),
            action="Set up monthly DCA on Endowus or Syfe — takes 15 minutes",
            impact=0,
        ))

    # ── 5. Food spend vs SG benchmark ──
    food_mo = exp_all[exp_all["Category"]=="Food"]["Amount"].sum() / N_MONTHS
    if food_mo > 500:
        saving = food_mo - 400
        recs.append(dict(
            priority="med",
            title=f"Food spend is S${food_mo:,.0f}/month — above SG median",
            body=(
                f"SG median dining spend for a single person is S$300–500/month. "
                f"You're at S${food_mo:,.0f}. Swapping 3 restaurant meals/week for hawker centre "
                f"saves roughly S$15–25 per meal. "
                f"Even cutting S${saving:.0f}/month adds S${saving*12:,.0f} to your annual savings."
            ),
            action="Try hawker centre 3× per week instead of restaurants",
            impact=saving * 12,
        ))

    # ── 6. Emergency fund check ──
    core_monthly = avg_exp_mo
    recs.append(dict(
        priority="info",
        title="Verify your emergency fund is fully funded",
        body=(
            f"Your core monthly expenses average S${core_monthly:,.0f}. "
            f"A 6-month buffer = <b>S${core_monthly*6:,.0f}</b>. "
            f"Park it in CIMB FastSaver (~3% p.a.) or SingLife Account (~3.5% p.a.) — "
            f"not in a current account. It earns while it waits."
        ),
        action=f"Target: S${core_monthly*6:,.0f} in a high-yield savings account",
        impact=0,
    ))

    # Sort: high first, then by annual impact descending
    order = {"high": 0, "med": 1, "info": 2, "good": 3}
    recs.sort(key=lambda r: (order.get(r["priority"], 9), -r.get("impact", 0)))

    return recs[:top_n] if top_n else recs


# ── SIDEBAR ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 💰 Finance")
    st.markdown(
        "<p style='color:#8ABFBA;font-size:11px;letter-spacing:1.5px;"
        "text-transform:uppercase;margin-top:-8px'>Naveen · Singapore</p>",
        unsafe_allow_html=True
    )
    st.markdown("---")

    selected_month = st.selectbox("Period", ["All Time"] + MONTHS, index=0)

    st.markdown("---")

    page = st.radio("Navigate", [
        "📊  Dashboard",
        "📈  Spending Analysis",
        "💡  Insights",
        "💳  Transactions",
        "🏦  Net Worth",
    ], label_visibility="collapsed")

    st.markdown("---")

    st.markdown(
        "<p style='color:#8ABFBA;font-size:10px;letter-spacing:1px;"
        "text-transform:uppercase;margin-bottom:4px'>Data</p>",
        unsafe_allow_html=True
    )
    if st.button("🔄 Refresh Data", type="primary", use_container_width=True):
        load_data.clear()
        st.rerun()

    st.markdown("---")

    min_d = df_all["Date"].min().strftime("%d %b %Y")
    max_d = df_all["Date"].max().strftime("%d %b %Y")
    st.markdown(
        f"<p style='color:#8ABFBA;font-size:11px;line-height:1.8'>"
        f"📅 {min_d} → {max_d}<br>"
        f"🧾 {len(df_all)} transactions<br>"
        f"🔁 Auto-refresh every 5 min</p>",
        unsafe_allow_html=True
    )


# ── FILTERED DATA ─────────────────────────────────────────────────────────────
if selected_month == "All Time":
    df = df_all.copy()
else:
    df = df_all[df_all["Month"] == selected_month].copy()

exp = df[df["Type"] == "Expense"]
inc = df[df["Type"] == "Income"]

total_inc = inc["Amount"].sum()
total_exp = exp["Amount"].sum()
net       = total_inc - total_exp
sav_rate  = net / total_inc * 100 if total_inc > 0 else 0
n_days    = max((df["Date"].max() - df["Date"].min()).days + 1, 1)
avg_daily = total_exp / n_days


# ══════════════════════════════════════════════════════════════════════════════
# PAGE: DASHBOARD
# ══════════════════════════════════════════════════════════════════════════════
if page == "📊  Dashboard":
    st.markdown('<div class="page-title">Dashboard</div>', unsafe_allow_html=True)

    # ── Month pills (in-page filter) ─────────────────────────────────────────
    dash_month = st.pills(
        "Filter by month",
        ["All Time"] + MONTHS,
        default=selected_month,
        key="dash_month",
        label_visibility="collapsed",
    ) or "All Time"

    st.markdown(
        f"<div style='font-size:13px;color:#7A9E98;margin:-6px 0 20px'>",
        unsafe_allow_html=True
    )

    # Recompute filtered data for the dashboard using pill selection
    if dash_month == "All Time":
        df  = df_all.copy()
    else:
        df  = df_all[df_all["Month"] == dash_month].copy()
    exp = df[df["Type"] == "Expense"]
    inc = df[df["Type"] == "Income"]
    total_inc = inc["Amount"].sum()
    total_exp = exp["Amount"].sum()
    net       = total_inc - total_exp
    sav_rate  = net / total_inc * 100 if total_inc > 0 else 0
    n_days    = max((df["Date"].max() - df["Date"].min()).days + 1, 1)
    avg_daily = total_exp / n_days

    # All-time average savings per month (fixed reference, unaffected by filter)
    avg_savings_mo = (inc_all["Amount"].sum() - exp_all["Amount"].sum()) / N_MONTHS

    # ── KPI row with prev-month deltas ──────────────────────────────────────
    p_inc, p_exp, p_label = prev_month_stats(dash_month)
    p_net  = (p_inc - p_exp) if p_inc is not None else None
    p_rate = ((p_inc - p_exp) / p_inc * 100) if p_inc else None

    k1, k2, k3, k4, k5, k6 = st.columns(6)

    if dash_month != "All Time" and p_inc is not None:
        k1.metric("Total Income",       f"S${total_inc:,.0f}",
                  f"S${total_inc - p_inc:+,.0f} vs {p_label}")
        k2.metric("Total Expenses",     f"S${total_exp:,.0f}",
                  f"S${total_exp - p_exp:+,.0f} vs {p_label}",
                  delta_color="inverse")
        k3.metric("Net Savings",        f"S${net:,.0f}",
                  f"S${net - p_net:+,.0f} vs {p_label}")
        k4.metric("Savings Rate",       f"{sav_rate:.1f}%",
                  f"{sav_rate - p_rate:+.1f}pp vs {p_label}")
        k5.metric("Avg Daily Spend",    f"S${avg_daily:.0f}",
                  f"Over {n_days} days", delta_color="off")
        k6.metric("Avg Savings / Month", f"S${avg_savings_mo:,.0f}",
                  "All-time average", delta_color="off")
    else:
        k1.metric("Total Income",       f"S${total_inc:,.0f}", f"{len(inc)} transactions")
        k2.metric("Total Expenses",     f"S${total_exp:,.0f}", f"{len(exp)} transactions")
        k3.metric("Net Savings",        f"S${net:,.0f}",        "Income − Expenses")
        k4.metric("Savings Rate",       f"{sav_rate:.1f}%",     "Target > 20%")
        k5.metric("Avg Daily Spend",    f"S${avg_daily:.0f}",   f"Over {n_days} days")
        k6.metric("Avg Savings / Month", f"S${avg_savings_mo:,.0f}", "All-time average")

    st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)

    # ── Row 2: Monthly bar + Category donut ──────────────────────────────────
    col_l, col_r = st.columns([1.35, 1])

    with col_l:
        st.markdown('<div class="section-title">Monthly Income vs Expenses</div>', unsafe_allow_html=True)
        monthly = df_all.groupby(["Month", "Type"])["Amount"].sum().reset_index()
        monthly["_s"] = pd.to_datetime(monthly["Month"], format="%b %Y")
        monthly = monthly.sort_values("_s")
        fig = go.Figure()
        fig.add_bar(x=monthly[monthly["Type"]=="Income"]["Month"],
                    y=monthly[monthly["Type"]=="Income"]["Amount"],
                    name="Income", marker_color="#1B5E20", marker_line_width=0, opacity=0.9)
        fig.add_bar(x=monthly[monthly["Type"]=="Expense"]["Month"],
                    y=monthly[monthly["Type"]=="Expense"]["Amount"],
                    name="Expenses", marker_color="#B71C1C", marker_line_width=0, opacity=0.9)
        fig.update_layout(
            **base_layout(height=300, barmode="group"),
            yaxis=styled_yaxis(), xaxis=styled_xaxis(),
            legend=dict(orientation="h", y=1.08, x=0, font_size=12),
        )
        st.plotly_chart(fig, use_container_width=True)

    with col_r:
        st.markdown('<div class="section-title">Expenses by Category</div>', unsafe_allow_html=True)
        cat_data = exp.groupby("Category")["Amount"].sum().sort_values(ascending=False).reset_index()
        cat_data = cat_data[cat_data["Amount"] > 0]
        fig2 = px.pie(cat_data, values="Amount", names="Category",
                      color_discrete_sequence=PALETTE, hole=0.52)
        fig2.update_layout(
            **base_layout(height=300),
            legend=dict(orientation="v", x=1.02, y=0.5, font_size=11),
        )
        fig2.update_traces(textposition="inside", textinfo="percent",
                           hovertemplate="<b>%{label}</b><br>S$%{value:,.2f}<extra></extra>")
        st.plotly_chart(fig2, use_container_width=True)

    # ── Row 3: Weekly trend + Top 5 ──────────────────────────────────────────
    col_w, col_t = st.columns([1.35, 1])

    with col_w:
        st.markdown('<div class="section-title">Daily Spending</div>', unsafe_allow_html=True)
        # Specific month → show every day of that month
        # All Time → show last 60 days to keep it readable
        if dash_month != "All Time":
            daily_src = exp.copy()
        else:
            cutoff    = df_all["Date"].max() - pd.Timedelta(days=59)
            daily_src = exp_all[exp_all["Date"] >= cutoff].copy()

        daily = daily_src.groupby(daily_src["Date"].dt.date)["Amount"].sum().reset_index()
        daily.columns = ["Date", "Amount"]
        daily["Label"] = pd.to_datetime(daily["Date"]).dt.strftime("%d %b")

        fig3 = go.Figure()
        fig3.add_bar(
            x=daily["Label"], y=daily["Amount"],
            marker_color="#004D40", marker_line_width=0, opacity=0.75,
            hovertemplate="<b>%{x}</b><br>S$%{y:,.2f}<extra></extra>",
        )
        # Average daily line
        avg_d = daily["Amount"].mean()
        fig3.add_hline(
            y=avg_d, line_dash="dot", line_color="#E65100", line_width=1.5,
            annotation_text=f"Avg S${avg_d:,.0f}",
            annotation_position="top right",
            annotation_font_size=11,
            annotation_font_color="#E65100",
        )
        fig3.update_layout(
            **base_layout(height=250),
            yaxis=styled_yaxis(), xaxis=styled_xaxis(),
            bargap=0.25,
        )
        st.plotly_chart(fig3, use_container_width=True)

    with col_t:
        st.markdown('<div class="section-title">Top 5 Expenses</div>', unsafe_allow_html=True)
        top5 = exp.nlargest(5, "Amount")[["Date","Description","Category","Amount"]].copy()
        top5["Date"] = top5["Date"].dt.strftime("%d %b")
        st.dataframe(top5.reset_index(drop=True), width="stretch", height=230,
                     column_config={
                         "Date":        st.column_config.TextColumn("Date", width=60),
                         "Description": st.column_config.TextColumn("Description"),
                         "Category":    st.column_config.TextColumn("Category", width=110),
                         "Amount":      st.column_config.NumberColumn("S$", format="S$%.2f", width=80),
                     })

    # ── Smart Recommendations ─────────────────────────────────────────────────
    st.markdown('<div class="section-title">💡 Smart Recommendations</div>', unsafe_allow_html=True)
    st.caption("Analysed from your actual spending — highest-impact actions first.")

    top_recs = smart_recommendations(exp, inc, selected_month, top_n=3)
    for r in top_recs:
        st.markdown(rec_card(r["priority"], r["title"], r["body"],
                             r["action"], r["impact"]), unsafe_allow_html=True)

    st.markdown(
        "<div style='text-align:right;margin-top:-4px'>"
        "<small style='color:#7A9E98'>→ See full analysis in the 💡 Insights page</small></div>",
        unsafe_allow_html=True
    )

    # ── Savings Forecast ──────────────────────────────────────────────────────
    st.markdown('<div class="section-title">🔮 Savings Forecast</div>', unsafe_allow_html=True)
    st.caption("Based on your all-time average monthly income across 3 scenarios.")

    avg_inc  = inc_all["Amount"].sum() / N_MONTHS
    avg_exp  = exp_all["Amount"].sum() / N_MONTHS
    sub_cuts = 82.62 + 28.59 + 17.46
    food_mo  = exp_all[exp_all["Category"] == "Food"]["Amount"].sum() / N_MONTHS
    shop_mo  = exp_all[exp_all["Category"] == "Shopping"]["Amount"].sum() / N_MONTHS
    opt_cut  = sub_cuts + food_mo * 0.15 + shop_mo * 0.15

    f1, f2, f3 = st.columns(3)
    scenarios = [
        (f1, "Current Trajectory",  avg_exp,            "#004D40",
         "Maintaining current habits"),
        (f2, "Cut Redundant Subs",  avg_exp - sub_cuts, "#00897B",
         f"Cancel AVG, ChatGPT, Spotify — S${sub_cuts:.0f}/month saved"),
        (f3, "Fully Optimised",     avg_exp - opt_cut,  "#1B5E20",
         f"Subs + 15% less Food & Shopping — S${opt_cut:.0f}/month saved"),
    ]
    for col, label, scenario_exp, color, note in scenarios:
        saving = avg_inc - scenario_exp
        with col:
            st.markdown(forecast_card(label, saving, avg_inc, note, color),
                        unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# PAGE: SPENDING ANALYSIS
# ══════════════════════════════════════════════════════════════════════════════
elif page == "📈  Spending Analysis":
    st.markdown('<div class="page-title">Spending Analysis</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="page-subtitle">{selected_month}</div>', unsafe_allow_html=True)

    tab_charts, tab_txn = st.tabs(["📊  Charts & Summary", "💳  Transactions"])

    # ── TAB 1: Charts ─────────────────────────────────────────────────────────
    with tab_charts:
        st.markdown('<div class="section-title">Category Breakdown</div>', unsafe_allow_html=True)
        cat_data = exp.groupby("Category")["Amount"].sum().sort_values().reset_index()
        cat_data = cat_data[cat_data["Amount"] > 0]
        cat_data["pct"]   = (cat_data["Amount"] / cat_data["Amount"].sum() * 100).round(1)
        cat_data["label"] = cat_data.apply(lambda r: f"S${r['Amount']:,.0f}  ({r['pct']}%)", axis=1)
        fig = px.bar(cat_data, x="Amount", y="Category", orientation="h",
                     text="label", color="Amount",
                     color_continuous_scale=[[0,"#B2DFDB"],[1,"#004D40"]])
        fig.update_traces(textposition="outside", textfont_size=11, marker_line_width=0)
        fig.update_layout(
            **base_layout(height=max(300, len(cat_data) * 44)),
            coloraxis_showscale=False, showlegend=False,
            xaxis=dict(**styled_xaxis(), tickprefix="S$", title=""),
            yaxis=dict(gridcolor="#EFF4F3", zeroline=False, title=""),
        )
        fig.update_layout(margin=dict(l=0, r=140, t=24, b=0))
        st.plotly_chart(fig, use_container_width=True)

        c1, c2 = st.columns(2)
        with c1:
            st.markdown('<div class="section-title">Month-on-Month Comparison</div>', unsafe_allow_html=True)
            if len(MONTHS) >= 2:
                mom = exp_all.groupby(["Month","Category"])["Amount"].sum().reset_index()
                mom["_s"] = pd.to_datetime(mom["Month"], format="%b %Y")
                mom = mom.sort_values("_s")
                fig2 = px.bar(mom, x="Category", y="Amount", color="Month",
                              barmode="group", color_discrete_sequence=PALETTE)
                fig2.update_layout(
                    **base_layout(height=340), yaxis=styled_yaxis(),
                    xaxis=dict(**styled_xaxis(), tickangle=-35),
                    legend=dict(orientation="h", y=1.08, font_size=11), bargap=0.18,
                )
                st.plotly_chart(fig2, use_container_width=True)
            else:
                st.info("Need at least 2 months of data for comparison.")

        with c2:
            st.markdown('<div class="section-title">By Payment Method</div>', unsafe_allow_html=True)
            pay = exp.groupby("Payment Method")["Amount"].sum().sort_values(ascending=False).reset_index()
            pay = pay[pay["Amount"] > 0]
            fig3 = px.pie(pay, values="Amount", names="Payment Method",
                          color_discrete_sequence=PALETTE, hole=0.48)
            fig3.update_layout(
                **base_layout(height=340),
                legend=dict(orientation="h", y=-0.12, font_size=11),
            )
            fig3.update_traces(textinfo="percent+label", textposition="inside")
            st.plotly_chart(fig3, use_container_width=True)

        st.markdown('<div class="section-title">Monthly Summary</div>', unsafe_allow_html=True)
        rows = []
        for m in MONTHS:
            mi = inc_all[inc_all["Month"]==m]["Amount"].sum()
            me = exp_all[exp_all["Month"]==m]["Amount"].sum()
            mn = mi - me
            mr = mn / mi * 100 if mi > 0 else 0
            rows.append({"Month":m, "Income":f"S${mi:,.2f}", "Expenses":f"S${me:,.2f}",
                         "Net Savings":f"S${mn:,.2f}", "Savings Rate":f"{mr:.1f}%",
                         "# Transactions": len(exp_all[exp_all["Month"]==m])})
        st.dataframe(pd.DataFrame(rows), width="stretch", hide_index=True)

    # ── TAB 2: Transactions ───────────────────────────────────────────────────
    with tab_txn:
        txn_all = df.sort_values("Date", ascending=False).copy()

        # Use selected_month in keys so state resets when the month changes
        _mk = selected_month.replace(" ", "_")
        fa, fb, fc, fd = st.columns([1, 1, 1, 2])
        type_f   = fa.multiselect("Type",     ["Income","Expense"],
                                  default=["Income","Expense"],
                                  key=f"txn_type_{_mk}")
        cat_f    = fb.multiselect("Category", sorted(txn_all["Category"].unique()),
                                  default=list(txn_all["Category"].unique()),
                                  key=f"txn_cat_{_mk}")
        pay_f    = fc.multiselect("Payment",  sorted(txn_all["Payment Method"].unique()),
                                  default=list(txn_all["Payment Method"].unique()),
                                  key=f"txn_pay_{_mk}")
        search_f = fd.text_input("🔍 Search description or notes",
                                 key=f"txn_search_{_mk}")

        txn = txn_all[
            txn_all["Type"].isin(type_f) &
            txn_all["Category"].isin(cat_f) &
            txn_all["Payment Method"].isin(pay_f)
        ]
        if search_f:
            txn = txn[
                txn["Description"].str.contains(search_f, case=False, na=False) |
                txn["Notes"].str.contains(search_f, case=False, na=False)
            ]

        # Summary strip
        t_inc = txn[txn["Type"]=="Income"]["Amount"].sum()
        t_exp = txn[txn["Type"]=="Expense"]["Amount"].sum()
        s1, s2, s3, s4 = st.columns(4)
        s1.metric("Transactions", len(txn))
        s2.metric("Income",   f"S${t_inc:,.2f}")
        s3.metric("Expenses", f"S${t_exp:,.2f}")
        s4.metric("Net",      f"S${t_inc - t_exp:,.2f}")

        # Table
        display_txn = txn[["Date","Type","Category","Description",
                            "Amount","Payment Method","Notes"]].copy()
        display_txn["Date"] = display_txn["Date"].dt.strftime("%d %b %Y")

        st.dataframe(
            display_txn.reset_index(drop=True),
            width="stretch",
            height=500,
            column_config={
                "Date":           st.column_config.TextColumn("Date",     width=90),
                "Type":           st.column_config.TextColumn("Type",     width=75),
                "Category":       st.column_config.TextColumn("Category", width=115),
                "Description":    st.column_config.TextColumn("Description"),
                "Amount":         st.column_config.NumberColumn("Amount (SGD)", format="S$%.2f"),
                "Payment Method": st.column_config.TextColumn("Payment",  width=110),
                "Notes":          st.column_config.TextColumn("Notes",    width=130),
            },
        )

        csv_sa = txn.to_csv(index=False).encode("utf-8")
        st.download_button(
            "⬇️ Download as CSV",
            csv_sa,
            f"transactions_{selected_month.replace(' ','_')}.csv",
            "text/csv",
        )


# ══════════════════════════════════════════════════════════════════════════════
# PAGE: INSIGHTS
# ══════════════════════════════════════════════════════════════════════════════
elif page == "💡  Insights":
    st.markdown('<div class="page-title">Insights & Recommendations</div>', unsafe_allow_html=True)
    st.markdown(
        f'<div class="page-subtitle">{selected_month} · '
        f'Generated from your actual spending data</div>',
        unsafe_allow_html=True
    )

    all_inc  = inc_all["Amount"].sum()
    all_exp  = exp_all["Amount"].sum()
    all_rate = (all_inc - all_exp) / all_inc * 100 if all_inc > 0 else 0
    sub_exp  = exp_all[exp_all["Category"]=="Subscription"]["Amount"].sum()
    sub_n    = len(exp_all[exp_all["Category"]=="Subscription"])

    # ── Dynamic month comparison ──────────────────────────────────────────────
    if selected_month != "All Time":
        p_inc, p_exp, p_label = prev_month_stats(selected_month)

        if p_label:
            st.markdown(
                f'<div class="section-title">📅 {selected_month} vs {p_label}</div>',
                unsafe_allow_html=True
            )

            curr_cats = exp[exp["Type"]=="Expense"].groupby("Category")["Amount"].sum()
            prev_exp_df = df_all[df_all["Month"]==p_label]
            prev_cats = prev_exp_df[prev_exp_df["Type"]=="Expense"].groupby("Category")["Amount"].sum()

            all_cats_both = sorted(set(curr_cats.index) | set(prev_cats.index))
            comparison = []
            for cat in all_cats_both:
                curr_amt = curr_cats.get(cat, 0)
                prev_amt = prev_cats.get(cat, 0)
                delta    = curr_amt - prev_amt
                pct_chg  = (delta / prev_amt * 100) if prev_amt > 0 else (100 if curr_amt > 0 else 0)
                comparison.append({
                    "cat": cat, "curr": curr_amt,
                    "prev": prev_amt, "delta": delta, "pct": pct_chg
                })

            comp_df = pd.DataFrame(comparison).sort_values("delta", ascending=False)
            increases = comp_df[comp_df["delta"] > 5].head(4)
            decreases = comp_df[comp_df["delta"] < -5].tail(4)

            col_up, col_dn = st.columns(2)

            with col_up:
                st.markdown(
                    f"<div style='font-size:12px;font-weight:600;color:#B71C1C;"
                    f"letter-spacing:1px;margin-bottom:8px'>▲ INCREASED vs {p_label}</div>",
                    unsafe_allow_html=True
                )
                if increases.empty:
                    st.caption("No categories increased this month. 🎉")
                else:
                    for _, row in increases.iterrows():
                        pct_disp = f"+{row['pct']:.0f}%" if row['prev'] > 0 else "NEW"
                        bar_pct  = min(row["curr"] / max(comp_df["curr"].max(), 1) * 100, 100)
                        st.markdown(
                            f"<div style='margin-bottom:10px'>"
                            f"<div style='display:flex;justify-content:space-between;"
                            f"margin-bottom:4px'>"
                            f"<span style='font-weight:500'>{row['cat']}</span>"
                            f"<span><b>S${row['curr']:,.0f}</b>"
                            f" <span class='mover-up'>{pct_disp}</span></span></div>"
                            + prog_bar(bar_pct, "#B71C1C") +
                            f"<div style='font-size:11px;color:#7A9E98;margin-top:2px'>"
                            f"Was S${row['prev']:,.0f} in {p_label} · "
                            f"S${abs(row['delta']):,.0f} more</div>"
                            f"</div>",
                            unsafe_allow_html=True
                        )

            with col_dn:
                st.markdown(
                    f"<div style='font-size:12px;font-weight:600;color:#1B5E20;"
                    f"letter-spacing:1px;margin-bottom:8px'>▼ DECREASED vs {p_label}</div>",
                    unsafe_allow_html=True
                )
                if decreases.empty:
                    st.caption("No categories decreased this month.")
                else:
                    for _, row in decreases.sort_values("delta").iterrows():
                        pct_disp = f"{row['pct']:.0f}%"
                        bar_pct  = min(row["curr"] / max(comp_df["curr"].max(), 1) * 100, 100)
                        st.markdown(
                            f"<div style='margin-bottom:10px'>"
                            f"<div style='display:flex;justify-content:space-between;"
                            f"margin-bottom:4px'>"
                            f"<span style='font-weight:500'>{row['cat']}</span>"
                            f"<span><b>S${row['curr']:,.0f}</b>"
                            f" <span class='mover-down'>{pct_disp}</span></span></div>"
                            + prog_bar(bar_pct, "#1B5E20") +
                            f"<div style='font-size:11px;color:#7A9E98;margin-top:2px'>"
                            f"Was S${row['prev']:,.0f} in {p_label} · "
                            f"S${abs(row['delta']):,.0f} less</div>"
                            f"</div>",
                            unsafe_allow_html=True
                        )

            # Dynamic text recommendations based on movers
            st.markdown('<div class="section-title">💬 What This Month Tells You</div>',
                        unsafe_allow_html=True)

            dynamic_recs = []
            for _, row in increases.iterrows():
                if row["pct"] > 50 and row["prev"] > 0:
                    dynamic_recs.append((
                        "high",
                        f"{row['cat']} spending jumped {row['pct']:.0f}%",
                        f"You spent S${row['curr']:,.0f} on {row['cat']} this month vs "
                        f"S${row['prev']:,.0f} in {p_label} — a S${row['delta']:,.0f} increase. "
                        f"{'One-off or a new habit? Tag it clearly so future months look accurate.' if row['curr'] > 200 else 'Small in absolute terms but worth noting the trend.'} ",
                        f"📊 Review if this is recurring"
                    ))
                elif row["curr"] > 0 and row["prev"] == 0:
                    dynamic_recs.append((
                        "med",
                        f"New spending in {row['cat']} this month",
                        f"S${row['curr']:,.0f} in {row['cat']} — not present in {p_label}. "
                        f"If this is a one-off, tag it so it doesn't distort your monthly average.",
                        f"🏷️ Tag as one-off if applicable"
                    ))

            # Savings rate change recommendation
            if p_inc and p_exp:
                curr_rate = (total_inc - total_exp) / total_inc * 100 if total_inc > 0 else 0
                prev_rate = (p_inc - p_exp) / p_inc * 100 if p_inc > 0 else 0
                rate_diff = curr_rate - prev_rate
                if rate_diff < -5:
                    dynamic_recs.append((
                        "high",
                        f"Savings rate dropped {abs(rate_diff):.1f}pp vs {p_label}",
                        f"Your savings rate fell from {prev_rate:.1f}% to {curr_rate:.1f}%. "
                        f"The main driver: {increases.iloc[0]['cat'] if not increases.empty else 'higher overall spending'}. "
                        f"If this was a one-off month, no action needed — but if the pattern repeats, revisit your budget targets.",
                        f"🎯 Target: maintain above {prev_rate:.0f}%"
                    ))
                elif rate_diff > 5:
                    dynamic_recs.append((
                        "info",
                        f"Savings rate improved {rate_diff:.1f}pp vs {p_label} 🎉",
                        f"Great month — savings rate went from {prev_rate:.1f}% to {curr_rate:.1f}%. "
                        f"{'Lower spending in ' + ', '.join(decreases['cat'].head(2).tolist()) + ' helped.' if not decreases.empty else ''} "
                        f"Try to maintain this as your new baseline.",
                        f"✅ New target: {curr_rate:.0f}%+ savings rate"
                    ))

            if not dynamic_recs:
                dynamic_recs.append((
                    "info",
                    "Spending patterns are stable vs last month",
                    f"No major category shifts vs {p_label}. "
                    f"Your total expenses moved from S${p_exp:,.0f} to S${total_exp:,.0f}. "
                    f"Keep tracking — patterns become clearer with more months of data.",
                    "📈 Stay consistent"
                ))

            badge_style = {"high":"badge-high","med":"badge-med","info":"badge-info","good":"badge-good"}
            badge_label_map = {"high":"HIGH IMPACT","med":"MEDIUM","info":"INFO","good":"GOOD NEWS"}

            for priority, title, body, saving in dynamic_recs:
                st.markdown(f"""
                <div class="insight-card">
                  <div style="display:flex;align-items:center;gap:10px;margin-bottom:2px">
                    <span class="badge {badge_style[priority]}">{badge_label_map[priority]}</span>
                    <span class="insight-title">{title}</span>
                  </div>
                  <div class="insight-body">{body}</div>
                  <div class="insight-save">{saving}</div>
                </div>""", unsafe_allow_html=True)

        else:
            st.info(f"No previous month data to compare against — this is your earliest recorded month.")

    # ── Full smart recommendations ────────────────────────────────────────────
    st.markdown('<div class="section-title">💡 All Recommendations</div>', unsafe_allow_html=True)
    st.caption("Prioritised by annual savings impact. Updated based on your real data.")

    all_recs = smart_recommendations(exp, inc, selected_month)
    for r in all_recs:
        st.markdown(rec_card(r["priority"], r["title"], r["body"],
                             r["action"], r["impact"]), unsafe_allow_html=True)

    # ── Financial health snapshot ─────────────────────────────────────────────
    st.markdown('<div class="section-title">Financial Health Snapshot</div>', unsafe_allow_html=True)
    h1, h2, h3, h4 = st.columns(4)
    h1.metric("Overall Savings Rate",    f"{all_rate:.1f}%",               "⭐ Excellent")
    h2.metric("Avg Monthly Income",      f"S${all_inc / N_MONTHS:,.0f}",   "Stable")
    h3.metric("Subscription Spend",      f"S${sub_exp:,.0f}",              f"{sub_n} logged")
    h4.metric("Monthly Expense Average", f"S${all_exp / N_MONTHS:,.0f}",   "Tracked period")

    # ── Subscription audit ────────────────────────────────────────────────────
    st.markdown('<div class="section-title">Subscription Audit</div>', unsafe_allow_html=True)
    subscriptions = [
        ("Anytime Fitness",  89.00, "keep", "Great habit. Verify 3×/week+ attendance."),
        ("AVG Antivirus",    82.62, "cut",  "Windows Defender is #1 by AV-TEST. Cancel → saves S$83/mo."),
        ("Newspaper",        33.90, "rev",  "Only worth it if read daily. Free: CNA, ST (limited)."),
        ("Claude",           30.00, "keep", "You're using it — keep."),
        ("ChatGPT",          28.59, "cut",  "Duplicate AI with Claude. Cancel → save S$29/mo."),
        ("Netflix",          22.98, "rev",  "Review overlap with YouTube Premium."),
        ("Spotify",          17.46, "cut",  "YouTube Premium includes YouTube Music. Cancel → save S$17/mo."),
        ("YouTube Premium",  17.98, "keep", "Includes ad-free + YouTube Music. Keep if cancelling Spotify."),
        ("iCloud",           13.98, "keep", "Essential for iOS backup. Good value."),
        ("Hetzner VPS",      13.45, "keep", "Dev server — keep if actively used."),
        ("NTUC Membership",   9.00, "keep", "Pays for itself in FairPrice discounts."),
        ("Gomo (mobile)",     7.00, "keep", "Very affordable SIM plan. Keep."),
        ("Prime",             5.00, "rev",  "S$5 borderline — review if used regularly."),
    ]
    pill_class = {"cut":"pill-cut","keep":"pill-keep","rev":"pill-rev"}
    pill_label = {"cut":"❌ Cut","keep":"✅ Keep","rev":"🟡 Review"}
    potential_save = sum(amt for _, amt, s, _ in subscriptions if s == "cut")

    hdr = st.columns([3, 1, 1, 4])
    for col, lbl in zip(hdr, ["Subscription","S$/mo","Action","Reason"]):
        col.markdown(small_label(lbl), unsafe_allow_html=True)
    st.markdown("<hr style='border-color:#DDE9E7;margin:4px 0 8px'>", unsafe_allow_html=True)

    for name, amt, status, reason in subscriptions:
        c0, c1, c2, c3 = st.columns([3, 1, 1, 4])
        c0.markdown(f"**{name}**")
        c1.markdown(f"S${amt:.2f}")
        c2.markdown(
            f'<span class="pill {pill_class[status]}">{pill_label[status]}</span>',
            unsafe_allow_html=True
        )
        c3.caption(reason)

    st.success(
        f"💡 Potential saving: **S${potential_save:.0f}/month** = "
        f"**S${potential_save * 12:.0f}/year** by cutting redundant subscriptions only."
    )

    # ── SG Benchmarks ─────────────────────────────────────────────────────────
    st.markdown('<div class="section-title">Your Spending vs SG Benchmarks</div>', unsafe_allow_html=True)

    def m_avg(cat):
        return exp_all[exp_all["Category"]==cat]["Amount"].sum() / N_MONTHS

    benchmarks = [
        ("Food",          m_avg("Food"),          300, 500, "Dining out avg — reasonable for SG"),
        ("Groceries",     m_avg("Grocery"),         150, 250, "Low — you dine out more than cook"),
        ("Transport",     m_avg("Transport"),       100, 200, "Very low — mostly bus. Excellent."),
        ("Subscriptions", sub_exp / N_MONTHS,       50,  120, "Above typical range — audit recommended"),
        ("Shopping",      m_avg("Shopping"),        200, 400, "Mix of everyday + KL shopping"),
        ("Entertainment", m_avg("Entertainment"),   50,  150, "Including Pokemon hobby"),
    ]

    hdr2 = st.columns([2, 1, 1, 1, 3])
    for col, lbl in zip(hdr2, ["Category","Your avg/mo","SG Low","SG High","Note"]):
        col.markdown(small_label(lbl), unsafe_allow_html=True)
    st.markdown("<hr style='border-color:#DDE9E7;margin:4px 0 8px'>", unsafe_allow_html=True)

    for cat, your, lo, hi, note in benchmarks:
        status = "🟢" if your <= hi else "🔴" if your > hi * 1.3 else "🟡"
        c0, c1, c2, c3, c4 = st.columns([2, 1, 1, 1, 3])
        c0.markdown(f"**{cat}**")
        c1.markdown(f"**S${your:,.0f}**")
        c2.markdown(f"S${lo:,}")
        c3.markdown(f"S${hi:,}")
        c4.caption(f"{status} {note}")


# ══════════════════════════════════════════════════════════════════════════════
# PAGE: TRANSACTIONS
# ══════════════════════════════════════════════════════════════════════════════
elif page == "💳  Transactions":
    st.markdown('<div class="page-title">Transactions</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="page-subtitle">{selected_month}</div>', unsafe_allow_html=True)

    fc1, fc2, fc3 = st.columns([1, 1, 2])
    with fc1:
        type_filter = st.multiselect("Type", ["Income","Expense"], default=["Income","Expense"])
    with fc2:
        cat_opts   = sorted(df["Category"].unique().tolist())
        cat_filter = st.multiselect("Category", cat_opts, default=cat_opts)
    with fc3:
        search = st.text_input("🔍 Search description", "")

    filtered = df[df["Type"].isin(type_filter) & df["Category"].isin(cat_filter)]
    if search:
        filtered = filtered[filtered["Description"].str.contains(search, case=False, na=False)]

    filtered = filtered.sort_values("Date", ascending=False)
    display  = filtered[["Date","Type","Category","Description",
                          "Amount","Payment Method","Notes"]].copy()
    display["Date"] = display["Date"].dt.strftime("%d %b %Y")

    st.markdown(
        f"<small style='color:#7A9E98'>Showing <b>{len(display)}</b> of {len(df)} transactions</small>",
        unsafe_allow_html=True
    )
    st.dataframe(
        display.reset_index(drop=True),
        width="stretch", height=520,
        column_config={
            "Date":           st.column_config.TextColumn("Date", width=90),
            "Type":           st.column_config.TextColumn("Type", width=75),
            "Category":       st.column_config.TextColumn("Category", width=120),
            "Description":    st.column_config.TextColumn("Description"),
            "Amount":         st.column_config.NumberColumn("Amount (SGD)", format="S$%.2f"),
            "Payment Method": st.column_config.TextColumn("Payment", width=110),
            "Notes":          st.column_config.TextColumn("Notes", width=130),
        },
    )
    csv = filtered.to_csv(index=False).encode("utf-8")
    st.download_button(
        "⬇️ Download filtered transactions as CSV",
        csv, f"transactions_{selected_month.replace(' ','_')}.csv", "text/csv",
    )


# ══════════════════════════════════════════════════════════════════════════════
# PAGE: NET WORTH
# ══════════════════════════════════════════════════════════════════════════════
elif page == "🏦  Net Worth":
    st.markdown('<div class="page-title">Net Worth Tracker</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="page-subtitle">Enter your end-of-month balances — chart updates live</div>',
        unsafe_allow_html=True
    )
    st.info("Your data lives in this session. Export as CSV to save it between visits.", icon="ℹ️")

    months_nw = ["May 2026","Jun 2026","Jul 2026","Aug 2026",
                 "Sep 2026","Oct 2026","Nov 2026","Dec 2026"]

    if "nw_data" not in st.session_state:
        st.session_state.nw_data = {
            m: {"DBS/POSB":0.0,"Citi Bank":0.0,"Other Bank":0.0,"Cash":0.0,
                "CPF OA":0.0,"CPF SA":0.0,"CPF MA":0.0,"Stocks/ETFs":0.0}
            for m in months_nw
        }

    active_month = st.selectbox("Month to enter / edit", months_nw)
    d = st.session_state.nw_data[active_month]

    st.markdown('<div class="section-title">Cash & Bank Accounts</div>', unsafe_allow_html=True)
    bc1, bc2, bc3, bc4 = st.columns(4)
    d["DBS/POSB"]   = bc1.number_input("DBS / POSB",   value=d["DBS/POSB"],   step=100.0, format="%.2f", key=f"dbs_{active_month}")
    d["Citi Bank"]  = bc2.number_input("Citi Bank",    value=d["Citi Bank"],  step=100.0, format="%.2f", key=f"citi_{active_month}")
    d["Other Bank"] = bc3.number_input("Other Bank",   value=d["Other Bank"], step=100.0, format="%.2f", key=f"other_{active_month}")
    d["Cash"]       = bc4.number_input("Cash on Hand", value=d["Cash"],       step=10.0,  format="%.2f", key=f"cash_{active_month}")

    st.markdown('<div class="section-title">CPF Accounts</div>', unsafe_allow_html=True)
    cc1, cc2, cc3 = st.columns(3)
    d["CPF OA"] = cc1.number_input("CPF Ordinary (OA)", value=d["CPF OA"], step=100.0, format="%.2f", key=f"oa_{active_month}")
    d["CPF SA"] = cc2.number_input("CPF Special (SA)",  value=d["CPF SA"], step=100.0, format="%.2f", key=f"sa_{active_month}")
    d["CPF MA"] = cc3.number_input("CPF MediSave (MA)", value=d["CPF MA"], step=100.0, format="%.2f", key=f"ma_{active_month}")

    st.markdown('<div class="section-title">Investments</div>', unsafe_allow_html=True)
    d["Stocks/ETFs"] = st.number_input(
        "Stocks / ETFs (market value)", value=d["Stocks/ETFs"],
        step=100.0, format="%.2f", key=f"inv_{active_month}"
    )
    st.session_state.nw_data[active_month] = d

    rows = []
    for m in months_nw:
        v = st.session_state.nw_data[m]
        cash_t = v["DBS/POSB"] + v["Citi Bank"] + v["Other Bank"] + v["Cash"]
        cpf_t  = v["CPF OA"] + v["CPF SA"] + v["CPF MA"]
        nw     = cash_t + cpf_t + v["Stocks/ETFs"]
        rows.append({"Month":m,"Cash":cash_t,"CPF OA":v["CPF OA"],
                     "Total CPF":cpf_t,"Investments":v["Stocks/ETFs"],"Net Worth":nw})
    nw_df    = pd.DataFrame(rows)
    has_data = nw_df["Net Worth"].sum() > 0

    if has_data:
        st.markdown('<div class="section-title">Net Worth Over Time</div>', unsafe_allow_html=True)
        fig = go.Figure()
        fig.add_scatter(x=nw_df["Month"], y=nw_df["Cash"],
                        name="Cash in Hand", mode="lines+markers",
                        line=dict(color="#004D40", width=3),
                        marker=dict(size=9, line=dict(color="white", width=2)),
                        fill="tozeroy", fillcolor="rgba(0,77,64,0.06)")
        fig.add_scatter(x=nw_df["Month"], y=nw_df["CPF OA"],
                        name="CPF OA", mode="lines+markers",
                        line=dict(color="#0D47A1", width=3, dash="dot"),
                        marker=dict(size=9, symbol="diamond", line=dict(color="white", width=2)))
        fig.add_scatter(x=nw_df["Month"], y=nw_df["Net Worth"],
                        name="Total Net Worth", mode="lines+markers",
                        line=dict(color="#E65100", width=2.5),
                        marker=dict(size=8, symbol="square", line=dict(color="white", width=1.5)))
        fig.update_layout(
            **base_layout(height=380),
            yaxis=dict(**styled_yaxis(), tickformat=",.0f"),
            xaxis=styled_xaxis(),
            legend=dict(orientation="h", y=1.08, x=0, font_size=12),
            hovermode="x unified",
        )
        st.plotly_chart(fig, use_container_width=True)

        cur = rows[months_nw.index(active_month)]
        k1, k2, k3, k4 = st.columns(4)
        k1.metric("Cash in Hand", f"S${cur['Cash']:,.0f}")
        k2.metric("CPF OA",       f"S${cur['CPF OA']:,.0f}")
        k3.metric("Total CPF",    f"S${cur['Total CPF']:,.0f}")
        k4.metric("Net Worth",    f"S${cur['Net Worth']:,.0f}")

        display_nw = nw_df.copy()
        for col in ["Cash","CPF OA","Total CPF","Investments","Net Worth"]:
            display_nw[col] = display_nw[col].apply(lambda x: f"S${x:,.0f}" if x > 0 else "—")
        st.dataframe(display_nw, width="stretch", hide_index=True)

        csv_nw = nw_df.to_csv(index=False).encode("utf-8")
        st.download_button("⬇️ Export Net Worth as CSV", csv_nw, "net_worth.csv", "text/csv")
    else:
        st.markdown("""
        <div style='text-align:center;padding:70px 20px;color:#7A9E98;'>
          <div style='font-size:56px'>🏦</div>
          <div style='font-family:DM Serif Display,serif;font-size:20px;
                      margin-top:16px;color:#004D40;'>
            Enter your balances above to see the chart
          </div>
          <div style='font-size:13px;margin-top:8px'>
            Track your cash, CPF, and investments month by month
          </div>
        </div>""", unsafe_allow_html=True)
