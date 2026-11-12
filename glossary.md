# Water Supply Domain Glossary
**Assignment A0 — Domain Explorer**
**Student:** Bera Yashwant Pavan Kumar | **Cohort:** TechBharat C2-21

---

## 25 Key Terms

---

### 1. OHT / ESR — Overhead Tank / Elevated Service Reservoir
**Definition:** A water storage tank raised on a structure (typically 10–20 m above ground) so that gravity alone pushes water through the distribution network without a pump at the consumer end.

**Example:** An ESR of 500 kL capacity sits 15 m high; at full charge it delivers water to consumers up to 2 km away at a residual pressure of ~1.5 bar — no booster pump needed.

---

### 2. GLSR / Sump — Ground-Level Service Reservoir / Sump
**Definition:** A below-grade or at-grade enclosed storage tank that acts as a buffer between the treatment plant and pumping station, ensuring the pumps always have water to draw from.

**Example:** A GLSR with 2,000 kL capacity absorbs a 6-hour gap in raw-water supply; the pumps draw from it continuously at 300 kL/h without interruption.

---

### 3. MBR — Master Balancing Reservoir
**Definition:** A large intermediate reservoir (usually at a high elevation point in the network) that absorbs hourly demand swings and re-distributes flow across multiple zones.

**Example:** An MBR of 10,000 kL at 60 m elevation covers three distribution zones; when Zone-B demand spikes to 200 kL/h it draws from the MBR rather than stressing the WTP outflow.

---

### 4. WTP — Water Treatment Plant
**Definition:** A facility that removes physical, chemical, and biological contaminants from raw (source) water through a sequence of processes — typically coagulation → flocculation → sedimentation → filtration → chlorination — until the water is potable.

**Example:** Visakhapatnam's Mudasarlova WTP is rated at 54 MLD; it converts raw Mudasarlova reservoir water into treated drinking water for about 400,000 residents daily.

---

### 5. MLD — Million Litres per Day
**Definition:** The standard Indian engineering unit for large-scale water flow; 1 MLD = 1,000 kL/day = ~41.67 kL/h, used to rate WTP capacity, pipeline throughput, and reservoir inflow.

**Example:** A WTP rated 100 MLD processing at 80 % utilisation delivers 80 MLD = 80,000 kL/day to the city's distribution network.

---

### 6. kL / m³ — Kilolitre / Cubic Metre
**Definition:** The day-to-day volume unit in water utility billing and tank accounting; 1 kL = 1 m³ = 1,000 litres. OHT capacities, pump deliveries, and consumer bills are all expressed in kL.

**Example:** A household consuming 15 kL/month pays for exactly 15,000 litres; an OHT delivering 240 kL over 4 hours supplies at 60 kL/h.

---

### 7. LPCD — Litres Per Capita Per Day
**Definition:** A per-person daily water supply benchmark used to size infrastructure; CPHEEO's urban norm with underground sewerage is 135 LPCD.

**Example:** A ward of 50,000 people at 135 LPCD needs 6,750 kL/day = 6.75 MLD of treated water delivered to its zone inlet.

---

### 8. DMA — District Metered Area
**Definition:** A hydraulically isolated sub-zone of the distribution network, sealed off with boundary valves and monitored by one or two flow meters, so that night-flow measurements can pinpoint leakage.

**Example:** DMA-12 with 800 connections shows 40 kL/h inflow between 02:00–04:00 (minimum night flow); since measured consumption is only 10 kL/h, the inferred leakage is 30 kL/h ≈ 720 kL/day.

---

### 9. Zone / Ward
**Definition:** Administrative or hydraulic geographic divisions of a city used for supply scheduling, billing, and infrastructure planning; a ward is a civic boundary while a zone is an operational hydraulic boundary (the two may differ).

**Example:** Visakhapatnam is divided into ~72 wards for civic administration; the water utility further groups them into 6 hydraulic zones, each fed from a dedicated OHT.

---

### 10. Intermittent Supply
**Definition:** A mode of water distribution where taps run for only a few hours per day (or on certain days), because network pressure is insufficient to maintain continuous flow to all consumers.

**Example:** A colony receives supply from 06:00–08:00 and 18:00–19:00 daily — 3 hours total — meaning residents must store water in rooftop tanks or sumps to cover the remaining 21 hours.

---

### 11. 24×7 Supply
**Definition:** Continuous pressurised water delivery to consumers around the clock, eliminating the need for household storage tanks and enabling instantaneous leak detection through sustained pressure monitoring.

**Example:** Under Visakhapatnam's Smart City 24×7 pilot for Ward-21, pressure is maintained at ≥ 7 m head at all times; a household can draw water at 11 PM just as easily as at 7 AM.

---

### 12. Diurnal Pattern
**Definition:** The characteristic hourly variation of water demand over a 24-hour cycle, peaking in morning (06:00–09:00) and evening (17:00–20:00) and dipping at night (02:00–04:00).

**Example:** A zone's average demand is 100 kL/h; its morning peak hits 220 kL/h (peak factor 2.2) while the 03:00 trough drops to 30 kL/h — that full curve is its diurnal pattern.

---

