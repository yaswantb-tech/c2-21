# Visakhapatnam City Water System Map
**Assignment A0 — Domain Explorer | Part 2**
**Student:** Bera Yashwant Pavan Kumar | **Cohort:** TechBharat C2-21

---

## 1. Main Water Sources and Water Treatment Plants (WTPs)

Greater Visakhapatnam Municipal Corporation (GVMC) serves a population of ~2.1–2.3 million across its jurisdiction with an actual daily supply of **~380–410 MLD** against a demand approaching **~450–490 MLD**.

### Primary Water Sources

| # | Source | Type | Contribution (MLD) | Distance |
|---|--------|------|-------------------|---------|
| 1 | **Godavari River / Yeleru Reservoir System** (via Yeleru Left Main Canal) | River + Reservoir | ~**182 MLD** (≈48 % of supply mix) | ~190 km |
| 2 | **Raiwada Reservoir** (on River Sarada) | Surface reservoir | ~**72.5 MLD** (≈19 %) | ~65 km |
| 3 | **Tatipudi (Thatipudi) Reservoir** (on Gosthani River) | Surface reservoir | ~**45 MLD** (≈12 %) | ~70 km |
| 4 | **Meghadrigedda Reservoir** (Dronamraju Satyanarayana Reservoir) | Intra-city reservoir, est. 1977 | ~**41–50 MLD** | Within city |
| 5 | **Gosthani River Infiltration Wells** (Tagarapuvalasa) | Sub-surface wells | ~**22 MLD** | ~40 km |
| 6 | **Mudasarlova Reservoir** | Historic urban tank, built 1902 | ~**2.3–4.5 MLD** | Within city |
| 7 | **Gambheeramgedda Reservoir** | Seasonal supplementary | Minor/seasonal | Within city |

