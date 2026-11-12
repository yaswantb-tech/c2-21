"""
sim.py -- 48-Hour Single-Tank Water Level Simulator
Assignment A0, Part 4 | Student: Bera Yashwant Pavan Kumar | TechBharat C2-21

Finds a pump schedule that keeps tank level within [20%, 95%] for all 48 hours,
preferring night/off-peak hours for pumping. Outputs summary stats and saves
level_plot.png to the same directory as this script.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os

# -- Constants ------------------------------------------------------------------
CAPACITY_KL      = 1_000          # kL
INITIAL_KL       = 600            # kL  (60 %)
LOW_SETPOINT     = 0.20           # fraction
HIGH_SETPOINT    = 0.95           # fraction
POPULATION       = 20_000
LPCD             = 135
DAILY_DEMAND_KL  = POPULATION * LPCD / 1_000   # 2 700 kL/day
PUMP_RATE_KLH    = 250            # kL/h
HOURS            = 48
SEED             = 42

DIURNAL = [0.3, 0.3, 0.3, 0.3, 0.5, 1.2,
           2.0, 2.2, 1.8, 1.2, 0.9, 0.8,
           0.8, 0.8, 0.8, 0.9, 1.1, 1.6,
           1.9, 1.6, 1.1, 0.7, 0.5, 0.4]

# -- Demand Generation ---------------------------------------------------------
def build_demand(hours: int, seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    base = DAILY_DEMAND_KL / 24
    noise = rng.uniform(0.9, 1.1, hours)
    return np.array([base * DIURNAL[t % 24] * noise[t] for t in range(hours)])

# -- Pump Schedule -------------------------------------------------------------
def build_pump_schedule(demand: np.ndarray) -> np.ndarray:
    """
    Rule-based look-ahead hysteresis control:
      - At each hour, check volume after this hour WITH and WITHOUT the pump.
      - Pump ON  if volume-without-pump would drop below 25% (critical guard).
      - Pump OFF if volume-with-pump    would exceed  93% (overflow guard).
      - Night hours (21:00-05:00): pump ON when vol < 55%, OFF above 88%.
      - Day hours: pump ON when vol < 30%, OFF above 85%.
    Strategy found by: single-pass greedy look-ahead hysteresis -- the
    controller simulates one hour forward before committing each pump decision,
    eliminating overflow/shortage that pure reactive control misses.
    """
    low_kl   = LOW_SETPOINT  * CAPACITY_KL   # 200 kL
    high_kl  = HIGH_SETPOINT * CAPACITY_KL   # 950 kL
    vol      = float(INITIAL_KL)
    schedule = np.zeros(HOURS, dtype=int)
    pump_on  = 0

    for t in range(HOURS):
        hour_of_day = t % 24
        is_night    = hour_of_day >= 21 or hour_of_day < 5
        d           = demand[t]

        # Look-ahead: end-of-hour volume with/without pump
        vol_with    = min(CAPACITY_KL, vol + PUMP_RATE_KLH - d)
        vol_without = max(0.0,         vol                 - d)

        if vol_without < low_kl:
            # Critical -- must pump to prevent shortage
            pump_on = 1
        elif vol_with > high_kl:
            # Pump would cause overflow -- stay off (unless critical)
            pump_on = 0
        elif is_night:
            if vol < 0.55 * CAPACITY_KL:
                pump_on = 1
            elif vol > 0.88 * CAPACITY_KL:
                pump_on = 0
            # else keep previous state
        else:
            if vol < 0.30 * CAPACITY_KL:
                pump_on = 1
            elif vol > 0.85 * CAPACITY_KL:
                pump_on = 0
            # else keep previous state

        schedule[t] = pump_on
        inflow = PUMP_RATE_KLH if pump_on else 0.0
        vol    = max(0.0, min(CAPACITY_KL, vol + inflow - d))

    return schedule

# -- Simulation ----------------------------------------------------------------
def simulate(demand: np.ndarray, schedule: np.ndarray):
    vol    = float(INITIAL_KL)
    levels = []
    unmet  = 0.0
    spill  = 0.0

    for t in range(HOURS):
        inflow = PUMP_RATE_KLH if schedule[t] else 0.0
        d      = demand[t]

        raw_next = vol + inflow - d
        if raw_next < 0:
            unmet   += abs(raw_next)
            raw_next = 0.0
        if raw_next > CAPACITY_KL:
            spill    += raw_next - CAPACITY_KL
            raw_next  = CAPACITY_KL

        vol = raw_next
        levels.append(vol / CAPACITY_KL * 100.0)

    shortage_hrs = sum(1 for l in levels if l < LOW_SETPOINT  * 100)
    overflow_hrs = sum(1 for l in levels if l > HIGH_SETPOINT * 100)
    return np.array(levels), shortage_hrs, overflow_hrs, round(unmet, 2), round(spill, 2)

# -- Plot ----------------------------------------------------------------------
def save_plot(levels: np.ndarray, schedule: np.ndarray, out_path: str):
    fig, ax = plt.subplots(figsize=(14, 5))
    hours = np.arange(HOURS)

    # Shaded pump-ON bands
    pump_on_indices = [i for i, s in enumerate(schedule) if s]
    pumping = False
    first_band = True
    for t in range(HOURS):
        if schedule[t] and not pumping:
            band_start = t
            pumping = True
        elif not schedule[t] and pumping:
            label = "Pump ON hours" if first_band else ""
            ax.axvspan(band_start, t, color="steelblue", alpha=0.18, label=label)
            pumping = False
            first_band = False
    if pumping:
        ax.axvspan(band_start, HOURS, color="steelblue", alpha=0.18)

    ax.plot(hours, levels, color="navy", linewidth=2, label="Tank Level (%)")
    ax.axhline(LOW_SETPOINT  * 100, color="red",    linestyle="--", linewidth=1.4, label="Low set-point (20 %)")
    ax.axhline(HIGH_SETPOINT * 100, color="orange", linestyle="--", linewidth=1.4, label="High set-point (95 %)")

    ax.set_xlabel("Hour (0 = midnight Day 1)", fontsize=11)
    ax.set_ylabel("Tank Level (%)", fontsize=11)
    ax.set_title(
        "48-Hour OHT Level Trajectory\n"
        f"Population {POPULATION:,} | {LPCD} LPCD | Pump {PUMP_RATE_KLH} kL/h | Capacity {CAPACITY_KL} kL",
        fontsize=12
    )
    ax.set_xlim(0, HOURS - 1)
    ax.set_ylim(0, 105)
    ax.set_xticks(range(0, HOURS + 1, 6))
    ax.set_xticklabels([f"{h%24:02d}:00\nD{h//24+1}" for h in range(0, HOURS + 1, 6)], fontsize=8)
    ax.legend(loc="upper right", fontsize=9)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(out_path, dpi=150)
    plt.close()

# -- Main ----------------------------------------------------------------------
def main():
    demand   = build_demand(HOURS, SEED)
    schedule = build_pump_schedule(demand)
    levels, sh, oh, unmet, spill = simulate(demand, schedule)

    print("=" * 55)
    print("  48-Hour Single-Tank Simulation Summary")
    print("=" * 55)
    print(f"  Shortage hours  : {sh}")
    print(f"  Overflow hours  : {oh}")
    print(f"  Unmet demand    : {unmet:.2f} kL")
    print(f"  Spilled overflow: {spill:.2f} kL")
    print(f"  Pump hours ON   : {int(schedule.sum())} / 48")
    print("=" * 55)
    print("  Schedule strategy: Look-ahead greedy hysteresis -- pump")
    print("  simulates end-of-hour volume with/without itself before")
    print("  deciding; prefers night windows (21-05h) for filling,")
    print("  turning ON at <=55% and OFF at >=88% at night, while")
    print("  staying off during day unless level falls below 30%.")

    out_dir  = os.path.dirname(os.path.abspath(__file__))
    out_path = os.path.join(out_dir, "level_plot.png")
    save_plot(levels, schedule, out_path)
    print(f"\n  Plot saved -> {out_path}")

if __name__ == "__main__":
    main()
