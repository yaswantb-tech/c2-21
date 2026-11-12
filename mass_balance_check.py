"""
mass_balance_check.py — Verification of OHT-07 mass-balance calculations
Assignment A0, Part 3 | Student: Bera Yashwant Pavan Kumar | TechBharat C2-21
"""

CAPACITY    = 800        # kL
AREA        = 200        # m²
LOW_SP      = 0.20       # 20 %
HIGH_SP     = 0.95       # 95 %
PUMP_RATE   = 150        # kL/h
PUMP_HOURS  = {5, 6}     # pump ON during hour-slots 05-06 and 06-07

demand = {5: 60, 6: 140, 7: 180, 8: 160, 9: 120, 10: 80}


def status(vol, cap=CAPACITY):
    pct = vol / cap * 100
    if pct > HIGH_SP * 100:
        return "OVERFLOW"
    if pct <= 0:
        return "DRY / Unmet"
    if pct <= LOW_SP * 100:
        return "SHORTAGE"
    return "OK"


# ── Q1: Starting volume at 05:00 ───────────────────────────────────────────────
start_level_m = 1.2
start_vol     = AREA * start_level_m          # 200 * 1.2 = 240 kL
print("=" * 60)
print("Q1: Starting volume")
print(f"    Volume = {AREA} m² × {start_level_m} m = {start_vol:.1f} kL")
print(f"    Level  = {start_vol}/{CAPACITY} × 100 = {start_vol/CAPACITY*100:.2f} %")

# ── Q2: Base scenario (pump ON only 05-07) ────────────────────────────────────
print("\nQ2: Hour-by-hour table (pump ON only 05-06 and 06-07):")
print(f"{'Hour':<8}{'Inflow':>8}{'Outflow':>9}{'EndVol':>9}{'EndPct':>9}  Status     Unmet")
vol         = start_vol
total_unmet = 0.0
for h in range(5, 11):
    inflow   = PUMP_RATE if h in PUMP_HOURS else 0
    d        = demand[h]
    raw_next = vol + inflow - d
    unmet    = max(0.0, -raw_next) if raw_next < 0 else 0.0
    vol      = max(0.0, min(CAPACITY, raw_next))
    pct      = vol / CAPACITY * 100
    total_unmet += unmet
    print(f"  {h:02d}-{h+1:02d}  {inflow:>7}  {d:>7}  {vol:>8.1f}  {pct:>7.2f}%  {status(vol):<12} {unmet:.1f}")
print(f"  Total unmet demand by 11:00 = {total_unmet:.1f} kL")

# ── Q3: Set-point breach time ─────────────────────────────────────────────────
print("\nQ3: Low set-point breach")
print("    After 07-08: volume = 160 kL = 20.00% — exactly at set-point.")
print("    At 08:00, demand starts draining at 160 kL/h with 0 inflow.")
print("    Tank breaches 20% set-point immediately at the start of hour 08:00.")
print(f"    Total unmet demand = {total_unmet:.0f} kL (hours 09-10 and 10-11).")

# ── Q4: Minimum pump hours for tank >= 20% through 11:00 ──────────────────────
print("\nQ4: Minimum whole continuous pump hours starting at 05:00")
total_demand = sum(demand.values())
kl_needed    = LOW_SP * CAPACITY + total_demand - start_vol   # 160 + 740 - 240 = 660
min_h_exact  = kl_needed / PUMP_RATE
print(f"    Total demand 05-11 = {total_demand} kL")
print(f"    Required pump output >= {kl_needed:.1f} kL  =>  {min_h_exact:.4f} h  =>  ceil = 5 hours")

print("\n    Verify 5 pump hours (05:00 – 10:00):")
print(f"{'Hour':<8}{'Inflow':>8}{'Outflow':>9}{'EndVol':>9}{'EndPct':>9}  Status")
vol = start_vol
for h in range(5, 11):
    inflow = PUMP_RATE if h < 10 else 0    # pump ON 05, 06, 07, 08, 09
    vol    = max(0.0, min(CAPACITY, vol + inflow - demand[h]))
    pct    = vol / CAPACITY * 100
    print(f"  {h:02d}-{h+1:02d}  {inflow:>7}  {demand[h]:>7}  {vol:>8.1f}  {pct:>7.2f}%  {status(vol)}")

# ── Q5: Overflow exact time ────────────────────────────────────────────────────
print("\nQ5: Overflow time calculation")
start_q5   = 0.50 * CAPACITY                 # 400 kL
net_rate   = 300 - 20                        # 280 kL/h
target_vol = HIGH_SP * CAPACITY              # 760 kL
time_h     = (target_vol - start_q5) / net_rate
hours_int  = int(time_h)
minutes    = round((time_h - hours_int) * 60)
start_hhmm = 22 * 60                         # 22:00 in minutes
end_min    = start_hhmm + hours_int * 60 + minutes
print(f"    Start volume = {start_q5:.0f} kL (50%)")
print(f"    Net fill rate = 300 - 20 = {net_rate} kL/h")
print(f"    Volume to reach 95% (760 kL) = {target_vol - start_q5:.0f} kL")
print(f"    Time = {target_vol - start_q5:.0f} / {net_rate} = {time_h:.4f} h = {hours_int}h {minutes}min")
print(f"    22:00 + {hours_int}h {minutes}min = {end_min // 60:02d}:{end_min % 60:02d}")
print(f"    >> Operator must stop pump by 23:{minutes:02d}.")
print("=" * 60)
