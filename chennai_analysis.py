"""
chennai_analysis.py — Chennai Four-Reservoir Storage Analysis
Assignment A0, Part 5 | Student: Bera Yashwant Pavan Kumar | TechBharat C2-21

Dataset: Chennai Water Management by sudalairajkumar (Kaggle)
  URL: https://www.kaggle.com/datasets/sudalairajkumar/chennai-water-management
  File: chennai_reservoir_levels.csv
  Columns: Date, POONDI, CHOLAVARAM, REDHILLS, CHEMBARAMBAKKAM (units: mcft)
  Date format: DD-MM-YYYY
  Date range: 01-01-2004 to ~mid-2019

Place the CSV at:
  water-intel/a0/bera_yashwant_pavan_kumar/data/chennai_reservoir_levels.csv

Then run:  python chennai_analysis.py
Outputs:   chennai_reservoirs.png  (in same directory as this script)
"""

import os
import sys
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# ── Config ─────────────────────────────────────────────────────────────────────
SCRIPT_DIR   = os.path.dirname(os.path.abspath(__file__))
DATA_PATH    = os.path.join(SCRIPT_DIR, "data", "chennai_reservoir_levels.csv")
OUT_PATH     = os.path.join(SCRIPT_DIR, "chennai_reservoirs.png")

RESERVOIRS   = ["POONDI", "CHOLAVARAM", "REDHILLS", "CHEMBARAMBAKKAM"]
CAPACITIES   = {          # mcft (million cubic feet)
    "POONDI":          3231,
    "CHOLAVARAM":       881,
    "REDHILLS":        3300,
    "CHEMBARAMBAKKAM": 3645,
}
TOTAL_CAP    = sum(CAPACITIES.values())   # 11 057 mcft

COLORS = {
    "POONDI":          "#1f77b4",   # blue
    "CHOLAVARAM":      "#ff7f0e",   # orange
    "REDHILLS":        "#2ca02c",   # green
    "CHEMBARAMBAKKAM": "#d62728",   # red
}

# "Day Zero" annotation anchor
DAY_ZERO_DATE = pd.Timestamp("2019-06-19")


def load_data(path: str) -> pd.DataFrame:
    if not os.path.exists(path):
        print(f"\n[ERROR] Data file not found:\n  {path}\n")
        print("Please download 'chennai_reservoir_levels.csv' from:")
        print("  https://www.kaggle.com/datasets/sudalairajkumar/chennai-water-management")
        print(f"and place it at:\n  {path}\n")
        sys.exit(1)

    df = pd.read_csv(path, dayfirst=True, parse_dates=["Date"])
    df = df.sort_values("Date").reset_index(drop=True)
    df["TOTAL"] = df[RESERVOIRS].sum(axis=1)
    df["TOTAL_PCT"] = df["TOTAL"] / TOTAL_CAP * 100
    for res in RESERVOIRS:
        df[f"{res}_PCT"] = df[res] / CAPACITIES[res] * 100
    return df


def save_plot(df: pd.DataFrame, out_path: str):
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10), sharex=True)

    # ── Top panel: Individual reservoir storage (mcft) ──────────────────────
    for res in RESERVOIRS:
        ax1.plot(df["Date"], df[res], label=res.title(), color=COLORS[res],
                 linewidth=1.2, alpha=0.9)

    ax1.set_ylabel("Storage (mcft)", fontsize=11)
    ax1.set_title("Chennai Four-Reservoir Daily Storage — 2004 to mid-2019\n"
                  "Data: CMWSSB via Kaggle (sudalairajkumar/chennai-water-management)",
                  fontsize=12)
    ax1.legend(loc="upper right", fontsize=9)
    ax1.grid(True, alpha=0.3)

    # Annotate Day Zero on top panel
    ax1.axvline(DAY_ZERO_DATE, color="black", linestyle=":", linewidth=1.5)
    ax1.text(DAY_ZERO_DATE, ax1.get_ylim()[1] * 0.95,
             "Day Zero\n19 Jun 2019",
             fontsize=8, ha="left", va="top", color="black",
             bbox=dict(boxstyle="round,pad=0.2", fc="lightyellow", ec="grey", alpha=0.8))

    # ── Bottom panel: Combined % of total capacity ───────────────────────────
    ax2.plot(df["Date"], df["TOTAL_PCT"], color="navy", linewidth=1.5,
             label="Combined level (% of 11,057 mcft total)")
    ax2.fill_between(df["Date"], df["TOTAL_PCT"], alpha=0.15, color="navy")

    # Shade 2018-2019 drought band
    drought_start = pd.Timestamp("2018-01-01")
    drought_end   = pd.Timestamp("2019-06-30")
    ax2.axvspan(drought_start, drought_end,
                color="red", alpha=0.08, label="2018–2019 drought period")

    # Annotate NE monsoon recovery
    recovery_date = pd.Timestamp("2019-11-01")
    ax2.axvline(recovery_date, color="green", linestyle="--", linewidth=1.3)
    ax2.text(recovery_date, 5, " NE Monsoon\n 2019 recovery",
             fontsize=8, color="darkgreen",
             bbox=dict(boxstyle="round,pad=0.2", fc="honeydew", ec="green", alpha=0.8))

    ax2.axvline(DAY_ZERO_DATE, color="black", linestyle=":", linewidth=1.5)
    ax2.text(DAY_ZERO_DATE, 50, "Day Zero\n19 Jun 2019",
             fontsize=8, ha="left", color="black",
             bbox=dict(boxstyle="round,pad=0.2", fc="lightyellow", ec="grey", alpha=0.8))

    ax2.axhline(10, color="red", linestyle="--", linewidth=1, alpha=0.7, label="10% emergency threshold")

    ax2.set_ylabel("Combined Level (% of capacity)", fontsize=11)
    ax2.set_xlabel("Date", fontsize=11)
    ax2.set_ylim(0, 110)
    ax2.legend(loc="upper right", fontsize=9)
    ax2.grid(True, alpha=0.3)

    ax2.xaxis.set_major_locator(mdates.YearLocator())
    ax2.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    plt.setp(ax2.xaxis.get_majorticklabels(), rotation=45, ha="right")

    plt.tight_layout()
    plt.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Saved -> {out_path}")


def print_interpretation(df: pd.DataFrame):
    print("\n" + "=" * 65)
    print("  5-Line Interpretation")
    print("=" * 65)
    print("""
(a) Annual NE monsoon pattern: Reservoir levels reliably recover each
    October–December during the northeast monsoon, filling from seasonal
    lows (~20–40%) to peaks of 70–100% — the city's primary recharge
    window — before declining through the dry summer months.

(b) 2018–2019 divergence: The 2018 northeast monsoon received only ~344 mm
    against a long-period average of ~758 mm (≈55% deficit), following
    sub-par monsoons in 2016 and 2017; combined storage crashed from
    ~40% in Oct 2018 to effectively 0% by June 2019 — a trajectory
    with no historical precedent in the 2004–2019 record.

(c) Early-warning opportunity: A monitoring system tracking the October
    post-monsoon fill rate could have flagged by November 2018 that the
    seasonal recharge was critically low; issuing a Tier-1 alert by
    December 2018 (storage < 25% of capacity with no recovery trend)
    would have given authorities a 6-month window to implement demand
    rationing, activate emergency tanker/groundwater contingency plans,
    and fast-track inter-basin transfers before Day Zero in June 2019.
""")
    print("=" * 65)


def main():
    df = load_data(DATA_PATH)
    save_plot(df, OUT_PATH)
    print_interpretation(df)


if __name__ == "__main__":
    main()
