"""
generate_schematic.py — Visakhapatnam 8-stage source-to-tap chain schematic
Assignment A0, Part 2 | Student: Bera Yashwant Pavan Kumar | TechBharat C2-21

Saves city_schematic.png in the same directory as this script.
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch
import os

# ── Node definitions ───────────────────────────────────────────────────────────
# (label, sublabel, x, y, is_control_point)
NODES = [
    ("Source",          "Godavari/Yeleru\nRaiwada · Tatipudi\nMeghadrigedda",  0.5, 0.88, False),
    ("Intake +\nRaw Pump", "Kanithi Balancing\nReservoir (KBR)",               0.5, 0.74, False),
    ("WTP",             "11 Plants · 489 MLD\nRaiwada / Tatipudi\nNavara",     0.5, 0.60, False),
    ("Clear-Water\nSump (GLSR)",  "Master Balancing\nReservoir / GLSR\n★ PoC Control Pt 1",
                                                                                0.5, 0.46, True),
    ("Pumping\nStation",          "Zone-wise\nbooster pumps",                   0.5, 0.33, False),
    ("OHT / ESR",       "91–95 ELSRs · 38,820 kL\nTGR Nagar 2000kL\nSathivanipalem 1000kL\n★ PoC Control Pt 2",
                                                                                0.5, 0.20, True),
    ("Distribution\n(Zones/DMAs)", "72 Wards · 6 Zones\n50 DMAs planned\n(Madhurawada 24×7)", 0.5, 0.09, False),
    ("Consumers",       "~2.1M people\n135 LPCD norm\nIntermittent supply",    0.5, -0.02, False),
]

BOX_W  = 0.36
BOX_H  = 0.095

NORMAL_COLOR  = "#AED6F1"   # light blue
CONTROL_COLOR = "#F0B27A"   # orange — PoC control points
EDGE_COLOR    = "#1A5276"
ARROW_COLOR   = "#2E86C1"


def draw_box(ax, x, y, label, sublabel, is_ctrl):
    color = CONTROL_COLOR if is_ctrl else NORMAL_COLOR
    rect = mpatches.FancyBboxPatch(
        (x - BOX_W/2, y - BOX_H/2), BOX_W, BOX_H,
        boxstyle="round,pad=0.01",
        linewidth=2.5 if is_ctrl else 1.5,
        edgecolor="darkorange" if is_ctrl else EDGE_COLOR,
        facecolor=color,
        zorder=3
    )
    ax.add_patch(rect)

    # Main label (bold)
    ax.text(x - BOX_W/2 + 0.03, y + 0.012, label,
            fontsize=10, fontweight="bold", color="#1A252F",
            va="center", ha="left", zorder=4)

    # Sub-label (small, right side)
    ax.text(x + BOX_W/2 - 0.03, y - 0.005, sublabel,
            fontsize=6.5, color="#2C3E50",
            va="center", ha="right", zorder=4,
            linespacing=1.4)


def main():
    fig, ax = plt.subplots(figsize=(9, 13))
    ax.set_xlim(0, 1)
    ax.set_ylim(-0.1, 1.0)
    ax.axis("off")

    # Draw boxes
    for label, sublabel, x, y, is_ctrl in NODES:
        draw_box(ax, x, y, label, sublabel, is_ctrl)

    # Draw arrows between consecutive nodes
    for i in range(len(NODES) - 1):
        _, _, x0, y0, _ = NODES[i]
        _, _, x1, y1, _ = NODES[i + 1]
        ax.annotate("",
            xy=(x1, y1 + BOX_H/2 + 0.005),
            xytext=(x0, y0 - BOX_H/2 - 0.005),
            arrowprops=dict(
                arrowstyle="-|>",
                color=ARROW_COLOR,
                lw=1.8,
                mutation_scale=16
            ),
            zorder=2
        )

    # Legend
    ctrl_patch  = mpatches.Patch(color=CONTROL_COLOR, label="PoC Storage Control Point (★)")
    norm_patch  = mpatches.Patch(color=NORMAL_COLOR,  label="Standard infrastructure stage")
    ax.legend(handles=[ctrl_patch, norm_patch], loc="lower right",
              fontsize=9, framealpha=0.9, edgecolor="#999")

    # Title
    ax.set_title(
        "Visakhapatnam Water Supply — 8-Stage Source-to-Tap Chain\n"
        "Greater Visakhapatnam Municipal Corporation (GVMC)\n"
        "Orange boxes = PoC control points  |  TechBharat C2-21 · A0",
        fontsize=11, pad=12, color="#1A252F"
    )

    out_dir  = os.path.dirname(os.path.abspath(__file__))
    out_path = os.path.join(out_dir, "city_schematic.png")
    plt.tight_layout()
    plt.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Saved -> {out_path}")


if __name__ == "__main__":
    main()