> The **Kanithi Balancing Reservoir (KBR)** is the main aggregation hub that receives Yeleru/Godavari canal water before onward treatment and distribution to both GVMC (domestic) and industrial users (RINL Steel, NTPC).
>
> *Source: [neervazhvu.org — Visakhapatnam Water Sector Research](https://neervazhvu.org); [Wikipedia — Meghadrigedda Reservoir](https://en.wikipedia.org/wiki/Meghadrigedda_Reservoir)*

### Water Treatment Plants (WTPs)

GVMC operates **11 WTPs** with a combined installed capacity of ~**489 MLD**.

| # | WTP | Raw Water Source | Capacity (MLD) |
|---|-----|-----------------|----------------|
| 1 | **Raiwada WTP** | Raiwada Reservoir | 72.5 |
| 2 | **Tatipudi WTP** | Tatipudi Reservoir | 45 |
| 3 | **Meghadrigedda WTP** | Meghadrigedda Reservoir | 41–50 |
| 4 | **Narava WTP** | Yeleru/Raiwada pipeline mains | ~42 |
| 5 | **Madhurawada WTP** *(under construction)* | Godavari system | **65** (new) |
| 6–11 | Various zonal/seasonal WTPs | Mixed | Balance of 489 MLD |

> *Sources: [neervazhvu.org](https://neervazhvu.org); [The Hindu — Madhurawada 65 MLD WTP / ₹725 cr Urban Challenge Fund project](https://www.thehindu.com); [Deccan Chronicle — GVMC treatment infrastructure](https://www.deccanchronicle.com)*

---

## 2. Overhead Tanks (OHTs / ELSRs) — At Least Three Named

GVMC maintains approximately **91–95 Elevated Service Reservoirs (ELSRs)** with a combined overhead storage of ~**38,820 kL**. Selected named tanks:

| # | OHT / ELSR Name | Zone / Location | Capacity (kL) | Scheme |
|---|-----------------|-----------------|---------------|--------|
| 1 | **TGR Nagar ELSR** | Gajuwaka Zone (Zone VI), Ward 74 | **2,000 kL** | AMRUT |
| 2 | **Nalla Quarry (Pulagalapalem) ELSR** | Pendurthi Zone (Zone VIII), Ward 96 | **1,000 kL** | AMRUT |
| 3 | **Sathivanipalem ELSR** | Gajuwaka Zone (Zone VI), Ward 88 | **1,000 kL** | AMRUT |
| 4 | **Revenue Colony ELSR** | Madhurawada Zone (Zone II) | **1,000 kL** | AMRUT Phase 2 |
| 5 | **Venkateswarametta GLSR** | Bheemunipatnam Zone | **1,800 kL** | AMRUT 2.0 |
| 6 | **Islam Peta ELSR** | Old City / Central Zone | 150 kL | GVMC Existing |
| 7 | **Pedda Palem Village ELSR** | Old City / Central Zone | 250 kL | GVMC Existing |

> *Sources: [MOHUA AMRUT project sheets for GVMC — Visakhapatnam](https://www.mohua.gov.in); [GVMC official portal](https://www.gvmc.gov.in); [GVMC asset register (Scribd)](https://www.scribd.com)*

---

## 3. Supply Schedule

| Parameter | Detail |
|-----------|--------|
| **Mode (citywide)** | **Intermittent** — once or twice daily |
| **Morning window** | ~05:00 – 11:00 (varies by zone/elevation) |
| **Evening window** | ~18:00 – 21:00 (not all areas) |
| **Duration per cycle** | 1–3 hours at consumer tap |
| **High-elevation / tail-end areas** | Once every 2–3 days in summer |
| **24×7 pilot zones** | Madhavadhara, Muralinagar, Marripalem (ADB-assisted) |
| **Planned 24×7 expansion** | Madhurawada Zone-II (₹725 crore, Smart City / UCF — SCADA, 50 DMAs, AMI meters) |

> *Sources: [GVMC official supply schedule](https://www.gvmc.gov.in); [The Coastal Times Visakhapatnam](https://www.thecoastaltimes.in); [ProjectsToday — ADB 24×7 zones](https://www.projectstoday.ai)*

---

## 4. Real Incident — Summer 2024 Acute Water Crisis

**Date:** April – May 2024 (peak summer)
**Type:** Citywide water shortage → tanker supply overload → inequitable distribution

### What Happened
Municipal tap supply in localities including Seethammadhara, Madhurawada, Arilova, Yendada, PM Palem, and Gajuwaka dropped to once every **2–3 days** for short intervals. Borewells across residential hubs ran dry even at depths of 500–800 feet. Large apartment complexes needed 10–20 private tanker loads per day for basic domestic needs.

### Root Cause — Mapped to Utility Failure Modes

| Failure Mode | Manifestation in Visakhapatnam 2024 |
|---|---|
| **Water shortage** | El Niño-driven 2023 monsoon deficit depleted local reservoirs (Mudasarlova completely dry; Meghadrigedda, Raiwada, Tatipudi at critically low levels) |
| **Inefficient pumping** | Increased pump run-time and energy cost as GVMC pushed Godavari/Yeleru supply harder (~60 % dependence) to compensate for failed local sources |
| **Poor replenishment scheduling** | ESR filling windows fell short — OHTs in peripheral zones (Pendurthi, Bhimili) could not be refilled daily due to pipeline capacity bottleneck |
| **Uneven distribution** | High-elevation areas (Madhurawada hilltop colonies, PM Palem) received supply once every 2–3 days; low-lying Gajuwaka received more frequently |
| **Reduced service continuity** | Dial-A-Tanker emergency tanker deployments scaled up; private tanker prices inflated to ₹3,000–₹6,000 per load (vs. official GVMC rate); IT parks (Infosys, Cognizant) instructed to cut non-essential water use |

> *Sources: [Deccan Chronicle — Visakhapatnam summer 2024 crisis](https://www.deccanchronicle.com); [The Hindu — Vizag apartment/borewell distress, May 2024](https://www.thehindu.com); [Times of India — tanker price exploitation](https://timesofindia.indiatimes.com)*

**Secondary Incident:** A major drinking-water main **burst at Hanumanthawaka junction** in September 2023 — high-pressure water shot up several stories, roads flooded, thousands of litres wasted over several hours before the valve was isolated. Root cause: ageing pipeline joint failure.
> *Source: [NTV Telugu — Hanumanthawaka pipeline burst, September 2023](https://www.ntvtelugu.com)*

---

## 5. City Schematic

The 8-stage source-to-tap chain is visualised in `city_schematic.png` (generated by `generate_schematic.py`). The two **PoC storage control points** (Clear-Water Sump/GLSR and OHT/ELSR) are highlighted in orange.

> See [`city_schematic.png`](city_schematic.png) in this folder.

---

*All factual claims cited with direct sources above.*