### 13. Peak Factor
**Definition:** The ratio of peak-hour demand to average-hour demand; used to size pipes, pumps, and OHTs so the system copes with the morning and evening rush without pressure drop.

**Example:** If daily demand = 2,400 kL (average 100 kL/h) and the 07:00 hour sees 220 kL demanded, the peak factor = 220/100 = 2.2 — pipes and OHTs must be sized for at least 220 kL/h.

---

### 14. NRW — Non-Revenue Water
**Definition:** The portion of treated water that enters the distribution system but never reaches a paying consumer — comprising physical losses (leaks, pipe bursts), apparent losses (meter errors, theft), and unbilled authorised consumption.

**Example:** A utility produces 100 MLD but bills only 68 MLD; its NRW = 32 % — equivalent to wasting 32,000 kL of expensively treated water every day.

---

### 15. Inflow / Outflow
**Definition:** Inflow is the volumetric rate (kL/h) at which water enters a tank or reservoir; outflow is the rate at which it leaves — the signed difference drives the mass balance each hour.

**Example:** An OHT has inflow (pump) = 150 kL/h and outflow (zone demand) = 200 kL/h; the net = −50 kL/h, so the tank loses 50 kL every hour until the pump increases or demand falls.

---

### 16. Mass Balance
**Definition:** The accounting equation that tracks tank volume over time: V(t+1) = V(t) + (Inflow − Outflow) × Δt; volume is conserved (no water appears or disappears, only the storage level changes).

**Example:** OHT at 500 kL, inflow 120 kL/h, outflow 90 kL/h over Δt = 1 h → V(next) = 500 + (120 − 90) × 1 = 530 kL; level rises by 3 % in a 1,000 kL tank.

---

### 17. Dead Storage
**Definition:** The volume of water permanently below the lowest outlet pipe of a tank; it cannot be drawn for supply under gravity and exists only as a structural / sedimentation buffer.

**Example:** An OHT has a 20 kL dead storage zone (the bottom 10 cm of the tank); even if the "usable" live storage empties, 20 kL remains inaccessible to consumers.

---

### 18. Live Storage
**Definition:** The usable volume between the dead-storage level and the high set-point (or overflow weir); this is the water that can actually be drawn for consumer supply.

**Example:** OHT capacity = 800 kL, dead storage = 40 kL, high set-point = 760 kL → live storage = 760 − 40 = 720 kL; the pump fills only this 720 kL range during normal operation.

---

### 19. Set-Point
**Definition:** A pre-programmed volume or level threshold that triggers an automatic control action — the low set-point starts the pump; the high set-point stops it — protecting the tank from running dry or overflowing.

**Example:** OHT-07: low set-point 160 kL (20 %), high set-point 760 kL (95 %); SCADA turns pump P-07 ON when level ≤ 160 kL and OFF when level ≥ 760 kL.

---

### 20. Overflow
**Definition:** Water that spills over the tank's overflow weir when inflow continues after the tank is full; overflow is wasted treated water and can cause localised flooding or structural damage.

**Example:** Pump P-07 delivers 300 kL/h; if it stays ON when the OHT is at 780 kL (capacity 800 kL), 20 kL spills in the first 4 minutes — operator must stop the pump within that window.

---

### 21. Pump Head
**Definition:** The total energy (expressed in metres of water column) a pump must deliver to push water from the sump to the OHT, accounting for elevation difference, pipe friction, and velocity head.

**Example:** OHT base at 18 m above sump + friction loss 4 m + velocity head 1 m → total pump head = 23 m; a pump rated < 23 m head cannot fill the OHT even at full speed.

---

### 22. Pump Rate
**Definition:** The volumetric flow a pump delivers per unit time (kL/h or L/s) at its rated head; also called discharge rate or pump capacity.

**Example:** Pump P-07 rated at 150 kL/h means it delivers 150,000 litres every hour when running against its design head — equivalent to 41.67 L/s.

---

### 23. Valve Operation
**Definition:** The manual or automated opening/closing of isolation, pressure-reducing, or check valves to control flow direction, pressure, and zone isolation in the distribution network.

**Example:** To fill OHT-East without overcharging OHT-West, the operator partially closes valve V-12 (reducing flow to 60 kL/h) while V-14 stays fully open (90 kL/h) — both tanks reach their high set-points simultaneously.

---

### 24. Supply Roster
**Definition:** A published timed schedule that specifies which ward, street, or zone receives water on which day and during which hours — used to manage equitable distribution when supply is intermittent.

**Example:** Ward-14's roster: Monday / Wednesday / Friday 06:30–08:30, Saturday 17:00–18:00; residents know in advance and fill their sump tanks during those windows.

---

### 25. SCADA — Supervisory Control and Data Acquisition
**Definition:** An industrial control system that uses sensors (flow, pressure, level) and remote terminal units (RTUs) to monitor the entire water network in real time and allows operators to issue remote commands (pump ON/OFF, valve open/close) from a central control room.

**Example:** Visakhapatnam's GVMC SCADA centre displays live OHT levels across all 40+ tanks on a city-wide map; when OHT-North drops below its 20 % set-point, the SCADA alarm fires and auto-starts pump P-N3 within 30 seconds.

---

*End of Glossary — 25 of 30 terms selected.*
