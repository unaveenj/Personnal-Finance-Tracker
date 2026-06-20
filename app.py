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
.pill-new  { background: #DBEAFE; color: #1E3A8A; }

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
_GID       = "1321769101"
_NW_GID    = "2019544975"
GSHEET_URL = (
    f"https://docs.google.com/spreadsheets/d/{_SHEET_ID}"
    f"/export?format=csv&gid={_GID}"
)
NW_GSHEET_URL = (
    f"https://docs.google.com/spreadsheets/d/{_SHEET_ID}"
    f"/export?format=csv&gid={_NW_GID}"
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
    df.rename(columns={"Amount (SGD)": "Amount", "Card / Account": "Card"}, inplace=True)
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

@st.cache_data(ttl=300)
def load_networth():
    try:
        df = pd.read_csv(NW_GSHEET_URL)
    except Exception as e:
        st.error(
            "**Cannot load Net Worth sheet.**\n\n"
            f"`{e}`"
        )
        return pd.DataFrame()
    df.columns = df.columns.str.strip()
    numeric_cols = ["DBS","Maribank","UOB","OCBC","Citi","Chocolate",
                    "IBKR","CPF (OA)","CPF (SA)","CPF (MA)",
                    "Wife savings cash","Liquid Cash","Total networth"]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(
                df[col].astype(str).str.replace("S$", "", regex=False).str.replace(",", ""),
                errors="coerce"
            ).fillna(0)
    df["Month"] = df["Month"].astype(str).str.strip()
    df["_sort"] = pd.to_datetime(df["Month"], format="%b %Y", errors="coerce")
    df = df.sort_values("_sort").drop(columns=["_sort"]).reset_index(drop=True)
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

CATEGORY_GROUPS = {
    "Food & Dining":  "Food",
    "Groceries":      "Food",
    "Transport":      "Transport & Travel",
    "Travel":         "Transport & Travel",
    "Shopping":       "Shopping",
    "Entertainment":  "Shopping",
    "Gifts":          "Shopping",
    "Bills & Utilities": "Bills & Utilities",
    "Subscriptions":  "Subscriptions",
    "Health & Fitness": "Health & Education",
    "Education":      "Health & Education",
    "Family":         "Family & Giving",
    "Donations":      "Family & Giving",
    "Misc":           "Other",
    "Refunds":        "Other",
}

GROUP_COLORS = {
    "Food":                "#2E7D32",
    "Transport & Travel":  "#1565C0",
    "Shopping":            "#E65100",
    "Bills & Utilities":   "#6A1B9A",
    "Subscriptions":       "#00838F",
    "Health & Education":  "#AD1457",
    "Family & Giving":     "#F9A825",
    "Other":               "#546E7A",
}

def base_layout(**extra):
    base = dict(
        plot_bgcolor="white", paper_bgcolor="white",
        font=dict(family="DM Sans", color="#1C3A35"),
        margin=dict(l=0, r=0, t=24, b=0),
    )
    base.update(extra)
    return base

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

    # ── 3. Redundant subscriptions (data-driven from last 2 months) ──
    _rsub_months = MONTHS[-2:] if len(MONTHS) >= 2 else MONTHS
    _rsub_df = exp_all[
        (exp_all["Category"] == "Subscriptions") &
        (exp_all["Month"].isin(_rsub_months))
    ]
    _sub_map = {}
    for _, _r in _rsub_df.sort_values("Date").iterrows():
        _sub_map[_r["Description"].strip().lower()] = (_r["Description"].strip(), _r["Amount"])

    _sub_names = set(_sub_map.keys())
    _has_claude  = "claude"  in _sub_names
    _has_youtube = "youtube" in _sub_names
    _has_netflix = "netflix" in _sub_names

    _redundancy_rules = [
        ("chatgpt", "You're paying for Claude — ChatGPT duplicates it"       if _has_claude  else "Consolidate AI tools"),
        ("gemini",  "You're paying for Claude — Gemini duplicates it"        if _has_claude  else "Consolidate AI tools"),
        ("spotify", "YouTube subscription already covers music streaming"     if _has_youtube else "Check if worth keeping"),
        ("disney+", "You have Netflix — evaluate if both are worth keeping"   if _has_netflix else "Review streaming overlap"),
    ]

    sub_cuts_list = []
    for _key, _reason in _redundancy_rules:
        if _key in _sub_names:
            _name, _amt = _sub_map[_key]
            sub_cuts_list.append((_name, _amt, _reason))

    if sub_cuts_list:
        sub_total = sum(a for _, a, _ in sub_cuts_list)
        n_cuts    = len(sub_cuts_list)
        detail    = "; ".join(f"{n} (S${a:.0f})" for n, a, _ in sub_cuts_list)
        reasons   = " ".join(f"<b>{n}:</b> {r}." for n, _, r in sub_cuts_list)
        recs.append(dict(
            priority="high",
            title=f"Cancel {n_cuts} redundant subscription{'s' if n_cuts > 1 else ''} — zero lifestyle change",
            body=(
                f"{detail}. "
                f"{reasons} "
                f"Cancelling takes 10 minutes."
            ),
            action=f"Cancel today → save S${sub_total:.0f}/month (S${sub_total*12:.0f}/year)",
            impact=sub_total * 12,
        ))

    # ── 4. New large / unrecognised subscriptions ──
    all_subs = exp_all[exp_all["Category"] == "Subscriptions"].copy()
    if not all_subs.empty:
        sub_freq = (
            all_subs.groupby("Description")["Amount"]
            .agg(count="count", total="sum")
            .reset_index()
        )
        sub_freq["per_occ"] = sub_freq["total"] / sub_freq["count"]
        known_subs = {
            "chatgpt", "spotify", "claude", "netflix", "icloud", "youtube",
            "hetzner vps", "ntuc membership", "ntuc membeship", "gomo", "prime",
            "avg antivirus", "newspaper", "surfshark", "gemini", "disney+",
            "anytime fitness", "kodecloud",
        }
        new_big = sub_freq[
            (~sub_freq["Description"].str.lower().isin(known_subs)) &
            (sub_freq["per_occ"] >= 50)
        ].sort_values("per_occ", ascending=False)
        if not new_big.empty:
            names_amts = "; ".join(
                f"{r['Description']} (S${r['per_occ']:.0f}/occurrence, seen {r['count']}×)"
                for _, r in new_big.iterrows()
            )
            flagged_total = new_big["per_occ"].sum()
            recs.append(dict(
                priority="med",
                title="New large subscription(s) detected — confirm billing frequency",
                body=(
                    f"High-value subscriptions appeared recently: {names_amts}. "
                    f"Verify whether these are monthly recurring charges or annual one-offs. "
                    f"If monthly, they add <b>S${flagged_total*12:,.0f}/year</b> to your subscription bill."
                ),
                action="Log into each service and check your billing period",
                impact=flagged_total * 12,
            ))

    # ── 5. Investment gap / bank account optimisation ──
    idle_monthly = avg_inc_mo * (all_rate / 100)
    if idle_monthly > 500:
        recs.append(dict(
            priority="high",
            title="Maximise returns on your banking pile",
            body=(
                f"With a {all_rate:.0f}% savings rate, you generate ~S${idle_monthly:,.0f}/month of surplus. "
                f"You're already investing via IBKR — great start. But large balances sitting in standard "
                f"accounts earn sub-optimal rates. "
                f"OCBC 360 and UOB One offer <b>3–4%+ p.a.</b> when salary credit + spend criteria are met. "
                f"Continuing to DCA S${idle_monthly:,.0f}/month at 7% p.a. (VWRA) compounds to "
                f"<b>S${idle_monthly * 12 * 10 * 1.07**5:,.0f}</b> over 10 years."
            ),
            action="Review OCBC 360 / UOB One bonus interest tiers; continue IBKR DCA",
            impact=0,
        ))

    # ── 6. Food & dining vs SG benchmark ──
    food_mo = exp_all[exp_all["Category"] == "Food & Dining"]["Amount"].sum() / N_MONTHS
    if food_mo > 420:
        saving = food_mo - 380
        recs.append(dict(
            priority="med",
            title=f"Food & dining averaging S${food_mo:,.0f}/month — above SG median",
            body=(
                f"SG median dining spend for a single person is S$300–400/month. "
                f"You're averaging S${food_mo:,.0f} (travel months inflate this). "
                f"Hawker centre vs restaurant saves S$15–25 per meal — "
                f"3 swaps/week adds S${saving*12:,.0f} back to your savings annually."
            ),
            action="Set a S$380/month food budget; tag travel dining separately",
            impact=saving * 12,
        ))

    # ── 7. Entertainment spike ──
    ent_mo = exp_all[exp_all["Category"] == "Entertainment"]["Amount"].sum() / N_MONTHS
    if ent_mo > 120:
        recs.append(dict(
            priority="med",
            title=f"Entertainment averaging S${ent_mo:,.0f}/month — worth a ceiling",
            body=(
                f"Pokemon cards, movies and events averaged S${ent_mo:,.0f}/month. "
                f"SG benchmark is S$50–150/month. "
                f"A monthly hobby budget prevents lifestyle inflation without eliminating the enjoyment."
            ),
            action="Set a S$150/month entertainment cap; track Pokemon buys separately",
            impact=max(0, ent_mo - 150) * 12,
        ))

    # ── 8. Bank yield optimisation ──
    core_monthly = avg_exp_mo
    recs.append(dict(
        priority="info",
        title="Your emergency fund is strong — make sure it earns well",
        body=(
            f"Core monthly expenses average S${core_monthly:,.0f}. "
            f"A 6-month buffer is S${core_monthly*6:,.0f} — you already exceed this comfortably. "
            f"Maribank (2.5% p.a.), CIMB FastSaver (~3%), SingLife (~3.5%) all beat standard accounts. "
            f"Excess above 6 months should flow into IBKR or CPF top-ups, not sit idle."
        ),
        action="Confirm liquid savings are in a high-yield account, not a current account",
        impact=0,
    ))

    # Sort: high first, then by annual impact descending
    order = {"high": 0, "med": 1, "info": 2, "good": 3}
    recs.sort(key=lambda r: (order.get(r["priority"], 9), -r.get("impact", 0)))

    return recs[:top_n] if top_n else recs


# ── SMART INSIGHTS HELPERS ────────────────────────────────────────────────────

def _grade_letter(score):
    """Convert 0-100 score to (letter, hex_color, bar_pct)."""
    if score >= 85: return "A", "#166534", score
    if score >= 70: return "B", "#0F766E", score
    if score >= 50: return "C", "#92400E", score
    if score >= 30: return "D", "#C2410C", score
    return "F", "#991B1B", max(score, 5)


def _grade_card_html(area, letter, color, verdict, bar_pct):
    return f"""
    <div style='background:white;border-radius:12px;padding:16px 12px;text-align:center;
                box-shadow:0 1px 6px rgba(0,77,64,.07);height:100%'>
      <div style='font-size:9px;font-weight:700;letter-spacing:1px;text-transform:uppercase;
                  color:#7A9E98;margin-bottom:8px'>{area}</div>
      <div style='font-size:32px;font-weight:800;line-height:1;color:{color};
                  margin-bottom:6px'>{letter}</div>
      <div style='font-size:10px;color:#556B67;line-height:1.4;min-height:30px'>{verdict}</div>
      <div style='height:4px;background:#EFF4F3;border-radius:2px;margin-top:10px'>
        <div style='height:4px;background:{color};border-radius:2px;
                    width:{min(bar_pct,100):.0f}%'></div>
      </div>
    </div>"""


def _action_card_html(priority, area, title, detail, action_text, impact_annual=0):
    colors = {
        "high": ("#FEE2E2", "#991B1B", "#B71C1C"),
        "med":  ("#FEF3C7", "#92400E", "#F59E0B"),
        "good": ("#DCFCE7", "#166534", "#16A34A"),
        "info": ("#DBEAFE", "#1E3A8A", "#1565C0"),
    }
    bg, text, border = colors.get(priority, ("#F3F4F6", "#374151", "#9CA3AF"))
    labels = {"high": "HIGH", "med": "WATCH", "good": "GOOD", "info": "INFO"}
    lbl = labels.get(priority, priority.upper())
    if impact_annual > 0:
        impact_html = f"<div style='font-size:11px;font-weight:700;color:#166534;white-space:nowrap;padding-top:2px'>S${impact_annual:,.0f}/yr</div>"
    elif impact_annual < 0:
        impact_html = f"<div style='font-size:11px;font-weight:700;color:#166534;white-space:nowrap;padding-top:2px'>+S${abs(impact_annual):,.0f}/yr vs peers</div>"
    else:
        impact_html = ""
    return f"""
    <div style='background:white;border-radius:12px;padding:14px 16px;margin-bottom:8px;
                display:flex;align-items:flex-start;gap:14px;
                box-shadow:0 1px 6px rgba(0,77,64,.07);border-left:3px solid {border}'>
      <div style='padding-top:2px;flex-shrink:0'>
        <span style='background:{bg};color:{text};font-size:9px;font-weight:700;
                     letter-spacing:0.8px;padding:3px 8px;border-radius:6px;
                     white-space:nowrap'>{lbl} · {area}</span>
      </div>
      <div style='flex:1'>
        <div style='font-size:13px;font-weight:600;color:#1C3A35;margin-bottom:3px'>{title}</div>
        <div style='font-size:11px;color:#556B67;line-height:1.6'>{detail}</div>
        <div style='font-size:11px;font-weight:600;color:#004D40;margin-top:6px'>→ {action_text}</div>
      </div>
      {impact_html}
    </div>"""


def live_subscription_audit(exp_df, months_list):
    """Pull subscriptions from live data, estimate monthly cost, flag redundancies."""
    subs = exp_df[exp_df["Category"] == "Subscriptions"].copy()
    if subs.empty:
        return pd.DataFrame(columns=[
            "name_display", "per_occurrence", "months_seen", "monthly_cost", "status", "reason"
        ])

    subs["name_key"] = subs["Description"].str.strip().str.lower()
    name_display_map = (
        subs.sort_values("Date").groupby("name_key")["Description"].last().str.strip()
    )
    agg = subs.groupby("name_key")["Amount"].agg(total="sum", count="count").reset_index()
    agg["name_display"]   = agg["name_key"].map(name_display_map)
    agg["per_occurrence"] = agg["total"] / agg["count"]
    months_seen_s = subs.groupby("name_key")["Month"].nunique().rename("months_seen")
    agg = agg.merge(months_seen_s, on="name_key")

    n_mo = max(len(months_list), 1)
    agg["monthly_cost"] = agg.apply(
        lambda r: r["per_occurrence"] if r["months_seen"] >= n_mo * 0.7
        else r["per_occurrence"] * r["months_seen"] / n_mo,
        axis=1,
    )
    agg["is_new"] = (agg["months_seen"] == 1) & (n_mo > 1)

    present = set(agg["name_key"].tolist())
    def _has(kw): return any(kw in k for k in present)
    has_claude  = _has("claude")
    has_youtube = _has("youtube")
    has_netflix = _has("netflix")

    redundancy = {}
    if has_claude:
        for k in present:
            if "chatgpt" in k: redundancy[k] = ("cut",  "Duplicate AI — Claude covers this")
            if "gemini"  in k: redundancy[k] = ("cut",  "Duplicate AI — Claude covers this")
    if has_youtube:
        for k in present:
            if "spotify" in k: redundancy[k] = ("cut",  "YouTube Premium already covers music")
    if has_netflix:
        for k in present:
            if "disney"  in k: redundancy[k] = ("rev",  "Overlaps with Netflix — keep only one")

    known_keep = {
        "icloud", "claude", "anytime fitness", "ntuc", "hetzner",
        "youtube", "prime", "surfshark", "avg",
    }

    statuses, reasons = [], []
    for _, row in agg.iterrows():
        k = row["name_key"]
        if k in redundancy:
            s, r = redundancy[k]
        elif row["is_new"]:
            s, r = "new", "First seen this month — monitor next month"
        elif any(ke in k for ke in known_keep):
            s, r = "keep", "Established, non-redundant"
        else:
            s, r = "rev", "Verify it's still actively used"
        statuses.append(s)
        reasons.append(r)

    agg["status"] = statuses
    agg["reason"] = reasons
    return (
        agg[["name_display", "per_occurrence", "months_seen", "monthly_cost", "status", "reason"]]
        .sort_values("monthly_cost", ascending=False)
        .reset_index(drop=True)
    )


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
        "❤️  Financial Health",
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
        raw = exp.groupby("Category")["Amount"].sum()
        raw = raw[raw > 0]
        raw_df = raw.reset_index()
        raw_df["Group"] = raw_df["Category"].map(CATEGORY_GROUPS).fillna("Other")
        group_totals = raw_df.groupby("Group")["Amount"].sum().reset_index()
        breakdowns = (
            raw_df.sort_values("Amount", ascending=False)
            .groupby("Group")
            .apply(lambda g: "<br>".join(
                f"  {r['Category']}: S${r['Amount']:,.0f}" for _, r in g.iterrows()
            ))
            .reset_index(name="Breakdown")
        )
        group_totals = group_totals.merge(breakdowns, on="Group")
        group_totals = group_totals.sort_values("Amount", ascending=False)
        group_totals["Color"] = group_totals["Group"].map(GROUP_COLORS).fillna("#546E7A")
        fig2 = go.Figure(go.Pie(
            labels=group_totals["Group"],
            values=group_totals["Amount"],
            customdata=group_totals["Breakdown"],
            marker_colors=group_totals["Color"],
            hole=0.52,
            textposition="inside",
            textinfo="percent",
            hovertemplate="<b>%{label}</b>  S$%{value:,.0f}<br><br>%{customdata}<extra></extra>",
        ))
        fig2.update_layout(
            **base_layout(height=300),
            legend=dict(orientation="v", x=1.02, y=0.5, font_size=11),
        )
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
    food_mo  = exp_all[exp_all["Category"] == "Food & Dining"]["Amount"].sum() / N_MONTHS
    shop_mo  = exp_all[exp_all["Category"] == "Shopping"]["Amount"].sum() / N_MONTHS
    # Compute sub_cuts from live data — only truly redundant monthly subs, not one-offs
    _fc_months = MONTHS[-2:] if len(MONTHS) >= 2 else MONTHS
    _fc_subs   = exp_all[(exp_all["Category"] == "Subscriptions") & (exp_all["Month"].isin(_fc_months))]
    _fc_map    = {r["Description"].strip().lower(): r["Amount"] for _, r in _fc_subs.iterrows()}
    _fc_disp   = {r["Description"].strip().lower(): r["Description"].strip() for _, r in _fc_subs.iterrows()}
    _cut_keys  = {"chatgpt", "gemini", "spotify", "disney+"}
    sub_cuts   = sum(v for k, v in _fc_map.items() if k in _cut_keys)
    _cut_label = ", ".join(_fc_disp[k] for k in _cut_keys if k in _fc_map)
    opt_cut    = sub_cuts + food_mo * 0.15 + shop_mo * 0.15

    f1, f2, f3 = st.columns(3)
    scenarios = [
        (f1, "Current Trajectory",  avg_exp,            "#004D40",
         "Maintaining current habits"),
        (f2, "Cut Redundant Subs",  avg_exp - sub_cuts, "#00897B",
         f"Cancel {_cut_label} — S${sub_cuts:.0f}/month saved"),
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
    st.markdown('<div class="page-title">Smart Insights</div>', unsafe_allow_html=True)
    st.markdown(
        f'<div class="page-subtitle">{selected_month} · '
        f'Graded from your actual spending data</div>',
        unsafe_allow_html=True
    )

    # ── Data prep ─────────────────────────────────────────────────────────────
    avg_inc_mo   = inc_all["Amount"].sum() / N_MONTHS
    avg_exp_mo   = exp_all["Amount"].sum() / N_MONTHS
    avg_rate     = (avg_inc_mo - avg_exp_mo) / avg_inc_mo * 100 if avg_inc_mo > 0 else 0
    food_mo      = exp_all[exp_all["Category"] == "Food & Dining"]["Amount"].sum() / N_MONTHS
    lifestyle_mo = exp_all[exp_all["Category"].isin(["Shopping", "Entertainment"])]["Amount"].sum() / N_MONTHS
    transport_mo = exp_all[exp_all["Category"] == "Transport"]["Amount"].sum() / N_MONTHS
    sub_audit_df = live_subscription_audit(exp_all, MONTHS)
    sub_mo_total = sub_audit_df["monthly_cost"].sum() if not sub_audit_df.empty else 0
    cut_subs     = sub_audit_df[sub_audit_df["status"] == "cut"] if not sub_audit_df.empty else pd.DataFrame()
    n_redundant  = len(cut_subs)

    rising_cats = []
    if len(MONTHS) >= 3:
        for cat in exp_all["Category"].unique():
            vals = [
                exp_all[(exp_all["Month"] == m) & (exp_all["Category"] == cat)]["Amount"].sum()
                for m in MONTHS[-3:]
            ]
            if all(vals[i] < vals[i + 1] for i in range(2)) and vals[-1] > 30:
                rising_cats.append((cat, vals))

    # ── Grade each area ───────────────────────────────────────────────────────
    # Savings Rate
    if avg_rate >= 35:   sr_score = 90
    elif avg_rate >= 25: sr_score = 78
    elif avg_rate >= 15: sr_score = 58
    elif avg_rate >= 5:  sr_score = 35
    else:                sr_score = 10
    sr_verdict = (
        f"{avg_rate:.0f}% — excellent, well above SG avg" if avg_rate >= 30 else
        f"{avg_rate:.0f}% — good, above SG average"       if avg_rate >= 20 else
        f"{avg_rate:.0f}% — below 20% target"             if avg_rate >= 10 else
        f"{avg_rate:.0f}% — low, review spending"
    )
    sr_letter, sr_color, _ = _grade_letter(sr_score)

    # Subscriptions
    if   n_redundant == 0 and sub_mo_total < 80:  sub_score = 90
    elif n_redundant == 0 and sub_mo_total < 150:  sub_score = 72
    elif n_redundant == 1:                          sub_score = 48
    else:                                           sub_score = 28
    sub_verdict = (
        f"{n_redundant} redundant sub{'s' if n_redundant != 1 else ''} detected" if n_redundant > 0 else
        f"S${sub_mo_total:.0f}/mo — lean and clean"    if sub_mo_total < 100 else
        f"S${sub_mo_total:.0f}/mo — worth a review"
    )
    sub_letter, sub_color, _ = _grade_letter(sub_score)

    # Spend Trend
    n_rising = len(rising_cats)
    if   n_rising == 0: trend_score = 90
    elif n_rising == 1: trend_score = 70
    elif n_rising == 2: trend_score = 48
    else:               trend_score = 25
    trend_verdict = (
        "Spending stable across all categories"        if n_rising == 0 else
        f"{rising_cats[0][0]} rising 3 months in a row" if n_rising == 1 else
        f"{n_rising} categories rising consistently"
    )
    trend_letter, trend_color, _ = _grade_letter(trend_score)

    # Food & Dining
    if   food_mo < 300: food_score = 90
    elif food_mo < 400: food_score = 72
    elif food_mo < 500: food_score = 50
    elif food_mo < 600: food_score = 30
    else:               food_score = 10
    food_verdict = (
        f"S${food_mo:.0f}/mo — under SG low benchmark" if food_mo < 300 else
        f"S${food_mo:.0f}/mo — within SG range"        if food_mo < 400 else
        f"S${food_mo:.0f}/mo — above SG median"
    )
    food_letter, food_color, _ = _grade_letter(food_score)

    # Lifestyle (Shopping + Entertainment)
    if   lifestyle_mo < 200: ls_score = 90
    elif lifestyle_mo < 400: ls_score = 72
    elif lifestyle_mo < 600: ls_score = 50
    elif lifestyle_mo < 800: ls_score = 30
    else:                    ls_score = 10
    ls_verdict = (
        f"S${lifestyle_mo:.0f}/mo — well controlled" if lifestyle_mo < 300 else
        f"S${lifestyle_mo:.0f}/mo — within range"    if lifestyle_mo < 500 else
        f"S${lifestyle_mo:.0f}/mo — consider a ceiling"
    )
    ls_letter, ls_color, _ = _grade_letter(ls_score)

    # ── Report Card ──────────────────────────────────────────────────────────
    st.markdown('<div class="section-title">📊 Financial Report Card</div>', unsafe_allow_html=True)
    gc1, gc2, gc3, gc4, gc5 = st.columns(5)
    for col, (area, letter, color, verdict, score) in zip(
        [gc1, gc2, gc3, gc4, gc5],
        [
            ("Savings Rate",  sr_letter,    sr_color,    sr_verdict,    sr_score),
            ("Subscriptions", sub_letter,   sub_color,   sub_verdict,   sub_score),
            ("Spend Trend",   trend_letter, trend_color, trend_verdict, trend_score),
            ("Food & Dining", food_letter,  food_color,  food_verdict,  food_score),
            ("Lifestyle",     ls_letter,    ls_color,    ls_verdict,    ls_score),
        ],
    ):
        col.markdown(_grade_card_html(area, letter, color, verdict, score), unsafe_allow_html=True)

    # ── Action Queue ─────────────────────────────────────────────────────────
    st.markdown('<div class="section-title" style="margin-top:28px">🎯 Action Queue</div>',
                unsafe_allow_html=True)

    actions = []

    # 1. Redundant subscriptions → HIGH
    if not cut_subs.empty:
        reasons_str = " ".join(
            f"<b>{r['name_display']}</b>: {r['reason']}." for _, r in cut_subs.iterrows()
        )
        cut_names   = " + ".join(cut_subs["name_display"].tolist())
        cut_total   = cut_subs["monthly_cost"].sum()
        actions.append((
            "high", "Subscriptions",
            f"Cancel {len(cut_subs)} redundant subscription{'s' if len(cut_subs) > 1 else ''} — zero lifestyle change",
            reasons_str + " Cancelling takes under 10 minutes.",
            f"Cancel {cut_names} today",
            cut_total * 12,
        ))

    # 2. Rising spend categories → MED
    for cat, vals in rising_cats:
        rise = vals[-1] - vals[0]
        actions.append((
            "med", "Spend Trend",
            f"{cat} has risen 3 months in a row",
            f"S${vals[0]:,.0f} → S${vals[1]:,.0f} → S${vals[2]:,.0f}. New habit, price increase, or scope creep?",
            f"Set a monthly ceiling for {cat}",
            rise * 12,
        ))

    # 3. Food over SG median → MED
    if food_mo > 400:
        saving = food_mo - 380
        actions.append((
            "med", "Food & Dining",
            f"Food & Dining averaging S${food_mo:.0f}/mo — above SG median",
            "SG median for a single person is S$300–400/mo. Travel months inflate this — tag travel meals as 'Travel' to see your true home baseline.",
            "Set S$380/mo food budget; tag travel dining separately",
            saving * 12,
        ))

    # 4. Over-budget vs average for the selected month → HIGH / MED
    if selected_month != "All Time":
        cat_curr = exp.groupby("Category")["Amount"].sum().to_dict()
        cat_avg  = (exp_all.groupby("Category")["Amount"].sum() / N_MONTHS).to_dict()
        for cat, curr in sorted(cat_curr.items(), key=lambda x: -x[1]):
            avg = cat_avg.get(cat, 0)
            if avg > 0 and curr > avg * 1.3 and curr - avg > 50:
                if any(cat == rc[0] for rc in rising_cats):
                    continue
                over = curr - avg
                actions.append((
                    "high" if over > 200 else "med", "This Month",
                    f"{cat} is {(curr / avg - 1) * 100:.0f}% above your monthly average",
                    f"S${curr:,.0f} in {selected_month} vs your S${avg:,.0f} average — S${over:,.0f} extra. One-off or new habit?",
                    f"Review {cat} transactions for {selected_month}",
                    over * 12,
                ))

    # 5. Bank yield optimisation → INFO
    surplus_mo = avg_inc_mo * (avg_rate / 100)
    if surplus_mo > 500:
        actions.append((
            "info", "Savings",
            f"S${surplus_mo:,.0f}/mo surplus — is it earning 3%+?",
            f"Your {avg_rate:.0f}% savings rate generates ~S${surplus_mo:,.0f}/mo. Large idle balances in standard accounts lose to inflation. "
            "OCBC 360, Maribank (2.5%), CIMB FastSaver (~3%) all offer better rates when salary-credited.",
            "Confirm idle cash is in a high-yield account",
            0,
        ))

    # 6. Transport good news → GOOD
    if 0 < transport_mo < 100:
        sg_mid = 150
        actions.append((
            "good", "Lifestyle",
            f"Transport S${transport_mo:.0f}/mo — saving S${(sg_mid - transport_mo) * 12:.0f}/yr vs SG average",
            f"SG benchmark is S$100–200/mo. Bus/MRT habit is paying off — no action needed.",
            "No action needed — keep it up",
            -((sg_mid - transport_mo) * 12),
        ))

    # 7. Strong savings rate good news → GOOD
    if avg_rate >= 30:
        actions.append((
            "good", "Savings Rate",
            f"{avg_rate:.0f}% savings rate — top quartile for Singapore",
            f"SG median is 15–20%. At this pace you're accumulating S${surplus_mo * 12:,.0f}/yr.",
            "Stay consistent — consider increasing IBKR DCA if surplus is idle",
            0,
        ))

    _priority_order = {"high": 0, "med": 1, "info": 2, "good": 3}
    actions.sort(key=lambda a: (_priority_order.get(a[0], 9), -(a[5] if a[5] > 0 else 0)))

    recoverable = sum(a[5] for a in actions if a[5] > 0)
    if recoverable > 0:
        st.caption(f"S${recoverable:,.0f}/yr available to recover from the actions below.")

    for priority, area, title, detail, action_text, impact in actions:
        st.markdown(
            _action_card_html(priority, area, title, detail, action_text, impact),
            unsafe_allow_html=True,
        )

    # ── Subscription Audit (live) ─────────────────────────────────────────────
    st.markdown('<div class="section-title" style="margin-top:28px">🔍 Subscription Audit</div>',
                unsafe_allow_html=True)
    st.caption("Live from your transactions — pulled from the Subscriptions category in your sheet.")

    if sub_audit_df.empty:
        st.info("No subscription transactions found in your data.")
    else:
        pill_cls = {"cut": "pill-cut", "keep": "pill-keep", "rev": "pill-rev", "new": "pill-new"}
        pill_lbl = {"cut": "❌ Cut", "keep": "✅ Keep", "rev": "🟡 Review", "new": "🆕 New"}

        hdr = st.columns([3, 1, 1, 1, 4])
        for col, lbl in zip(hdr, ["Subscription", "S$/occurrence", "Months seen", "Action", "Reason"]):
            col.markdown(small_label(lbl), unsafe_allow_html=True)
        st.markdown("<hr style='border-color:#DDE9E7;margin:4px 0 8px'>", unsafe_allow_html=True)

        for _, row in sub_audit_df.iterrows():
            c0, c1, c2, c3, c4 = st.columns([3, 1, 1, 1, 4])
            c0.markdown(f"**{row['name_display']}**")
            c1.markdown(f"S${row['per_occurrence']:.2f}")
            c2.markdown(f"{int(row['months_seen'])}")
            status = row["status"]
            pill_c = pill_cls.get(status, "pill-rev")
            pill_t = pill_lbl.get(status, "🟡 Review")
            c3.markdown(
                f'<span class="pill {pill_c}">{pill_t}</span>',
                unsafe_allow_html=True,
            )
            c4.caption(row["reason"])

        cut_total = sub_audit_df[sub_audit_df["status"] == "cut"]["monthly_cost"].sum()
        if cut_total > 0:
            st.success(
                f"💡 Cancel redundant subscriptions → save **S${cut_total:.0f}/month** "
                f"(**S${cut_total * 12:.0f}/year**) with zero lifestyle change."
            )


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
        '<div class="page-subtitle">Live from your Google Sheet</div>',
        unsafe_allow_html=True
    )

    nw_df = load_networth()

    if nw_df.empty:
        st.warning("No net worth data found. Check that the Networth sheet is shared and the GID is correct.")
        st.stop()

    BANK_COLS = [c for c in ["DBS","Maribank","UOB","OCBC","Citi","Chocolate"] if c in nw_df.columns]
    INV_COLS  = [c for c in ["IBKR"] if c in nw_df.columns]
    CPF_COLS  = [c for c in ["CPF (OA)","CPF (SA)","CPF (MA)"] if c in nw_df.columns]
    WIFE_COL  = "Wife savings cash" if "Wife savings cash" in nw_df.columns else None
    CASH_COL  = "Liquid Cash" if "Liquid Cash" in nw_df.columns else None
    NW_COL    = "Total networth" if "Total networth" in nw_df.columns else None

    nw_df["_Banking"]     = nw_df[BANK_COLS].sum(axis=1) if BANK_COLS else 0
    nw_df["_Investments"] = nw_df[INV_COLS].sum(axis=1)  if INV_COLS  else 0
    nw_df["_CPF"]         = nw_df[CPF_COLS].sum(axis=1)  if CPF_COLS  else 0
    nw_df["_Family"]      = nw_df[WIFE_COL] if WIFE_COL else 0
    nw_df["_Cash"]        = nw_df[CASH_COL] if CASH_COL else 0
    if NW_COL:
        nw_df["_NW"] = nw_df[NW_COL]
    else:
        nw_df["_NW"] = (nw_df["_Banking"] + nw_df["_Investments"]
                        + nw_df["_CPF"] + nw_df["_Family"])

    has_data = len(nw_df) > 0 and nw_df["_NW"].sum() > 0

    if not has_data:
        st.info("The Networth sheet loaded but has no data yet. Add entries to see your tracker.")
    else:
        # ── KPI row: latest month ─────────────────────────────────────────────
        latest = nw_df.iloc[-1]
        prev   = nw_df.iloc[-2] if len(nw_df) >= 2 else None

        def nw_delta(key):
            if prev is None:
                return None
            return latest[key] - prev[key]

        st.markdown(
            f"<div style='font-size:12px;font-weight:600;color:#7A9E98;"
            f"letter-spacing:1.2px;text-transform:uppercase;margin-bottom:12px'>"
            f"Latest snapshot · {latest['Month']}</div>",
            unsafe_allow_html=True
        )

        k1, k2, k3, k4, k5, k6 = st.columns(6)
        k1.metric("Total Net Worth",
                  f"S${latest['_NW']:,.0f}",
                  f"S${nw_delta('_NW'):+,.0f} vs {prev['Month']}" if prev is not None else None)
        k2.metric("Banking",
                  f"S${latest['_Banking']:,.0f}",
                  f"S${nw_delta('_Banking'):+,.0f}" if prev is not None else None)
        k3.metric("Investments (IBKR)",
                  f"S${latest['_Investments']:,.0f}",
                  f"S${nw_delta('_Investments'):+,.0f}" if prev is not None else None)
        k4.metric("CPF Total",
                  f"S${latest['_CPF']:,.0f}",
                  f"S${nw_delta('_CPF'):+,.0f}" if prev is not None else None)
        if WIFE_COL:
            k5.metric("Wife Savings",
                      f"S${latest['_Family']:,.0f}",
                      f"S${nw_delta('_Family'):+,.0f}" if prev is not None else None)
        k6.metric("Liquid (non-CPF)",
                  f"S${latest['_Cash']:,.0f}",
                  f"S${nw_delta('_Cash'):+,.0f}" if prev is not None else None)

        st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)

        # ── Net Worth over time ───────────────────────────────────────────────
        col_nw, col_bk = st.columns([1.4, 1])

        with col_nw:
            st.markdown('<div class="section-title">Net Worth Over Time</div>', unsafe_allow_html=True)
            fig_nw = go.Figure()
            fig_nw.add_scatter(
                x=nw_df["Month"], y=nw_df["_NW"],
                name="Total Net Worth", mode="lines+markers",
                line=dict(color="#E65100", width=3),
                marker=dict(size=9, line=dict(color="white", width=2)),
                fill="tozeroy", fillcolor="rgba(230,81,0,0.06)",
                hovertemplate="<b>%{x}</b><br>S$%{y:,.0f}<extra></extra>",
            )
            fig_nw.add_scatter(
                x=nw_df["Month"], y=nw_df["_Banking"],
                name="Banking", mode="lines+markers",
                line=dict(color="#004D40", width=2),
                marker=dict(size=7, line=dict(color="white", width=1.5)),
                hovertemplate="<b>%{x}</b> Banking: S$%{y:,.0f}<extra></extra>",
            )
            fig_nw.add_scatter(
                x=nw_df["Month"], y=nw_df["_CPF"],
                name="CPF", mode="lines+markers",
                line=dict(color="#0D47A1", width=2, dash="dot"),
                marker=dict(size=7, symbol="diamond", line=dict(color="white", width=1.5)),
                hovertemplate="<b>%{x}</b> CPF: S$%{y:,.0f}<extra></extra>",
            )
            if nw_df["_Investments"].sum() > 0:
                fig_nw.add_scatter(
                    x=nw_df["Month"], y=nw_df["_Investments"],
                    name="IBKR", mode="lines+markers",
                    line=dict(color="#00897B", width=2),
                    marker=dict(size=7, symbol="square", line=dict(color="white", width=1.5)),
                    hovertemplate="<b>%{x}</b> IBKR: S$%{y:,.0f}<extra></extra>",
                )
            if WIFE_COL and nw_df["_Family"].sum() > 0:
                fig_nw.add_scatter(
                    x=nw_df["Month"], y=nw_df["_Family"],
                    name="Wife Savings", mode="lines+markers",
                    line=dict(color="#9C27B0", width=2, dash="dash"),
                    marker=dict(size=7, symbol="star", line=dict(color="white", width=1.5)),
                    hovertemplate="<b>%{x}</b> Wife Savings: S$%{y:,.0f}<extra></extra>",
                )
            fig_nw.update_layout(
                **base_layout(height=360),
                yaxis=dict(**styled_yaxis(), tickformat=",.0f"),
                xaxis=styled_xaxis(),
                legend=dict(orientation="h", y=1.1, x=0, font_size=11),
                hovermode="x unified",
            )
            st.plotly_chart(fig_nw, use_container_width=True)

        with col_bk:
            st.markdown('<div class="section-title">Breakdown by Type</div>', unsafe_allow_html=True)
            latest_breakdown = {
                "Banking":      latest["_Banking"],
                "CPF":          latest["_CPF"],
                "Investments":  latest["_Investments"],
                "Wife Savings": latest["_Family"],
            }
            bd_df = pd.DataFrame([
                {"Type": k, "Amount": v}
                for k, v in latest_breakdown.items() if v > 0
            ])
            if not bd_df.empty:
                fig_pie = px.pie(
                    bd_df, values="Amount", names="Type",
                    color_discrete_sequence=["#004D40","#0D47A1","#00897B","#9C27B0"],
                    hole=0.52,
                )
                fig_pie.update_layout(
                    **base_layout(height=360),
                    legend=dict(orientation="v", x=1.02, y=0.5, font_size=11),
                )
                fig_pie.update_traces(
                    textposition="inside", textinfo="percent",
                    hovertemplate="<b>%{label}</b><br>S$%{value:,.0f}<extra></extra>",
                )
                st.plotly_chart(fig_pie, use_container_width=True)

        # ── Stacked breakdown over time ───────────────────────────────────────
        st.markdown('<div class="section-title">Asset Breakdown Over Time</div>', unsafe_allow_html=True)
        fig_stack = go.Figure()
        stack_layers = [
            ("Banking",       "_Banking",     "#004D40"),
            ("Investments",   "_Investments", "#00897B"),
            ("CPF",           "_CPF",         "#0D47A1"),
            ("Wife Savings",  "_Family",      "#9C27B0"),
        ]
        for label, col_key, color in stack_layers:
            if nw_df[col_key].sum() == 0:
                continue
            fig_stack.add_bar(
                x=nw_df["Month"], y=nw_df[col_key],
                name=label, marker_color=color, marker_line_width=0, opacity=0.85,
                hovertemplate=f"<b>%{{x}}</b> {label}: S$%{{y:,.0f}}<extra></extra>",
            )
        fig_stack.update_layout(
            **base_layout(height=300),
            barmode="stack",
            yaxis=dict(**styled_yaxis(), tickformat=",.0f"),
            xaxis=styled_xaxis(),
            legend=dict(orientation="h", y=1.1, x=0, font_size=11),
            hovermode="x unified",
            bargap=0.3,
        )
        st.plotly_chart(fig_stack, use_container_width=True)

        # ── SG Peer Comparison ───────────────────────────────────────────────────
        st.markdown(
            '<div class="section-title">SG Peer Comparison · Married Household · Ages 25–35</div>',
            unsafe_allow_html=True,
        )

        # Reference benchmarks
        # ── Net Worth (married household, excl. property) ──────────────────────
        # No official SG age-stratified NW table exists. Estimates derived from:
        #   • UBS Global Wealth Databook 2024 (median adult NW ≈ S$134K, all ages)
        #     scaled to household (×2) for 25–35 cohort
        #   • MOF Occasional Paper Feb 2026 / SingStat HES 2023 (avg HH NW S$1.755M,
        #     all ages incl. property → stripped back for young, non-property cohort)
        #   • Financial Horse / SingSaver planning benchmarks 2026
        # ── CPF (individual, one person) ───────────────────────────────────────
        # Official CPF Board data (cpf.gov.sg, balances as at 31 Dec 2025):
        #   Ages 25–30: 271K members, S$16.01B total → avg S$59,100/person
        #   Ages 30–35: 327K members, S$37.42B total → avg S$114,400/person
        #   Ages 35–40: 337K members, S$54.38B total → avg S$161,400/person
        # Median < average (right-skewed dist.); est. median ~80–85% of average.
        # ── Cash / Investments (household) ─────────────────────────────────────
        # OCBC Financial Wellness Index 2024; SingStat personal savings-rate data
        # (10-yr avg 31.1%); DBS Gen-Z/Millennial study Jun 2024 (2M customers).
        BM = dict(
            nw_p50      = 250_000,   # Household median NW excl. property (25–35)
            nw_p75      = 480_000,   # 75th percentile household NW
            nw_p90      = 820_000,   # 90th percentile household NW
            bank_p50    =  70_000,   # Median household cash/bank savings
            bank_p75    = 140_000,   # 75th percentile household cash
            inv_p50     =  30_000,   # Median household investments (equities/ETFs)
            inv_p75     =  80_000,   # 75th percentile household investments
            cpf_ind_avg =114_400,    # Official avg individual CPF, ages 30–35 (Dec 2025)
            cpf_ind_p50 =  95_000,   # Est. median individual CPF (avg × ~0.83)
            cpf_ind_p75 = 160_000,   # Est. 75th-percentile individual CPF
            sav_rate_avg = 31.5,     # SG avg household savings rate (SingStat 2025)
            sav_rate_top = 40.0,     # Top-saver threshold
        )

        u_nw   = float(latest["_NW"])
        u_bank = float(latest["_Banking"])
        u_inv  = float(latest["_Investments"])
        u_cpf  = float(latest["_CPF"])
        u_fam  = float(latest["_Family"]) if WIFE_COL else 0
        u_cash_total = u_bank + u_fam

        avg_mo_exp_bm = exp_all["Amount"].sum() / max(len(MONTHS), 1)
        avg_mo_inc_bm = inc_all["Amount"].sum() / max(len(MONTHS), 1)
        sav_rate_bm   = ((avg_mo_inc_bm - avg_mo_exp_bm) / avg_mo_inc_bm * 100
                         if avg_mo_inc_bm > 0 else 0)

        # Determine NW percentile tier
        if u_nw >= BM["nw_p90"]:
            nw_tier, nw_pct, nw_badge_bg, nw_badge_fg = "Top 10%",  92, "#DCFCE7", "#166534"
        elif u_nw >= BM["nw_p75"]:
            nw_tier, nw_pct, nw_badge_bg, nw_badge_fg = "Top 25%",  78, "#D1FAE5", "#065F46"
        elif u_nw >= BM["nw_p50"]:
            nw_tier, nw_pct, nw_badge_bg, nw_badge_fg = "Above Median", 62, "#FEF3C7", "#92400E"
        else:
            nw_tier, nw_pct, nw_badge_bg, nw_badge_fg = "Below Median", 35, "#FEE2E2", "#991B1B"

        # ── Percentile banner ─────────────────────────────────────────────────
        st.markdown(f"""
        <div style="background:linear-gradient(135deg,#004D40 0%,#00695C 100%);
                    border-radius:18px;padding:24px 32px;margin-bottom:20px;
                    display:flex;align-items:center;justify-content:space-between;
                    box-shadow:0 4px 20px rgba(0,77,64,0.25)">
          <div>
            <div style="font-size:11px;font-weight:700;letter-spacing:2px;
                        text-transform:uppercase;color:#80CBC4;margin-bottom:8px">
              Household Net Worth · vs SG Married Peers (25–35)
            </div>
            <div style="font-family:'DM Serif Display',serif;font-size:40px;
                        color:#FFFFFF;line-height:1">S${u_nw:,.0f}</div>
            <div style="font-size:12px;color:#B2DFDB;margin-top:6px">
              Banking · Investments · CPF · Wife Savings · Excl. property
            </div>
          </div>
          <div style="text-align:right;flex-shrink:0;margin-left:24px">
            <div style="font-family:'DM Serif Display',serif;font-size:56px;
                        color:#FFFFFF;line-height:1">{nw_pct}<span style="font-size:28px">th</span></div>
            <div style="background:{nw_badge_bg};color:{nw_badge_fg};border-radius:100px;
                        padding:6px 20px;font-size:12px;font-weight:700;
                        display:inline-block;margin-top:6px;letter-spacing:0.3px">
              Percentile · {nw_tier}
            </div>
          </div>
        </div>
        """, unsafe_allow_html=True)

        # ── Grouped comparison bar chart ──────────────────────────────────────
        comp_cats = ["Total Net Worth", "Banking & Cash", "Investments (IBKR)", "CPF (individual)"]
        user_vals = [u_nw,    u_cash_total, u_inv,           u_cpf]
        med_vals  = [BM["nw_p50"], BM["bank_p50"], BM["inv_p50"], BM["cpf_ind_p50"]]
        p75_vals  = [BM["nw_p75"], BM["bank_p75"], BM["inv_p75"], BM["cpf_ind_p75"]]

        fig_comp = go.Figure()
        fig_comp.add_bar(
            name="SG Median (P50)", x=comp_cats, y=med_vals,
            marker_color="#B2DFDB", marker_line_width=0, opacity=0.9,
            hovertemplate="<b>%{x}</b><br>SG Median: S$%{y:,.0f}<extra></extra>",
        )
        fig_comp.add_bar(
            name="SG Top 25% (P75)", x=comp_cats, y=p75_vals,
            marker_color="#26A69A", marker_line_width=0, opacity=0.9,
            hovertemplate="<b>%{x}</b><br>Top 25%: S$%{y:,.0f}<extra></extra>",
        )
        fig_comp.add_bar(
            name="You", x=comp_cats, y=user_vals,
            marker_color="#E65100", marker_line_width=0, opacity=0.95,
            hovertemplate="<b>%{x}</b><br>Yours: S$%{y:,.0f}<extra></extra>",
        )
        fig_comp.update_layout(
            **base_layout(height=320),
            barmode="group",
            yaxis=dict(**styled_yaxis(), tickformat=",.0f"),
            xaxis=styled_xaxis(),
            legend=dict(orientation="h", y=1.12, x=0, font_size=11),
            hovermode="x unified",
            bargap=0.22, bargroupgap=0.06,
        )
        st.plotly_chart(fig_comp, use_container_width=True)

        # ── Financial milestones ──────────────────────────────────────────────
        st.markdown('<div class="section-title">Financial Milestones</div>', unsafe_allow_html=True)

        milestones = [
            (u_cash_total >= avg_mo_exp_bm * 3,
             "3-month emergency fund",
             f"S${u_cash_total:,.0f} available vs S${avg_mo_exp_bm*3:,.0f} target"),
            (u_cash_total >= avg_mo_exp_bm * 6,
             "6-month emergency fund (MAS guideline)",
             f"Covers {u_cash_total/avg_mo_exp_bm:.1f} months of expenses"),
            (sav_rate_bm >= BM["sav_rate_avg"],
             f"Savings rate ≥ {BM['sav_rate_avg']:.0f}% (SG household average)",
             f"Your rate: {sav_rate_bm:.1f}%"),
            (sav_rate_bm >= BM["sav_rate_top"],
             f"Savings rate ≥ {BM['sav_rate_top']:.0f}% (top saver tier)",
             f"Your rate: {sav_rate_bm:.1f}%"),
            (u_inv > 0,
             "Started investing (ETF / stocks portfolio)",
             f"S${u_inv:,.0f} in IBKR"),
            (u_inv >= BM["inv_p75"],
             f"Investments ≥ S${BM['inv_p75']:,} (SG Top 25%)",
             f"S${u_inv:,.0f} — above the 75th-percentile benchmark"),
            (u_cpf >= 100_000,
             "Individual CPF ≥ S$100,000",
             f"S${u_cpf:,.0f} across OA, SA & MediSave"),
            (u_cpf >= BM["cpf_ind_p75"],
             f"CPF in top 25% for this age group (≥ S${BM['cpf_ind_p75']:,})",
             f"S${u_cpf:,.0f} total CPF"),
            (u_nw >= BM["nw_p50"],
             "Net worth above SG peer median",
             f"S${u_nw:,.0f} vs S${BM['nw_p50']:,} median"),
            (u_nw >= BM["nw_p75"],
             "Net worth in top 25% of SG peers",
             f"S${u_nw:,.0f} vs S${BM['nw_p75']:,} threshold"),
        ]

        mc1, mc2 = st.columns(2)
        for i, (achieved, label, detail) in enumerate(milestones):
            col = mc1 if i % 2 == 0 else mc2
            icon  = "✅" if achieved else "⬜"
            color = "#166534" if achieved else "#7A9E98"
            bg    = "#DCFCE7" if achieved else "#F2F6F5"
            bdr   = "#A7F3D0" if achieved else "#DDE9E7"
            col.markdown(f"""
            <div style="background:{bg};border-radius:12px;padding:12px 16px;
                        margin-bottom:10px;border:1px solid {bdr}">
              <div style="font-size:13px;font-weight:600;color:{color};margin-bottom:3px">
                {icon}&nbsp; {label}
              </div>
              <div style="font-size:11px;color:#7A9E98">{detail}</div>
            </div>
            """, unsafe_allow_html=True)

        # ── CPF vs expected for age group ─────────────────────────────────────
        st.markdown(
            '<div class="section-title">CPF vs Expected · Age 25–35 (per person)</div>',
            unsafe_allow_html=True,
        )
        cpf_bm_rows = [
            ("OA · Ordinary Account", "CPF (OA)", 60_000, 100_000,
             "2.5% p.a. interest. Used for housing & investments. "
             "Median for working 25–35-yr-old: S$60K–100K."),
            ("SA · Special Account",  "CPF (SA)", 18_000,  42_000,
             "4% p.a. interest. Earmarked for retirement. "
             "Median for 25–35: S$18K–42K."),
            ("MA · MediSave",         "CPF (MA)", 26_000,  50_000,
             "4% p.a. interest. Healthcare savings. "
             "Basic Healthcare Sum 2026: S$79,000."),
        ]
        cpf_cols_out = st.columns(3)
        for col_w, (lbl, col_key, lo, hi, note) in zip(cpf_cols_out, cpf_bm_rows):
            if col_key not in nw_df.columns:
                continue
            val = float(latest[col_key])
            pct = min(val / hi * 100, 100) if hi else 0
            if val >= hi:
                c_bar, c_status = "#00BFA5", "✅ Above benchmark"
            elif val >= lo:
                c_bar, c_status = "#26A69A", "✅ Within benchmark"
            elif val >= lo * 0.7:
                c_bar, c_status = "#FF8F00", "⚠️ Slightly below"
            else:
                c_bar, c_status = "#EF5350", "🔴 Below benchmark"
            col_w.markdown(f"""
            <div style="background:#FFFFFF;border-radius:14px;padding:18px 20px;
                        border:1px solid #DDE9E7;
                        box-shadow:0 2px 10px rgba(0,77,64,0.06);height:100%">
              <div style="font-size:10px;font-weight:700;letter-spacing:1.4px;
                          text-transform:uppercase;color:#7A9E98;margin-bottom:6px">
                {lbl}
              </div>
              <div style="font-family:'DM Serif Display',serif;font-size:28px;
                          color:#1C3A35;line-height:1.1">S${val:,.0f}</div>
              <div style="position:relative;height:7px;background:#EFF4F3;
                          border-radius:100px;margin:10px 0 4px">
                <div style="width:{pct:.0f}%;height:100%;background:{c_bar};
                            border-radius:100px"></div>
              </div>
              <div style="font-size:11px;color:{c_bar};font-weight:600;
                          margin-bottom:8px">{c_status}</div>
              <div style="font-size:11px;color:#7A9E98;margin-bottom:4px">
                Benchmark: S${lo:,} – S${hi:,}
              </div>
              <div style="font-size:11px;color:#556B67;line-height:1.65">{note}</div>
            </div>
            """, unsafe_allow_html=True)

        # ── Savings rate context ──────────────────────────────────────────────
        st.markdown("<div style='height:4px'></div>", unsafe_allow_html=True)
        sr1, sr2, sr3 = st.columns(3)
        sr1.metric("Your Savings Rate",    f"{sav_rate_bm:.1f}%",
                   f"+{sav_rate_bm - BM['sav_rate_avg']:.1f}pp vs SG avg" if sav_rate_bm >= BM["sav_rate_avg"] else f"{sav_rate_bm - BM['sav_rate_avg']:.1f}pp vs SG avg")
        sr2.metric("SG Household Average", f"{BM['sav_rate_avg']:.0f}%", "SingStat 2025")
        sr3.metric("Median SG Peer NW",    f"S${BM['nw_p50']:,}", "Married couple 25–35, excl. property")

        # ── Benchmark source note ─────────────────────────────────────────────
        st.markdown("""
        <div style="background:#F2F6F5;border-radius:12px;padding:14px 18px;
                    margin-top:12px;border:1px solid #DDE9E7">
          <div style="font-size:11px;font-weight:700;letter-spacing:1.2px;
                      text-transform:uppercase;color:#7A9E98;margin-bottom:6px">
            📌 Benchmark Sources & Methodology
          </div>
          <div style="font-size:11px;color:#556B67;line-height:1.85">
            <b>Net worth percentiles:</b> UBS Global Wealth Databook 2024 individual estimates
            scaled to household level (×2) and adjusted for SG wealth distribution, excluding
            primary property. <b>Cash/investment benchmarks:</b> OCBC Financial Wellness Index
            2024 & SingStat Household Expenditure Survey 2023.
            <b>CPF benchmarks:</b> CPF Board Annual Report 2024 — median active-member balances
            for the 25–34 cohort based on standard contribution rates (20% employee +
            17% employer on median salary of S$6,338/mo for ages 30–34).
            <b>Savings rate:</b> SingStat Key Household Income Trends 2025 (SG average 31.5%).
            Note: official age-stratified NW percentile tables are not published by SingStat —
            these are informed estimates and should be treated as directional guides.
          </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)

        # ── Individual bank balances (latest month) ───────────────────────────
        if BANK_COLS:
            st.markdown('<div class="section-title">Bank Balances · Latest Month</div>', unsafe_allow_html=True)
            bank_data = [(c, latest[c]) for c in BANK_COLS if latest[c] > 0]
            if bank_data:
                bk_df = pd.DataFrame(bank_data, columns=["Account", "Balance"])
                bk_df = bk_df.sort_values("Balance", ascending=True)
                bk_df["label"] = bk_df["Balance"].apply(lambda x: f"S${x:,.0f}")
                fig_bk = px.bar(
                    bk_df, x="Balance", y="Account", orientation="h",
                    text="label", color="Balance",
                    color_continuous_scale=[[0,"#B2DFDB"],[1,"#004D40"]],
                )
                fig_bk.update_traces(textposition="outside", textfont_size=11, marker_line_width=0)
                fig_bk.update_layout(
                    **base_layout(height=max(200, len(bank_data) * 50),
                                  margin=dict(l=0, r=120, t=24, b=0)),
                    coloraxis_showscale=False, showlegend=False,
                    xaxis=dict(**styled_xaxis(), tickprefix="S$", title=""),
                    yaxis=dict(gridcolor="#EFF4F3", zeroline=False, title=""),
                )
                st.plotly_chart(fig_bk, use_container_width=True)

        # ── CPF breakdown ─────────────────────────────────────────────────────
        if CPF_COLS:
            st.markdown('<div class="section-title">CPF Accounts · Latest Month</div>', unsafe_allow_html=True)
            cpf_labels = {"CPF (OA)": "Ordinary (OA)", "CPF (SA)": "Special (SA)", "CPF (MA)": "MediSave (MA)"}
            c1, c2, c3 = st.columns(3)
            for col_w, cpf_col in zip([c1, c2, c3], CPF_COLS):
                delta_val = nw_delta(cpf_col) if prev is not None else None
                col_w.metric(
                    cpf_labels.get(cpf_col, cpf_col),
                    f"S${latest[cpf_col]:,.0f}",
                    f"S${delta_val:+,.0f}" if delta_val is not None else None,
                )

        # ── History table ─────────────────────────────────────────────────────
        st.markdown('<div class="section-title">Full History</div>', unsafe_allow_html=True)
        display_cols = (
            ["Month"] + BANK_COLS + INV_COLS + CPF_COLS
            + (["Wife savings cash"] if WIFE_COL else [])
            + (["Liquid Cash"] if CASH_COL else [])
            + (["Total networth"] if NW_COL else [])
        )
        display_cols = [c for c in display_cols if c in nw_df.columns]
        display_hist = nw_df[display_cols].copy().iloc[::-1].reset_index(drop=True)
        for c in display_cols[1:]:
            display_hist[c] = display_hist[c].apply(lambda x: f"S${x:,.0f}" if x > 0 else "—")
        st.dataframe(display_hist, width="stretch", hide_index=True)

        csv_nw = nw_df[display_cols].to_csv(index=False).encode("utf-8")
        st.download_button("⬇️ Export Net Worth as CSV", csv_nw, "net_worth.csv", "text/csv")


# ══════════════════════════════════════════════════════════════════════════════
# PAGE: FINANCIAL HEALTH
# ══════════════════════════════════════════════════════════════════════════════
elif page == "❤️  Financial Health":
    st.markdown('<div class="page-title">Financial Health</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="page-subtitle">'
        'Key financial ratios benchmarked against Monetary Authority of Singapore guidelines'
        '</div>',
        unsafe_allow_html=True,
    )

    # ── Data preparation ──────────────────────────────────────────────────────
    N_MONTHS_FH     = max(len(MONTHS), 1)
    avg_monthly_exp = exp_all["Amount"].sum() / N_MONTHS_FH
    avg_monthly_inc = inc_all["Amount"].sum() / N_MONTHS_FH
    avg_monthly_sav = avg_monthly_inc - avg_monthly_exp

    nw_fh = load_networth()
    if not nw_fh.empty:
        BANK_FH      = [c for c in ["DBS", "Maribank", "UOB", "OCBC", "Citi", "Chocolate"] if c in nw_fh.columns]
        nw_latest    = nw_fh.iloc[-1]
        banking_tot  = sum(float(nw_latest.get(c, 0) or 0) for c in BANK_FH)
        wife_savings = float(nw_latest.get("Wife savings cash", 0) or 0)
        # Use banking + wife savings as the true accessible cash pool.
        # "Liquid Cash" in the sheet is a derived subtotal (banking + IBKR + wife savings)
        # and must NOT be used here to avoid double-counting.
        ef_pool      = banking_tot + wife_savings
    else:
        ef_pool = None

    # Emergency Fund ratio
    if ef_pool is not None and avg_monthly_exp > 0:
        ef_val = ef_pool / avg_monthly_exp
        ef_status  = "good" if ef_val >= 6 else ("warn" if ef_val >= 3 else "bad")
        ef_pct_bar = min(ef_val / 9 * 100, 100)
        ef_target  = 6 / 9 * 100
        wife_note  = f" + wife savings S${wife_savings:,.0f}" if wife_savings > 0 else ""
        ef_detail  = (
            f"You have <b>S${ef_pool:,.0f}</b> in accessible savings "
            f"(banking S${banking_tot:,.0f}{wife_note}), "
            f"covering <b>{ef_val:.1f} months</b> of your average monthly expenses "
            f"of <b>S${avg_monthly_exp:,.0f}</b>."
        )
    else:
        ef_val, ef_pct_bar, ef_target = None, 0, 66.7
        ef_status = "na"
        ef_detail = (
            "Net worth data not available. Populate your Networth sheet to see this metric."
        )

    # Savings Ratio
    if avg_monthly_inc > 0:
        sav_val    = avg_monthly_sav / avg_monthly_inc * 100
        sav_status = "good" if sav_val >= 15 else ("warn" if sav_val >= 10 else "bad")
        sav_pct_bar = min(max(sav_val, 0) / 30 * 100, 100)
        sav_target  = 15 / 30 * 100
        sav_detail  = (
            f"Average monthly savings of <b>S${avg_monthly_sav:,.0f}</b> on average income "
            f"of <b>S${avg_monthly_inc:,.0f}</b> — a savings rate of <b>{sav_val:.1f}%</b>. "
            f"Note: your tracked income is take-home pay; gross income (pre-CPF) would yield "
            f"a slightly lower ratio."
        )
    else:
        sav_val, sav_pct_bar, sav_target = None, 0, 50
        sav_status = "na"
        sav_detail = "No income data found in your transactions."

    # Debt ratios — auto-detect by category name
    LOAN_KEYWORDS = ["loan", "mortgage", "debt", "repay", "installment", "instalment"]
    all_cats = exp_all["Category"].unique()
    loan_cats    = [c for c in all_cats if any(k in c.lower() for k in LOAN_KEYWORDS)]
    nonmtg_cats  = [c for c in loan_cats if not any(k in c.lower() for k in ["mortgage", "home loan"])]

    if loan_cats and avg_monthly_inc > 0:
        avg_loan    = exp_all[exp_all["Category"].isin(loan_cats)]["Amount"].sum() / N_MONTHS_FH
        tdsr_val    = avg_loan / avg_monthly_inc * 100
        tdsr_status = "good" if tdsr_val <= 25 else ("warn" if tdsr_val <= 35 else "bad")
        tdsr_pct_bar = min(tdsr_val / 50 * 100, 100)
        tdsr_target  = 35 / 50 * 100
        tdsr_detail  = (
            f"Average monthly loan repayments: <b>S${avg_loan:,.0f}</b> "
            f"(categories: {', '.join(loan_cats)})."
        )
    else:
        tdsr_val, tdsr_pct_bar, tdsr_target = None, 0, 70
        tdsr_status = "na"
        tdsr_detail = (
            "No loan repayment categories detected. To track this ratio, add expenses "
            "with a category containing a keyword like <em>Loan</em>, <em>Mortgage</em>, "
            "<em>Debt</em>, or <em>Repayment</em>."
        )

    if nonmtg_cats and avg_monthly_inc > 0:
        avg_nm_loan  = exp_all[exp_all["Category"].isin(nonmtg_cats)]["Amount"].sum() / N_MONTHS_FH
        ndsr_val     = avg_nm_loan / avg_monthly_inc * 100
        ndsr_status  = "good" if ndsr_val <= 10 else ("warn" if ndsr_val <= 15 else "bad")
        ndsr_pct_bar = min(ndsr_val / 30 * 100, 100)
        ndsr_target  = 15 / 30 * 100
        ndsr_detail  = (
            f"Average monthly non-mortgage repayments: <b>S${avg_nm_loan:,.0f}</b> "
            f"(categories: {', '.join(nonmtg_cats)})."
        )
    else:
        ndsr_val, ndsr_pct_bar, ndsr_target = None, 0, 50
        ndsr_status = "na"
        ndsr_detail = (
            "No non-mortgage loan categories detected. Separate mortgage and non-mortgage "
            "loans by using specific category names to unlock this metric."
        )

    # ── Overall health score ──────────────────────────────────────────────────
    STATUS_SCORE = {"good": 100, "warn": 55, "bad": 15}
    scored = [(s, STATUS_SCORE[s]) for s in [ef_status, sav_status, tdsr_status, ndsr_status]
              if s in STATUS_SCORE]
    if scored:
        overall = sum(v for _, v in scored) / len(scored)
        if overall >= 80:   ov_label, ov_color, ov_text = "Excellent", "#DCFCE7", "#1B5E20"
        elif overall >= 60: ov_label, ov_color, ov_text = "Good",      "#D1FAE5", "#2E7D32"
        elif overall >= 40: ov_label, ov_color, ov_text = "Fair",      "#FEF3C7", "#E65100"
        else:               ov_label, ov_color, ov_text = "Needs Work","#FEE2E2", "#B71C1C"
        tracked = len(scored)
    else:
        overall, ov_label, ov_color, ov_text, tracked = None, "Incomplete", "#F2F6F5", "#7A9E98", 0

    # ── Overall score banner ──────────────────────────────────────────────────
    banner_score = f"{overall:.0f}" if overall is not None else "—"
    st.markdown(f"""
    <div style="background:linear-gradient(135deg,#004D40 0%,#00695C 100%);
                border-radius:20px;padding:28px 36px;margin-bottom:28px;
                display:flex;align-items:center;justify-content:space-between;
                box-shadow:0 4px 20px rgba(0,77,64,0.25)">
      <div>
        <div style="font-size:11px;font-weight:700;letter-spacing:2px;
                    text-transform:uppercase;color:#80CBC4;margin-bottom:8px">
          Overall Financial Health Score
        </div>
        <div style="font-family:'DM Serif Display',serif;font-size:18px;color:#FFFFFF;">
          Based on {tracked} of 4 ratios tracked
        </div>
        <div style="font-size:12px;color:#80CBC4;margin-top:6px;line-height:1.6">
          Emergency Funds · Savings Ratio · TDSR · Non-Mortgage DSR
        </div>
      </div>
      <div style="text-align:right">
        <div style="font-family:'DM Serif Display',serif;font-size:64px;
                    color:#FFFFFF;line-height:1">{banner_score}</div>
        <div style="background:{ov_color};color:{ov_text};border-radius:100px;
                    padding:6px 22px;font-size:13px;font-weight:700;
                    display:inline-block;margin-top:6px">{ov_label}</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Ratio card helper ─────────────────────────────────────────────────────
    def ratio_card(label, icon, value, unit, guideline, pct_bar, target_pct,
                   status, detail, lower_is_better=False):
        if status == "good":
            bar_color, badge_bg, badge_fg, badge_text = "#00BFA5", "#DCFCE7", "#166534", "✅ Healthy"
        elif status == "warn":
            bar_color, badge_bg, badge_fg, badge_text = "#FF8F00", "#FEF3C7", "#92400E", "⚠️ Needs Attention"
        elif status == "bad":
            bar_color, badge_bg, badge_fg, badge_text = "#EF5350", "#FEE2E2", "#991B1B", "🚨 At Risk"
        else:
            bar_color, badge_bg, badge_fg, badge_text = "#B0BEC5", "#F2F6F5", "#546E7A", "ℹ️ Not Tracked"

        val_str = f"{value:.1f}{unit}" if value is not None else "—"
        left_border = "#00BFA5" if status == "good" else (
                      "#FF8F00" if status == "warn" else (
                      "#EF5350" if status == "bad" else "#B0BEC5"))

        # Progress bar with target marker
        bar_html = f"""
        <div style="position:relative;height:8px;background:#EFF4F3;
                    border-radius:100px;margin:14px 0 4px">
          <div style="width:{pct_bar:.1f}%;height:100%;background:{bar_color};
                      border-radius:100px;transition:width 0.4s ease"></div>
          <div style="position:absolute;top:-5px;left:{target_pct:.1f}%;
                      height:18px;width:3px;background:#E65100;border-radius:2px"
               title="Target threshold"></div>
        </div>
        <div style="display:flex;justify-content:space-between;
                    font-size:10px;color:#7A9E98;margin-bottom:4px">
          <span>0</span>
          <span style="color:#E65100;font-weight:600">▲ target</span>
          <span>Max</span>
        </div>
        """

        return f"""
        <div style="background:#FFFFFF;border-radius:16px;padding:24px 26px;
                    border:1px solid #DDE9E7;border-left:4px solid {left_border};
                    box-shadow:0 2px 12px rgba(0,77,64,0.07);margin-bottom:18px;
                    height:100%">
          <div style="display:flex;justify-content:space-between;align-items:flex-start;
                      margin-bottom:4px">
            <div style="font-size:11px;font-weight:700;letter-spacing:1.4px;
                        text-transform:uppercase;color:#7A9E98">
              {icon}&nbsp; {label}
            </div>
            <div style="background:{badge_bg};color:{badge_fg};border-radius:100px;
                        padding:4px 12px;font-size:10px;font-weight:700;
                        letter-spacing:0.3px;white-space:nowrap">
              {badge_text}
            </div>
          </div>
          <div style="font-family:'DM Serif Display',serif;font-size:40px;
                      color:{left_border};line-height:1.1;margin:8px 0 2px">
            {val_str}
          </div>
          {bar_html}
          <div style="font-size:12px;color:#556B67;line-height:1.75;margin-top:10px">
            {detail}
          </div>
          <div style="margin-top:14px;font-size:11px;font-weight:700;
                      color:{badge_fg};background:{badge_bg};
                      border-radius:8px;padding:6px 12px;display:inline-block">
            Guideline: {guideline}
          </div>
        </div>
        """

    # ── Four ratio cards in 2×2 grid ─────────────────────────────────────────
    st.markdown('<div class="section-title">Financial Ratios</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="medium")
    with col1:
        st.markdown(ratio_card(
            "Emergency Funds", "🏦",
            ef_val, " months",
            "6 – 9 months of expenses",
            ef_pct_bar, ef_target,
            ef_status, ef_detail,
        ), unsafe_allow_html=True)

        st.markdown(ratio_card(
            "Total Debt Servicing Ratio", "💳",
            tdsr_val, "%",
            "35% or less of gross income",
            tdsr_pct_bar, tdsr_target,
            tdsr_status, tdsr_detail,
            lower_is_better=True,
        ), unsafe_allow_html=True)

    with col2:
        st.markdown(ratio_card(
            "Savings Ratio", "💰",
            sav_val, "%",
            ">15% of gross income",
            sav_pct_bar, sav_target,
            sav_status, sav_detail,
        ), unsafe_allow_html=True)

        st.markdown(ratio_card(
            "Non-Mortgage Debt Servicing Ratio", "📋",
            ndsr_val, "%",
            "15% or less of take-home income",
            ndsr_pct_bar, ndsr_target,
            ndsr_status, ndsr_detail,
            lower_is_better=True,
        ), unsafe_allow_html=True)

    # ── Supporting metrics strip ──────────────────────────────────────────────
    st.markdown('<div class="section-title">All-Time Monthly Averages</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    c1.metric("Avg Monthly Income",   f"S${avg_monthly_inc:,.0f}")
    c2.metric("Avg Monthly Expenses", f"S${avg_monthly_exp:,.0f}")
    sav_delta = f"{sav_val:.1f}% savings rate" if sav_val is not None else None
    c3.metric("Avg Monthly Savings",  f"S${avg_monthly_sav:,.0f}", delta=sav_delta)

    # ── Plotly gauge charts ───────────────────────────────────────────────────
    st.markdown('<div class="section-title">Visual Gauges</div>', unsafe_allow_html=True)

    def make_gauge(title, value, max_val, target, unit, good_range, warn_range):
        if value is None:
            value = 0
            bar_color = "#B0BEC5"
        elif good_range[0] <= value <= good_range[1]:
            bar_color = "#00BFA5"
        elif warn_range[0] <= value <= warn_range[1]:
            bar_color = "#FF8F00"
        else:
            bar_color = "#EF5350"

        steps = [
            dict(range=[0, warn_range[0]], color="#DCFCE7"),
            dict(range=[warn_range[0], target], color="#FEF3C7"),
            dict(range=[target, max_val], color="#FEE2E2"),
        ]
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=value,
            number={"suffix": unit, "font": {"size": 28, "family": "DM Serif Display"}},
            title={"text": title, "font": {"size": 13, "color": "#7A9E98"}},
            gauge=dict(
                axis=dict(range=[0, max_val], tickfont=dict(size=10)),
                bar=dict(color=bar_color, thickness=0.6),
                steps=steps,
                threshold=dict(
                    line=dict(color="#E65100", width=3),
                    thickness=0.85,
                    value=target,
                ),
                bgcolor="#F2F6F5",
                borderwidth=0,
            ),
        ))
        fig.update_layout(
            height=220,
            margin=dict(l=20, r=20, t=40, b=10),
            paper_bgcolor="rgba(0,0,0,0)",
            font=dict(family="DM Sans"),
        )
        return fig

    g1, g2, g3, g4 = st.columns(4)
    with g1:
        st.plotly_chart(make_gauge(
            "Emergency Fund", ef_val, 12, 6, " mo",
            good_range=(6, 12), warn_range=(3, 6),
        ), use_container_width=True)
    with g2:
        st.plotly_chart(make_gauge(
            "Savings Ratio", sav_val, 30, 15, "%",
            good_range=(15, 30), warn_range=(10, 15),
        ), use_container_width=True)
    with g3:
        st.plotly_chart(make_gauge(
            "Total DSR", tdsr_val, 50, 35, "%",
            good_range=(0, 25), warn_range=(25, 35),
        ), use_container_width=True)
    with g4:
        st.plotly_chart(make_gauge(
            "Non-Mortgage DSR", ndsr_val, 30, 15, "%",
            good_range=(0, 10), warn_range=(10, 15),
        ), use_container_width=True)

    # ── Methodology note ──────────────────────────────────────────────────────
    st.markdown("""
    <div style="background:#F2F6F5;border-radius:12px;padding:18px 22px;
                margin-top:8px;border:1px solid #DDE9E7">
      <div style="font-size:11px;font-weight:700;letter-spacing:1.2px;
                  text-transform:uppercase;color:#7A9E98;margin-bottom:10px">
        📌 Methodology
      </div>
      <div style="font-size:12px;color:#556B67;line-height:1.9">
        <b>Emergency Funds:</b> Total banking balances + liquid cash (latest Networth entry)
        ÷ average monthly expenses over all tracked months.<br>
        <b>Savings Ratio:</b> Average monthly net savings ÷ average monthly income.
        Gross income (pre-CPF) would yield a slightly lower ratio.<br>
        <b>TDSR / Non-Mortgage DSR:</b> Auto-detected from expense categories whose name
        contains keywords: <em>Loan, Mortgage, Debt, Repayment, Installment</em>.<br>
        <b>Guidelines</b> sourced from the Monetary Authority of Singapore (MAS) · 2026.
      </div>
    </div>
    """, unsafe_allow_html=True)
