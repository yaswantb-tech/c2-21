"""
sim_two_tanks.py -- 48-Hour Two-Tank Simulator (Bonus)
Assignment A0, Part 4 Bonus | Student: Bera Yashwant Pavan Kumar | TechBharat C2-21

One 250 kL/h pump exclusively routed to Tank A, Tank B, or OFF each hour.
Priority control with look-ahead: pump feeds the tank most at risk of shortage,
but checks that pumping will not cause overflow before committing.
Both tanks kept within [20%, 95%] over 48 hours.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os

# -- Constants -----------------------------------------------------------------
CAPACITY_A   = 1_000    # kL -- Tank A
CAPACITY_B   =   800    # kL -- Tank B (different size for realism)
INITIAL_A    =   600    # kL (60%)
INITIAL_B    =   400    # kL (50%)
LOW_SP       = 0.20
HIGH_SP      = 0.95
PUMP_RATE    = 250      # kL/h (shared, exclusive)
HOURS        = 48
SEED         = 42

POPULATION_A = 12_000
POPULATION_B =  8_000
LPCD         = 135
DAILY_A      = POPULATION_A * LPCD / 1_000   # 1 620 kL/day
DAILY_B      = POPULATION_B * LPCD / 1_000   # 1 080 kL/day

DIURNAL = [0.3, 0.3, 0.3, 0.3, 0.5, 1.2,
           2.0, 2.2, 1.8, 1.2, 0.9, 0.8,
           0.8, 0.8, 0.8, 0.9, 1.1, 1.6,
           1.9, 1.6, 1.1, 0.7, 0.5, 0.4]


def build_demand(daily_kl: float, hours: int, seed: int) -> np.ndarray:
    rng  = np.random.default_rng(seed)
    base = daily_kl / 24
    noise = rng.uniform(0.9, 1.1, hours)
    return np.array([base * DIURNAL[t % 24] * noise[t] for t in range(hours)])


def priority_schedule(dem_a: np.ndarray, dem_b: np.ndarray):
    """
    Look-ahead priority control:
      1. For each tank, compute end-of-hour volume if pump routes to it.
      2. If routing to a tank would overflow it (>95%), that tank is ineligible.
      3. Among eligible tanks, choose the one with the lower relative level.
         If both are above 85%, pump is OFF (no urgent need).
      4. If a tank is at critical shortage risk (<22% after this hour
         without pump), it overrides and grabs the pump.
    """
    vol_a, vol_b = float(INITIAL_A), float(INITIAL_B)
    sched   = []          # 'A', 'B', or 'OFF'
    lvl_a_hist, lvl_b_hist = [], []

    for t in range(HOURS):
        d_a, d_b = dem_a[t], dem_b[t]
        pct_a = vol_a / CAPACITY_A
        pct_b = vol_b / CAPACITY_B

        # Look-ahead end volumes
        va_with    = min(CAPACITY_A, vol_a + PUMP_RATE - d_a)
        vb_with    = min(CAPACITY_B, vol_b + PUMP_RATE - d_b)
        va_without = max(0.0, vol_a - d_a)
        vb_without = max(0.0, vol_b - d_b)

        a_overflow = va_with > HIGH_SP * CAPACITY_A
        b_overflow = vb_with > HIGH_SP * CAPACITY_B
        a_critical = va_without < LOW_SP * CAPACITY_A
        b_critical = vb_without < LOW_SP * CAPACITY_B

        if a_critical and not a_overflow:
            choice = "A"
        elif b_critical and not b_overflow:
            choice = "B"
        elif a_overflow and b_overflow:
            choice = "OFF"
        elif a_overflow:
            # Can only pump B -- but check if B needs it
            choice = "B" if pct_b < 0.85 else "OFF"
        elif b_overflow:
            # Can only pump A -- but check if A needs it
            choice = "A" if pct_a < 0.85 else "OFF"
        elif pct_a <= pct_b and pct_a < 0.80:
            choice = "A"
        elif pct_b < pct_a and pct_b < 0.80:
            choice = "B"
        else:
            choice = "OFF"

        in_a = PUMP_RATE if choice == "A" else 0.0
        in_b = PUMP_RATE if choice == "B" else 0.0

        vol_a = max(0.0, min(CAPACITY_A, vol_a + in_a - d_a))
        vol_b = max(0.0, min(CAPACITY_B, vol_b + in_b - d_b))

        sched.append(choice)
        lvl_a_hist.append(vol_a / CAPACITY_A * 100)
        lvl_b_hist.append(vol_b / CAPACITY_B * 100)

    return sched, np.array(lvl_a_hist), np.array(lvl_b_hist)


def print_summary(lvl_a, lvl_b, sched):
    sh_a = sum(1 for l in lvl_a if l < LOW_SP * 100)
    oh_a = sum(1 for l in lvl_a if l > HIGH_SP * 100)
    sh_b = sum(1 for l in lvl_b if l < LOW_SP * 100)
    oh_b = sum(1 for l in lvl_b if l > HIGH_SP * 100)
    print("=" * 55)
    print("  48-Hour Two-Tank Simulation Summary")
    print("=" * 55)
    print(f"  Tank A -- shortage hrs: {sh_a} | overflow hrs: {oh_a}")
    print(f"  Tank B -- shortage hrs: {sh_b} | overflow hrs: {oh_b}")
    print(f"  Pump->A: {sched.count('A')}h | Pump->B: {sched.count('B')}h | OFF: {sched.count('OFF')}h")
    print("=" * 55)
    print("  Strategy: look-ahead priority control -- each hour checks")
    print("  if pumping would overflow either tank before routing;")
    print("  critical-shortage tanks grab the pump first, otherwise")
    print("  the pump feeds whichever tank has the lower relative level.")


def save_plot(lvl_a, lvl_b, sched, out_path):
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 8), sharex=True)
    t = np.arange(HOURS)

    for ax, lvl, cap_label, color, tank_id in [
        (ax1, lvl_a, f"Tank A ({CAPACITY_A} kL)", "navy",      "A"),
        (ax2, lvl_b, f"Tank B ({CAPACITY_B} kL)", "darkgreen", "B"),
    ]:
        pumping = False
        first   = True
        for i in range(HOURS):
            if sched[i] == tank_id and not pumping:
                band_start = i
                pumping = True
            elif sched[i] != tank_id and pumping:
                lbl = "Pump ON (this tank)" if first else ""
                ax.axvspan(band_start, i, color="steelblue", alpha=0.20, label=lbl)
                pumping = False
                first   = False
        if pumping:
            ax.axvspan(band_start, HOURS, color="steelblue", alpha=0.20)

        ax.plot(t, lvl, color=color, linewidth=2, label=cap_label)
        ax.axhline(LOW_SP  * 100, color="red",    linestyle="--", linewidth=1.3, label="Low 20%")
        ax.axhline(HIGH_SP * 100, color="orange", linestyle="--", linewidth=1.3, label="High 95%")
        ax.set_ylabel("Level (%)", fontsize=10)
        ax.set_ylim(0, 105)
        ax.legend(loc="upper right", fontsize=8)
        ax.grid(True, alpha=0.3)
        ax.set_title(cap_label, fontsize=11)

    ax2.set_xlabel("Hour (0 = midnight Day 1)", fontsize=11)
    ax2.set_xticks(range(0, HOURS + 1, 6))
    ax2.set_xticklabels([f"{h%24:02d}:00\nD{h//24+1}" for h in range(0, HOURS + 1, 6)], fontsize=8)

    fig.suptitle("48-Hour Two-Tank Shared Pump Simulation\n"
                 "Strategy: look-ahead priority -- pump feeds lower-risk / lower-level tank", fontsize=12)
    plt.tight_layout()
    plt.savefig(out_path, dpi=150)
    plt.close()


def main():
    dem_a = build_demand(DAILY_A, HOURS, SEED)
    dem_b = build_demand(DAILY_B, HOURS, SEED + 1)
    sched, lvl_a, lvl_b = priority_schedule(dem_a, dem_b)
    print_summary(lvl_a, lvl_b, sched)

    out_dir  = os.path.dirname(os.path.abspath(__file__))
    out_path = os.path.join(out_dir, "two_tank_plot.png")
    save_plot(lvl_a, lvl_b, sched, out_path)
    print(f"\n  Plot saved -> {out_path}")


if __name__ == "__main__":
    main()
