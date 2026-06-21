# CLAUDE.md

## Project Goal

Personal finance tracker web app for Naveen (Singapore). Replaces an Excel file with a live Streamlit dashboard. Data lives in a Google Sheet — the app reads it via CSV export URLs and visualises spending, income, savings, and net worth.

## Stack

- **Framework:** Streamlit (`app.py` is the single entry point)
- **Language:** Python 3
- **Charts:** Plotly (Express + Graph Objects)
- **Data:** pandas, read from Google Sheets via `pd.read_csv(url)`
- **Runtime:** `venv/` virtual environment

## Virtual Environment — Always Required

**Never install packages globally.** The project now uses `venv312` (Python 3.12) because `ninejs` requires Python ≥ 3.10:

```bash
# Install a package
venv312/bin/pip install <package>

# Run the app
venv312/bin/streamlit run app.py

# Or activate first
source venv312/bin/activate
```

The old `venv/` (Python 3.9) remains on disk but is no longer the active environment. When adding new dependencies, also add them to `requirements.txt`.

## Data Sources

| Variable | Sheet tab | What it contains |
|---|---|---|
| `GSHEET_URL` | Transactions tab (`gid=379184043`) | All income & expense rows |
| `NW_GSHEET_URL` | Networth tab (`gid=699682413`) | Monthly net worth snapshots by account |

Both are cached with `@st.cache_data(ttl=300)`. Call `.clear()` on the cache function to force a refresh.

The sheet must be shared publicly (Anyone with the link → Viewer) for the CSV export to work.

## App Structure

All pages live in `app.py` as `if/elif` blocks gated on the `page` sidebar radio value:

| Page | Key content |
|---|---|
| `📊  Dashboard` | KPI metrics, monthly bar chart, daily spend, top 5, smart recommendations, savings forecast |
| `📈  Spending Analysis` | Category breakdown, month-on-month comparison, payment method pie, transaction table |
| `💡  Insights` | Month comparison movers, all recommendations, subscription audit, SG benchmarks |
| `💳  Transactions` | Filterable, searchable full transaction table with CSV download |
| `🏦  Net Worth` | KPI row, net worth over time, asset breakdown, bank balances, CPF accounts, history table |

## Design System

Custom CSS is injected once at the top via `st.markdown("""<style>...</style>""", unsafe_allow_html=True)`. Key CSS variables:

```
--primary: #004D40   (dark teal)
--accent:  #00BFA5   (bright teal)
--bg:      #F2F6F5
--card:    #FFFFFF
--sidebar: #00352C
--text:    #1C3A35
--muted:   #7A9E98
```

Fonts: DM Serif Display (headings) + DM Sans (body), loaded from Google Fonts.

Reusable layout helpers: `base_layout(**extra)`, `styled_yaxis()`, `styled_xaxis()`.

## Key Conventions

- Currency is SGD; display as `S$X,XXX` format throughout.
- All amounts are numeric after `load_data()` — strip `S$` and commas before `pd.to_numeric`.
- `df_all` = all transactions; `exp_all` / `inc_all` = expense/income subsets; `df` / `exp` / `inc` = filtered by the selected month.
- `MONTHS` is a sorted list of month strings (`"Jan 2025"` format).
- `N_MONTHS` is the count of distinct months — used to compute monthly averages.
- Never use `st.set_page_config` more than once (it's already called at the top).
- Keep the app as a single file unless the user asks to split it.

## Running Locally

```bash
source venv/bin/activate
streamlit run app.py
```

The app opens at `http://localhost:8501`.
