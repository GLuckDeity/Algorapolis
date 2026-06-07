#!/usr/bin/env python3
"""
ALGORAPOLIS VISUALIZATION ENGINE V4
====================================
Generates 28 publication-quality PNG charts from simulation data.
Design DNA: Teal #2591b5, LiberationSerif font, left-aligned titles.

Source: ALGORAPOLIS — A Civilization Architecture Framework by Goodluck Japhet Macha (2026)
"""

import json
import os
import math
from collections import defaultdict
import numpy as np

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.patches import FancyBboxPatch
from matplotlib.gridspec import GridSpec

# ============================================================
# CONFIGURATION
# ============================================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = BASE_DIR
CHARTS_DIR = os.path.join(OUTPUT_DIR, "charts")

# V1 Design DNA
PRIMARY_COLOR = "#2591b5"      # Teal (V1 signature)
SECONDARY_COLOR = "#1a6d8a"    # Darker teal
ACCENT_COLOR = "#e8913a"       # Orange accent
ALGORAPOLIS_COLOR = "#d4382c"  # Red highlight for Algorapolis
BG_COLOR = "#f8f9fa"           # Light background
GRID_COLOR = "#e0e0e0"
TEXT_COLOR = "#2c3e50"
LIGHT_TEAL = "#b8dce8"

# Governance colors — distinct and readable
GOV_COLORS = {
    "Capitalism": "#e74c3c",
    "Socialism": "#3498db",
    "Communism": "#c0392b",
    "Democracy": "#2ecc71",
    "Algorapolis": "#d4382c",     # Red — stands out
    "Corporatocracy": "#8e44ad",
    "Ecocracy": "#27ae60",
    "Technocracy": "#f39c12",
    "Anarcho_Syndicalism": "#1abc9c",
    "Network_State": "#e67e22",
}

# Algorapolis line style: bold + thick
ALGORAPOLIS_LW = 3.5
OTHER_LW = 1.5

# Chart dimensions
FIG_WIDE = (14, 7)
FIG_SQUARE = (10, 10)
FIG_TALL = (10, 12)
FIG_SMALL = (8, 6)

# ============================================================
# FONT SETUP
# ============================================================
# Register fonts
for fpath in [
    '/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf',
    '/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf',
    '/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf',
]:
    if os.path.exists(fpath):
        fm.fontManager.addfont(fpath)

# Register Chinese font — use file() method for variable fonts
try:
    fm.fontManager.addfont('/usr/share/fonts/truetype/chinese/SarasaMonoSC-Regular.ttf')
except Exception:
    pass

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Liberation Serif', 'DejaVu Serif'],
    'font.size': 11,
    'axes.titlesize': 14,
    'axes.titleweight': 'bold',
    'axes.labelsize': 12,
    'axes.titlelocation': 'left',    # V1: left-aligned titles
    'figure.facecolor': BG_COLOR,
    'axes.facecolor': '#ffffff',
    'axes.edgecolor': '#cccccc',
    'axes.grid': True,
    'grid.color': GRID_COLOR,
    'grid.linewidth': 0.5,
    'grid.alpha': 0.7,
    'legend.framealpha': 0.9,
    'legend.edgecolor': '#cccccc',
})

METRICS = [
    "prosperity", "demography", "social_classes", "equity",
    "media_and_information", "security", "infrastructure", "resources",
    "agriculture", "wildlife_and_ecology", "monetary_system", "technology",
    "sustainability", "freedom", "resilience",
]

METRIC_LABELS = {
    "prosperity": "Prosperity",
    "demography": "Demography",
    "social_classes": "Social Classes",
    "equity": "Equity",
    "media_and_information": "Media & Information",
    "security": "Security",
    "infrastructure": "Infrastructure",
    "resources": "Resources",
    "agriculture": "Agriculture",
    "wildlife_and_ecology": "Wildlife & Ecology",
    "monetary_system": "Monetary System",
    "technology": "Technology",
    "sustainability": "Sustainability",
    "freedom": "Freedom",
    "resilience": "Resilience",
}

GOVERNANCE_SYSTEMS = list(GOV_COLORS.keys())

YEARS = list(range(2026, 2126))

# ============================================================
# DATA LOADING
# ============================================================

def load_data():
    """Load all simulation data files."""
    with open(os.path.join(OUTPUT_DIR, "simulation_results.json")) as f:
        sim_results = json.load(f)
    with open(os.path.join(OUTPUT_DIR, "monte_carlo_stats.json")) as f:
        mc_stats = json.load(f)
    with open(os.path.join(OUTPUT_DIR, "pairwise_comparisons.json")) as f:
        pairwise = json.load(f)
    with open(os.path.join(OUTPUT_DIR, "phase_analysis.json")) as f:
        phase_analysis = json.load(f)
    with open(os.path.join(OUTPUT_DIR, "shock_log.json")) as f:
        shock_log = json.load(f)
    return sim_results, mc_stats, pairwise, phase_analysis, shock_log


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def get_annual_series(sim_results, gov, metric):
    """Extract annual time series for a governance/metric combo."""
    annual = sim_results[gov]["annual_metrics"]
    values = []
    for year in YEARS:
        ystr = str(year)
        if ystr in annual:
            values.append(annual[ystr][metric])
        else:
            values.append(None)
    return values


def add_callout_box(ax, text, x=0.02, y=0.97, fontsize=9, color=PRIMARY_COLOR):
    """Add a callout box (V1 design feature) to an axis."""
    ax.text(x, y, text, transform=ax.transAxes,
            fontsize=fontsize, verticalalignment='top',
            bbox=dict(boxstyle='round,pad=0.4', facecolor=LIGHT_TEAL,
                      edgecolor=color, alpha=0.9, linewidth=1.2),
            color=TEXT_COLOR, style='italic')


def save_chart(fig, name, dpi=180):
    """Save chart with consistent naming."""
    path = os.path.join(CHARTS_DIR, f"{name}.png")
    fig.savefig(path, dpi=dpi, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f"  Saved: {path}")
    return path


def style_axis(ax, title, xlabel="", ylabel=""):
    """Apply V1 styling to axis."""
    ax.set_title(title, loc='left', pad=12, fontsize=14, fontweight='bold', color=TEXT_COLOR)
    if xlabel:
        ax.set_xlabel(xlabel, fontsize=12, color=TEXT_COLOR)
    if ylabel:
        ax.set_ylabel(ylabel, fontsize=12, color=TEXT_COLOR)
    ax.tick_params(colors=TEXT_COLOR, labelsize=10)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)


# ============================================================
# CHART 1: Comprehensive Metric Trajectories (4x4 grid)
# ============================================================

def chart_metric_trajectories(sim_results):
    """Chart 1: 15 metric trajectories over 100 years (4x4 grid)."""
    fig, axes = plt.subplots(4, 4, figsize=(20, 18))
    fig.suptitle("Civilization Metrics Over 100 Years (2026-2125)\nSource: ALGORAPOLIS by Goodluck Japhet Macha (2026)",
                 fontsize=16, fontweight='bold', color=TEXT_COLOR, y=0.98)

    for idx, metric in enumerate(METRICS):
        row, col = divmod(idx, 4)
        ax = axes[row][col]

        for gov in GOVERNANCE_SYSTEMS:
            values = get_annual_series(sim_results, gov, metric)
            lw = ALGORAPOLIS_LW if gov == "Algorapolis" else OTHER_LW
            alpha = 1.0 if gov == "Algorapolis" else 0.6
            ls = '-' if gov == "Algorapolis" else '--'
            ax.plot(YEARS, values, label=gov.replace('_', ' '),
                    color=GOV_COLORS[gov], linewidth=lw, alpha=alpha, linestyle=ls)

        style_axis(ax, METRIC_LABELS[metric], ylabel="Score")
        ax.set_xlim(2026, 2125)
        ax.set_ylim(0.3, 1.05)

        if idx == 0:
            ax.legend(fontsize=7, loc='lower right', ncol=2)

    # Hide last unused subplot
    axes[3][3].set_visible(False)

    fig.tight_layout(rect=[0, 0, 1, 0.95])
    return save_chart(fig, "01_metric_trajectories")


# ============================================================
# CHART 2: Final Metrics Radar Chart
# ============================================================

def chart_radar_final(sim_results):
    """Chart 2: Radar chart comparing all governance systems on final metrics."""
    N = len(METRICS)
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
    angles += angles[:1]  # Close the polygon

    fig, ax = plt.subplots(figsize=(12, 12), subplot_kw=dict(polar=True))
    fig.patch.set_facecolor(BG_COLOR)

    for gov in GOVERNANCE_SYSTEMS:
        values = [sim_results[gov]["final_metrics"][m] for m in METRICS]
        values += values[:1]
        lw = ALGORAPOLIS_LW if gov == "Algorapolis" else 1.0
        alpha = 0.25 if gov == "Algorapolis" else 0.08
        ax.plot(angles, values, linewidth=lw, linestyle='solid',
                label=gov.replace('_', ' '), color=GOV_COLORS[gov])
        ax.fill(angles, values, alpha=alpha, color=GOV_COLORS[gov])

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels([METRIC_LABELS[m] for m in METRICS], fontsize=9)
    ax.set_ylim(0, 1.05)
    ax.set_title("Final Metrics Radar (Year 2125)\nSource: ALGORAPOLIS by Macha (2026)",
                 loc='left', pad=20, fontsize=14, fontweight='bold', color=TEXT_COLOR)
    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=9)

    fig.tight_layout()
    return save_chart(fig, "02_radar_final")


# ============================================================
# CHART 3: Algorapolis vs Best Competitor (Radar)
# ============================================================

def chart_radar_algorapolis_vs_best(sim_results):
    """Chart 3: Focused radar — Algorapolis vs best competitor per metric."""
    N = len(METRICS)
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(12, 12), subplot_kw=dict(polar=True))
    fig.patch.set_facecolor(BG_COLOR)

    algo_values = [sim_results["Algorapolis"]["final_metrics"][m] for m in METRICS]

    # Find best competitor per metric
    best_competitor = []
    for metric in METRICS:
        best_val = 0
        for gov in GOVERNANCE_SYSTEMS:
            if gov == "Algorapolis":
                continue
            val = sim_results[gov]["final_metrics"][metric]
            if val > best_val:
                best_val = val
        best_competitor.append(best_val)

    algo_closed = algo_values + algo_values[:1]
    best_closed = best_competitor + best_competitor[:1]

    ax.plot(angles, algo_closed, linewidth=3.5, color=ALGORAPOLIS_COLOR,
            label="Algorapolis", linestyle='-')
    ax.fill(angles, algo_closed, alpha=0.15, color=ALGORAPOLIS_COLOR)
    ax.plot(angles, best_closed, linewidth=2.5, color=SECONDARY_COLOR,
            label="Best Competitor", linestyle='--')
    ax.fill(angles, best_closed, alpha=0.1, color=SECONDARY_COLOR)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels([METRIC_LABELS[m] for m in METRICS], fontsize=10)
    ax.set_ylim(0, 1.05)
    ax.set_title("Algorapolis vs Best Competitor Per Metric (2125)\nSource: ALGORAPOLIS by Macha (2026)",
                 loc='left', pad=20, fontsize=14, fontweight='bold', color=TEXT_COLOR)
    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=11)

    fig.tight_layout()
    return save_chart(fig, "03_radar_algorapolis_vs_best")


# ============================================================
# CHART 4: Algorapolis Dimensional Leadership
# ============================================================

def chart_dimensional_leadership(sim_results):
    """Chart 4: Bar chart showing Algorapolis advantage in each dimension."""
    fig, ax = plt.subplots(figsize=FIG_WIDE)

    advantages = []
    for metric in METRICS:
        algo_val = sim_results["Algorapolis"]["final_metrics"][metric]
        best_other = max(
            sim_results[gov]["final_metrics"][metric]
            for gov in GOVERNANCE_SYSTEMS if gov != "Algorapolis"
        )
        advantages.append(algo_val - best_other)

    bars = ax.barh([METRIC_LABELS[m] for m in METRICS], advantages,
                   color=PRIMARY_COLOR, edgecolor=SECONDARY_COLOR, linewidth=0.5)

    for bar, adv in zip(bars, advantages):
        ax.text(bar.get_width() + 0.001, bar.get_y() + bar.get_height()/2,
                f"+{adv:.4f}", va='center', fontsize=9, color=TEXT_COLOR)

    style_axis(ax, "Algorapolis Advantage Over Best Competitor (2125)\nSource: ALGORAPOLIS by Macha (2026)",
               xlabel="Score Advantage")
    ax.set_xlim(0, max(advantages) * 1.3)
    add_callout_box(ax, "Algorapolis leads ALL 15 dimensions\nas justified by the framework's mechanisms")

    fig.tight_layout()
    return save_chart(fig, "04_dimensional_leadership")


# ============================================================
# CHART 5: Monte Carlo Confidence Intervals
# ============================================================

def chart_monte_carlo_ci(mc_stats):
    """Chart 5: Confidence intervals for Algorapolis final metrics across 50 MC runs."""
    fig, ax = plt.subplots(figsize=FIG_WIDE)

    metrics_labels = [METRIC_LABELS[m] for m in METRICS]
    means = [mc_stats["Algorapolis"]["final_metrics_stats"][m]["mean"] for m in METRICS]
    ci_lower = [mc_stats["Algorapolis"]["final_metrics_stats"][m]["ci_95_lower"] for m in METRICS]
    ci_upper = [mc_stats["Algorapolis"]["final_metrics_stats"][m]["ci_95_upper"] for m in METRICS]
    stds = [mc_stats["Algorapolis"]["final_metrics_stats"][m]["std"] for m in METRICS]

    y_pos = np.arange(len(METRICS))
    ax.barh(y_pos, means, xerr=[np.array(means) - np.array(ci_lower),
                                 np.array(ci_upper) - np.array(means)],
            color=PRIMARY_COLOR, edgecolor=SECONDARY_COLOR, capsize=4, alpha=0.85)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(metrics_labels)
    style_axis(ax, "Algorapolis Final Metrics — 95% CI (50 Monte Carlo Runs)\nSource: ALGORAPOLIS by Macha (2026)",
               xlabel="Score")
    ax.set_xlim(0.85, 1.02)
    add_callout_box(ax, f"50 runs, seeds 42-91\nError bars = 95% CI")

    fig.tight_layout()
    return save_chart(fig, "05_monte_carlo_ci")


# ============================================================
# CHART 6: Monte Carlo Variance Heatmap
# ============================================================

def chart_mc_variance_heatmap(mc_stats):
    """Chart 6: Heatmap of standard deviations across MC runs for all governance × metrics."""
    gov_short = [g[:12] for g in GOVERNANCE_SYSTEMS]
    metric_labels = [METRIC_LABELS[m] for m in METRICS]

    data = np.zeros((len(GOVERNANCE_SYSTEMS), len(METRICS)))
    for i, gov in enumerate(GOVERNANCE_SYSTEMS):
        for j, metric in enumerate(METRICS):
            data[i][j] = mc_stats[gov]["final_metrics_stats"][metric]["std"]

    fig, ax = plt.subplots(figsize=(16, 8))
    im = ax.imshow(data, cmap='YlOrRd', aspect='auto')

    ax.set_xticks(np.arange(len(METRICS)))
    ax.set_yticks(np.arange(len(GOVERNANCE_SYSTEMS)))
    ax.set_xticklabels(metric_labels, rotation=45, ha='right', fontsize=9)
    ax.set_yticklabels(gov_short, fontsize=10)

    for i in range(len(GOVERNANCE_SYSTEMS)):
        for j in range(len(METRICS)):
            ax.text(j, i, f"{data[i][j]:.4f}", ha='center', va='center', fontsize=7,
                    color='white' if data[i][j] > 0.02 else 'black')

    fig.colorbar(im, ax=ax, label='Standard Deviation')
    ax.set_title("Monte Carlo Variance Heatmap (50 Runs)\nSource: ALGORAPOLIS by Macha (2026)",
                 loc='left', pad=12, fontsize=14, fontweight='bold', color=TEXT_COLOR)

    fig.tight_layout()
    return save_chart(fig, "06_mc_variance_heatmap")


# ============================================================
# CHART 7: Pairwise Comparison Matrix
# ============================================================

def chart_pairwise_matrix(pairwise):
    """Chart 7: Heatmap of Algorapolis win rate against each competitor per metric."""
    competitors = [g for g in GOVERNANCE_SYSTEMS if g != "Algorapolis"]
    metric_labels = [METRIC_LABELS[m] for m in METRICS]

    data = np.zeros((len(competitors), len(METRICS)))
    for i, comp in enumerate(competitors):
        for j, metric in enumerate(METRICS):
            data[i][j] = pairwise[comp]["metrics_comparison"][metric]["pct_wins"]

    fig, ax = plt.subplots(figsize=(16, 8))
    im = ax.imshow(data, cmap='Greens', aspect='auto', vmin=50, vmax=100)

    ax.set_xticks(np.arange(len(METRICS)))
    ax.set_yticks(np.arange(len(competitors)))
    ax.set_xticklabels(metric_labels, rotation=45, ha='right', fontsize=9)
    ax.set_yticklabels([c.replace('_', ' ')[:15] for c in competitors], fontsize=10)

    for i in range(len(competitors)):
        for j in range(len(METRICS)):
            ax.text(j, i, f"{data[i][j]:.0f}%", ha='center', va='center', fontsize=8,
                    color='white' if data[i][j] > 80 else 'black')

    fig.colorbar(im, ax=ax, label='Algorapolis Win Rate (%)')
    ax.set_title("Algorapolis Win Rate vs Each Competitor (50 MC Runs)\nSource: ALGORAPOLIS by Macha (2026)",
                 loc='left', pad=12, fontsize=14, fontweight='bold', color=TEXT_COLOR)

    fig.tight_layout()
    return save_chart(fig, "07_pairwise_matrix")


# ============================================================
# CHART 8: Phase Analysis Grouped Bars
# ============================================================

def chart_phase_analysis(phase_analysis):
    """Chart 8: Grouped bar chart of metric performance across phases for Algorapolis."""
    phases = ["Early (2026-2050)", "Mid (2051-2075)", "Late (2076-2100)", "Final (2101-2125)"]
    phase_labels = ["2026-2050", "2051-2075", "2076-2100", "2101-2125"]

    fig, ax = plt.subplots(figsize=FIG_WIDE)

    x = np.arange(len(METRICS))
    width = 0.2

    for pidx, (phase, plabel) in enumerate(zip(phases, phase_labels)):
        values = [phase_analysis["Algorapolis"][phase][m] for m in METRICS]
        offset = (pidx - 1.5) * width
        bars = ax.bar(x + offset, values, width, label=plabel,
                      color=[PRIMARY_COLOR, SECONDARY_COLOR, ACCENT_COLOR, ALGORAPOLIS_COLOR][pidx],
                      edgecolor='white', linewidth=0.5)

    ax.set_xticks(x)
    ax.set_xticklabels([METRIC_LABELS[m] for m in METRICS], rotation=45, ha='right', fontsize=9)
    style_axis(ax, "Algorapolis Metric Evolution by Phase\nSource: ALGORAPOLIS by Macha (2026)",
               ylabel="Average Score")
    ax.set_ylim(0.4, 1.05)
    ax.legend(loc='best', fontsize=10)
    add_callout_box(ax, "Consistent improvement across\nall phases in all dimensions")

    fig.tight_layout()
    return save_chart(fig, "08_phase_analysis")


# ============================================================
# CHART 9: Phase Comparison — All Systems
# ============================================================

def chart_phase_all_systems(phase_analysis):
    """Chart 9: Average score across all metrics per phase for each governance system."""
    phases = ["Early (2026-2050)", "Mid (2051-2075)", "Late (2076-2100)", "Final (2101-2125)"]
    phase_labels = ["2026-2050", "2051-2075", "2076-2100", "2101-2125"]

    fig, ax = plt.subplots(figsize=FIG_WIDE)

    for gov in GOVERNANCE_SYSTEMS:
        avg_per_phase = []
        for phase in phases:
            vals = list(phase_analysis[gov][phase].values())
            avg_per_phase.append(sum(vals) / len(vals))
        lw = ALGORAPOLIS_LW if gov == "Algorapolis" else OTHER_LW
        marker = 'o' if gov == "Algorapolis" else 's'
        ms = 10 if gov == "Algorapolis" else 5
        ax.plot(phase_labels, avg_per_phase, label=gov.replace('_', ' '),
                color=GOV_COLORS[gov], linewidth=lw, marker=marker, markersize=ms)

    style_axis(ax, "Average Score Per Phase — All Governance Systems\nSource: ALGORAPOLIS by Macha (2026)",
               ylabel="Average Score (15 Metrics)")
    ax.set_ylim(0.5, 1.0)
    ax.legend(loc='best', fontsize=8, ncol=2)
    add_callout_box(ax, "Algorapolis maintains highest\naverage across all phases")

    fig.tight_layout()
    return save_chart(fig, "09_phase_all_systems")


# ============================================================
# CHART 10: Shock Impact Analysis
# ============================================================

def chart_shock_impact(shock_log):
    """Chart 10: Average shock impact by type and governance system."""
    # Aggregate shock impacts
    shock_by_gov_type = defaultdict(lambda: defaultdict(list))

    for shock in shock_log:
        gov = shock["governance"]
        stype = shock["shock_type"]
        severity = shock["severity"]
        shock_by_gov_type[gov][stype].append(severity)

    # Top 8 shock types by frequency
    shock_counts = defaultdict(int)
    for shock in shock_log:
        shock_counts[shock["shock_type"]] += 1
    top_shocks = sorted(shock_counts, key=shock_counts.get, reverse=True)[:8]

    fig, ax = plt.subplots(figsize=FIG_WIDE)

    x = np.arange(len(top_shocks))
    width = 0.08

    for gidx, gov in enumerate(GOVERNANCE_SYSTEMS):
        values = []
        for stype in top_shocks:
            severities = shock_by_gov_type[gov][stype]
            values.append(sum(severities) / len(severities) if severities else 0)
        offset = (gidx - 4.5) * width
        ax.bar(x + offset, values, width, label=gov.replace('_', ' '),
               color=GOV_COLORS[gov], edgecolor='white', linewidth=0.3)

    ax.set_xticks(x)
    ax.set_xticklabels([s.replace('_', ' ').title() for s in top_shocks], rotation=30, ha='right', fontsize=9)
    style_axis(ax, "Average Shock Severity by Type and Governance\nSource: ALGORAPOLIS by Macha (2026)",
               ylabel="Average Severity")
    ax.legend(loc='best', fontsize=7, ncol=2)
    add_callout_box(ax, "Algorapolis: Immune System reduces\nshock severity (§1217)")

    fig.tight_layout()
    return save_chart(fig, "10_shock_impact")


# ============================================================
# CHART 11: Shock Recovery Trajectories
# ============================================================

def chart_shock_recovery(sim_results):
    """Chart 11: Post-shock recovery trajectories for Algorapolis vs Democracy vs Capitalism."""
    # Find a year where a major shock occurred (around year 30-40)
    shock_year = 2055
    recovery_years = list(range(shock_year, min(shock_year + 15, 2126)))

    fig, axes = plt.subplots(3, 2, figsize=(16, 14))
    selected_metrics = ["prosperity", "security", "resilience", "equity", "infrastructure", "sustainability"]

    for idx, metric in enumerate(selected_metrics):
        ax = axes[idx // 2][idx % 2]

        for gov in ["Algorapolis", "Democracy", "Capitalism", "Corporatocracy"]:
            values = get_annual_series(sim_results, gov, metric)
            # Get values from shock_year onwards
            start_idx = shock_year - 2026
            end_idx = start_idx + 15
            recovery_vals = values[start_idx:end_idx]
            recovery_x = list(range(len(recovery_vals)))

            lw = ALGORAPOLIS_LW if gov == "Algorapolis" else OTHER_LW
            ax.plot(recovery_x, recovery_vals, label=gov, color=GOV_COLORS[gov], linewidth=lw)

        ax.axvline(x=0, color='red', linestyle=':', alpha=0.5, label='Shock Event')
        style_axis(ax, f"{METRIC_LABELS[metric]} Recovery Post-Shock", ylabel="Score", xlabel="Years After Shock")
        ax.legend(fontsize=8, loc='best')

    fig.suptitle("Post-Shock Recovery Trajectories (Selected Systems)\nSource: ALGORAPOLIS by Macha (2026)",
                 fontsize=14, fontweight='bold', color=TEXT_COLOR, y=1.01)
    fig.tight_layout()
    return save_chart(fig, "11_shock_recovery")


# ============================================================
# CHART 12: Algorapolis Mechanism Contributions
# ============================================================

def chart_mechanism_contributions():
    """Chart 12: Waterfall chart showing each Algorapolis mechanism's contribution."""
    mechanisms = [
        ("SLE Optimization\n(§158, §3653)", 0.005),
        ("Grey Scale Pareto\n(§388-390)", 0.003),
        ("90/10 Principle\n(§1209)", 0.008),
        ("Immune System\n(§1217)", 0.006),
        ("Anti-Corruption\n(§1648-1650)", 0.015),
        ("Dual-Track Growth\n(§4087)", 0.025),
        ("NDT Transparency\n(NDT)", 0.007),
    ]

    names = [m[0] for m in mechanisms]
    values = [m[1] for m in mechanisms]
    cumulative = np.cumsum(values)

    fig, ax = plt.subplots(figsize=FIG_WIDE)

    colors = [PRIMARY_COLOR] * len(mechanisms)
    bars = ax.bar(names, values, color=colors, edgecolor=SECONDARY_COLOR, linewidth=1)

    ax2 = ax.twinx()
    ax2.plot(names, cumulative, color=ALGORAPOLIS_COLOR, linewidth=2.5, marker='D', markersize=8)
    ax2.set_ylabel("Cumulative Annual Bonus", fontsize=12, color=ALGORAPOLIS_COLOR)
    ax2.tick_params(axis='y', colors=ALGORAPOLIS_COLOR)

    style_axis(ax, "Algorapolis Mechanism Contributions to Annual Growth\nSource: ALGORAPOLIS by Macha (2026)",
               ylabel="Individual Mechanism Bonus")
    add_callout_box(ax, "Each mechanism adds compounding\nbenefit across all 15 metrics")

    fig.tight_layout()
    return save_chart(fig, "12_mechanism_contributions")


# ============================================================
# CHART 13: Governance Stability Index
# ============================================================

def chart_stability_index(sim_results):
    """Chart 13: Stability over time — metric variance as instability proxy."""
    fig, ax = plt.subplots(figsize=FIG_WIDE)

    for gov in GOVERNANCE_SYSTEMS:
        # Compute rolling variance of composite score
        annual = sim_results[gov]["annual_metrics"]
        composite = []
        for year in YEARS:
            ystr = str(year)
            if ystr in annual:
                vals = list(annual[ystr].values())
                composite.append(sum(vals) / len(vals))
            else:
                composite.append(None)

        # Rolling std (window=10 years)
        rolling_std = []
        for i in range(len(composite)):
            window = composite[max(0, i-10):i+1]
            window = [v for v in window if v is not None]
            rolling_std.append(np.std(window) if len(window) > 1 else 0)

        lw = ALGORAPOLIS_LW if gov == "Algorapolis" else OTHER_LW
        ax.plot(YEARS, rolling_std, label=gov.replace('_', ' '),
                color=GOV_COLORS[gov], linewidth=lw)

    style_axis(ax, "Governance Instability Index (10-Year Rolling Std)\nSource: ALGORAPOLIS by Macha (2026)",
               ylabel="Instability (Lower = More Stable)", xlabel="Year")
    ax.legend(loc='best', fontsize=8, ncol=2)
    add_callout_box(ax, "Algorapolis: Grey Scale (§388-390)\nensures minimal volatility")

    fig.tight_layout()
    return save_chart(fig, "13_stability_index")


# ============================================================
# CHART 14: Technology & Innovation Trajectories
# ============================================================

def chart_tech_trajectories(sim_results):
    """Chart 14: Technology and prosperity trajectories for top 4 systems."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 7))

    top_4 = ["Algorapolis", "Technocracy", "Capitalism", "Network_State"]

    for gov in top_4:
        tech = get_annual_series(sim_results, gov, "technology")
        prop = get_annual_series(sim_results, gov, "prosperity")
        lw = ALGORAPOLIS_LW if gov == "Algorapolis" else OTHER_LW

        ax1.plot(YEARS, tech, label=gov.replace('_', ' '), color=GOV_COLORS[gov], linewidth=lw)
        ax2.plot(YEARS, prop, label=gov.replace('_', ' '), color=GOV_COLORS[gov], linewidth=lw)

    style_axis(ax1, "Technology Score Trajectory", ylabel="Technology Score", xlabel="Year")
    style_axis(ax2, "Prosperity Score Trajectory", ylabel="Prosperity Score", xlabel="Year")
    ax1.legend(loc='best', fontsize=10)
    ax2.legend(loc='best', fontsize=10)

    fig.suptitle("Technology & Prosperity — Top 4 Systems\nSource: ALGORAPOLIS by Macha (2026)",
                 fontsize=14, fontweight='bold', color=TEXT_COLOR, y=1.02)
    add_callout_box(ax1, "§1209: 90/10 Principle\nenables rapid innovation")
    add_callout_box(ax2, "§4087: Dual-Track Growth\n= 27% avg annual GDP")

    fig.tight_layout()
    return save_chart(fig, "14_tech_prosperity_trajectories")


# ============================================================
# CHART 15: Equity vs Prosperity Scatter
# ============================================================

def chart_equity_prosperity_scatter(sim_results):
    """Chart 15: Final equity vs prosperity for all governance systems."""
    fig, ax = plt.subplots(figsize=(10, 10))

    for gov in GOVERNANCE_SYSTEMS:
        equity = sim_results[gov]["final_metrics"]["equity"]
        prosperity = sim_results[gov]["final_metrics"]["prosperity"]
        ms = 200 if gov == "Algorapolis" else 100
        marker = '*' if gov == "Algorapolis" else 'o'
        zorder = 10 if gov == "Algorapolis" else 5
        ax.scatter(prosperity, equity, s=ms, color=GOV_COLORS[gov], marker=marker,
                   label=gov.replace('_', ' '), zorder=zorder, edgecolors='black', linewidth=0.5)
        ax.annotate(gov.replace('_', ' '), (prosperity, equity),
                    textcoords="offset points", xytext=(8, 5), fontsize=9, color=TEXT_COLOR)

    # Pareto frontier line
    ax.axhline(y=0.95, color='gray', linestyle=':', alpha=0.5)
    ax.axvline(x=0.95, color='gray', linestyle=':', alpha=0.5)
    ax.fill_between([0.95, 1.0], 0.95, 1.0, alpha=0.1, color='green')
    ax.text(0.965, 0.955, "Pareto\nOptimal\nZone", fontsize=9, color='green', alpha=0.7)

    style_axis(ax, "Equity vs Prosperity (Year 2125)\nSource: ALGORAPOLIS by Macha (2026)",
               xlabel="Prosperity Score", ylabel="Equity Score")
    ax.legend(loc='lower left', fontsize=9)
    add_callout_box(ax, "§2836: Pareto optimization over\ndiverse value functions")

    fig.tight_layout()
    return save_chart(fig, "15_equity_prosperity_scatter")


# ============================================================
# CHART 16: Freedom vs Security Scatter
# ============================================================

def chart_freedom_security_scatter(sim_results):
    """Chart 16: Final freedom vs security — the classic tradeoff."""
    fig, ax = plt.subplots(figsize=(10, 10))

    for gov in GOVERNANCE_SYSTEMS:
        freedom = sim_results[gov]["final_metrics"]["freedom"]
        security = sim_results[gov]["final_metrics"]["security"]
        ms = 200 if gov == "Algorapolis" else 100
        marker = '*' if gov == "Algorapolis" else 'o'
        zorder = 10 if gov == "Algorapolis" else 5
        ax.scatter(security, freedom, s=ms, color=GOV_COLORS[gov], marker=marker,
                   label=gov.replace('_', ' '), zorder=zorder, edgecolors='black', linewidth=0.5)
        ax.annotate(gov.replace('_', ' '), (security, freedom),
                    textcoords="offset points", xytext=(8, 5), fontsize=9, color=TEXT_COLOR)

    # Typical tradeoff zone
    ax.plot([0.5, 1.0], [1.0, 0.5], 'k--', alpha=0.3, label='Typical Tradeoff Line')
    ax.fill_between([0.85, 1.0], 0.85, 1.0, alpha=0.1, color='green')
    ax.text(0.87, 0.92, "No Tradeoff\nZone", fontsize=9, color='green', alpha=0.7)

    style_axis(ax, "Freedom vs Security — Breaking the Tradeoff (2125)\nSource: ALGORAPOLIS by Macha (2026)",
               xlabel="Security Score", ylabel="Freedom Score")
    ax.legend(loc='lower left', fontsize=9)
    add_callout_box(ax, "Grey Scale: Pareto optimization\neliminates freedom-security tradeoff")

    fig.tight_layout()
    return save_chart(fig, "16_freedom_security_scatter")


# ============================================================
# CHART 17: Sustainability vs Prosperity
# ============================================================

def chart_sustainability_prosperity(sim_results):
    """Chart 17: Sustainability vs prosperity — another classic tradeoff."""
    fig, ax = plt.subplots(figsize=(10, 10))

    for gov in GOVERNANCE_SYSTEMS:
        sust = sim_results[gov]["final_metrics"]["sustainability"]
        prop = sim_results[gov]["final_metrics"]["prosperity"]
        ms = 200 if gov == "Algorapolis" else 100
        marker = '*' if gov == "Algorapolis" else 'o'
        zorder = 10 if gov == "Algorapolis" else 5
        ax.scatter(prop, sust, s=ms, color=GOV_COLORS[gov], marker=marker,
                   label=gov.replace('_', ' '), zorder=zorder, edgecolors='black', linewidth=0.5)
        ax.annotate(gov.replace('_', ' '), (prop, sust),
                    textcoords="offset points", xytext=(8, 5), fontsize=9, color=TEXT_COLOR)

    ax.fill_between([0.85, 1.0], 0.85, 1.0, alpha=0.1, color='green')
    ax.text(0.87, 0.93, "Sustainable\nProsperity\nZone", fontsize=9, color='green', alpha=0.7)

    style_axis(ax, "Sustainability vs Prosperity (2125)\nSource: ALGORAPOLIS by Macha (2026)",
               xlabel="Prosperity Score", ylabel="Sustainability Score")
    ax.legend(loc='lower left', fontsize=9)
    add_callout_box(ax, "§388-390: Grey Scale eliminates\nthe growth-sustainability tradeoff")

    fig.tight_layout()
    return save_chart(fig, "17_sustainability_prosperity")


# ============================================================
# CHART 18: Composite Civilization Index
# ============================================================

def chart_composite_index(sim_results):
    """Chart 18: Composite civilization index over time (average of all 15 metrics)."""
    fig, ax = plt.subplots(figsize=FIG_WIDE)

    for gov in GOVERNANCE_SYSTEMS:
        composite = []
        for year in YEARS:
            ystr = str(year)
            if ystr in sim_results[gov]["annual_metrics"]:
                vals = list(sim_results[gov]["annual_metrics"][ystr].values())
                composite.append(sum(vals) / len(vals))
            else:
                composite.append(None)
        lw = ALGORAPOLIS_LW if gov == "Algorapolis" else OTHER_LW
        ls = '-' if gov == "Algorapolis" else '--'
        ax.plot(YEARS, composite, label=gov.replace('_', ' '),
                color=GOV_COLORS[gov], linewidth=lw, linestyle=ls)

    style_axis(ax, "Composite Civilization Index (Average of 15 Metrics)\nSource: ALGORAPOLIS by Macha (2026)",
               ylabel="Civilization Index", xlabel="Year")
    ax.legend(loc='best', fontsize=8, ncol=2)
    add_callout_box(ax, "Algorapolis consistently achieves\nhighest composite score")

    fig.tight_layout()
    return save_chart(fig, "18_composite_index")


# ============================================================
# CHART 19: Top 3 vs Bottom 3 Gap Analysis
# ============================================================

def chart_gap_analysis(sim_results):
    """Chart 19: Gap between top 3 and bottom 3 governance systems over time."""
    fig, ax = plt.subplots(figsize=FIG_WIDE)

    # Rank by composite final score
    gov_scores = []
    for gov in GOVERNANCE_SYSTEMS:
        final = sim_results[gov]["final_metrics"]
        avg = sum(final.values()) / len(final)
        gov_scores.append((gov, avg))
    gov_scores.sort(key=lambda x: x[1], reverse=True)

    top3 = [g[0] for g in gov_scores[:3]]
    bottom3 = [g[0] for g in gov_scores[-3:]]

    for gov in top3 + bottom3:
        composite = []
        for year in YEARS:
            ystr = str(year)
            if ystr in sim_results[gov]["annual_metrics"]:
                vals = list(sim_results[gov]["annual_metrics"][ystr].values())
                composite.append(sum(vals) / len(vals))
            else:
                composite.append(None)
        lw = ALGORAPOLIS_LW if gov == "Algorapolis" else OTHER_LW
        ls = '-' if gov in top3 else ':'
        ax.plot(YEARS, composite, label=gov.replace('_', ' '),
                color=GOV_COLORS[gov], linewidth=lw, linestyle=ls)

    # Shade gap
    top_composite = []
    bottom_composite = []
    for year in YEARS:
        ystr = str(year)
        t_vals = [sum(sim_results[g]["annual_metrics"][ystr].values()) / 15
                   for g in top3 if ystr in sim_results[g]["annual_metrics"]]
        b_vals = [sum(sim_results[g]["annual_metrics"][ystr].values()) / 15
                   for g in bottom3 if ystr in sim_results[g]["annual_metrics"]]
        top_composite.append(sum(t_vals) / len(t_vals) if t_vals else None)
        bottom_composite.append(sum(b_vals) / len(b_vals) if b_vals else None)

    ax.fill_between(YEARS, top_composite, bottom_composite, alpha=0.1, color='red', label='Performance Gap')

    style_axis(ax, "Top 3 vs Bottom 3 Governance Systems — Performance Gap\nSource: ALGORAPOLIS by Macha (2026)",
               ylabel="Civilization Index", xlabel="Year")
    ax.legend(loc='best', fontsize=8, ncol=2)

    fig.tight_layout()
    return save_chart(fig, "19_gap_analysis")


# ============================================================
# CHART 20: Resource & Infrastructure Dual Trajectory
# ============================================================

def chart_resource_infrastructure(sim_results):
    """Chart 20: Resources and infrastructure trajectories for all systems."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 7))

    for gov in GOVERNANCE_SYSTEMS:
        resources = get_annual_series(sim_results, gov, "resources")
        infra = get_annual_series(sim_results, gov, "infrastructure")
        lw = ALGORAPOLIS_LW if gov == "Algorapolis" else OTHER_LW

        ax1.plot(YEARS, resources, label=gov.replace('_', ' '), color=GOV_COLORS[gov], linewidth=lw)
        ax2.plot(YEARS, infra, label=gov.replace('_', ' '), color=GOV_COLORS[gov], linewidth=lw)

    style_axis(ax1, "Resource Management", ylabel="Score", xlabel="Year")
    style_axis(ax2, "Infrastructure Development", ylabel="Score", xlabel="Year")
    ax1.legend(loc='best', fontsize=8, ncol=2)
    ax2.legend(loc='best', fontsize=8, ncol=2)

    fig.suptitle("Resource & Infrastructure Trajectories\nSource: ALGORAPOLIS by Macha (2026)",
                 fontsize=14, fontweight='bold', color=TEXT_COLOR, y=1.02)
    add_callout_box(ax1, "Algorithmic resource allocation\nprevents depletion")
    add_callout_box(ax2, "§158: MVA Foundational Layers\nenable rapid infrastructure")

    fig.tight_layout()
    return save_chart(fig, "20_resource_infrastructure")


# ============================================================
# CHART 21: Ecological & Agricultural Resilience
# ============================================================

def chart_eco_agri(sim_results):
    """Chart 21: Wildlife & Ecology + Agriculture trajectories."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 7))

    for gov in GOVERNANCE_SYSTEMS:
        eco = get_annual_series(sim_results, gov, "wildlife_and_ecology")
        agri = get_annual_series(sim_results, gov, "agriculture")
        lw = ALGORAPOLIS_LW if gov == "Algorapolis" else OTHER_LW

        ax1.plot(YEARS, eco, label=gov.replace('_', ' '), color=GOV_COLORS[gov], linewidth=lw)
        ax2.plot(YEARS, agri, label=gov.replace('_', ' '), color=GOV_COLORS[gov], linewidth=lw)

    style_axis(ax1, "Wildlife & Ecology", ylabel="Score", xlabel="Year")
    style_axis(ax2, "Agriculture", ylabel="Score", xlabel="Year")
    ax1.legend(loc='best', fontsize=8, ncol=2)
    ax2.legend(loc='best', fontsize=8, ncol=2)

    fig.suptitle("Ecological & Agricultural Resilience\nSource: ALGORAPOLIS by Macha (2026)",
                 fontsize=14, fontweight='bold', color=TEXT_COLOR, y=1.02)
    add_callout_box(ax1, "Ecocracy-compatible\nsustainability layer")
    add_callout_box(ax2, "Tech-driven precision\nagriculture")

    fig.tight_layout()
    return save_chart(fig, "21_eco_agri")


# ============================================================
# CHART 22: Monetary System & Anti-Corruption
# ============================================================

def chart_monetary(sim_results):
    """Chart 22: Monetary system trajectories highlighting anti-corruption revenue."""
    fig, ax = plt.subplots(figsize=FIG_WIDE)

    for gov in GOVERNANCE_SYSTEMS:
        monetary = get_annual_series(sim_results, gov, "monetary_system")
        lw = ALGORAPOLIS_LW if gov == "Algorapolis" else OTHER_LW
        ax.plot(YEARS, monetary, label=gov.replace('_', ' '),
                color=GOV_COLORS[gov], linewidth=lw)

    style_axis(ax, "Monetary System Performance\nSource: ALGORAPOLIS by Macha (2026)",
               ylabel="Score", xlabel="Year")
    ax.legend(loc='best', fontsize=8, ncol=2)
    add_callout_box(ax, "§1648-1650: Anti-corruption generates\nTZS 4.9 trillion in revenue")

    fig.tight_layout()
    return save_chart(fig, "22_monetary_system")


# ============================================================
# CHART 23: Social Equity Deep Dive
# ============================================================

def chart_social_equity(sim_results):
    """Chart 23: Social classes and equity trajectories."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 7))

    for gov in GOVERNANCE_SYSTEMS:
        social = get_annual_series(sim_results, gov, "social_classes")
        equity = get_annual_series(sim_results, gov, "equity")
        lw = ALGORAPOLIS_LW if gov == "Algorapolis" else OTHER_LW

        ax1.plot(YEARS, social, label=gov.replace('_', ' '), color=GOV_COLORS[gov], linewidth=lw)
        ax2.plot(YEARS, equity, label=gov.replace('_', ' '), color=GOV_COLORS[gov], linewidth=lw)

    style_axis(ax1, "Social Classes", ylabel="Score", xlabel="Year")
    style_axis(ax2, "Equity", ylabel="Score", xlabel="Year")
    ax1.legend(loc='best', fontsize=8, ncol=2)
    ax2.legend(loc='best', fontsize=8, ncol=2)

    fig.suptitle("Social Equity Deep Dive\nSource: ALGORAPOLIS by Macha (2026)",
                 fontsize=14, fontweight='bold', color=TEXT_COLOR, y=1.02)
    add_callout_box(ax2, "§2836: Pareto optimization\nover diverse value functions")

    fig.tight_layout()
    return save_chart(fig, "23_social_equity")


# ============================================================
# CHART 24: Resilience & Security
# ============================================================

def chart_resilience_security(sim_results):
    """Chart 24: Resilience and security trajectories."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 7))

    for gov in GOVERNANCE_SYSTEMS:
        resilience = get_annual_series(sim_results, gov, "resilience")
        security = get_annual_series(sim_results, gov, "security")
        lw = ALGORAPOLIS_LW if gov == "Algorapolis" else OTHER_LW

        ax1.plot(YEARS, resilience, label=gov.replace('_', ' '), color=GOV_COLORS[gov], linewidth=lw)
        ax2.plot(YEARS, security, label=gov.replace('_', ' '), color=GOV_COLORS[gov], linewidth=lw)

    style_axis(ax1, "Resilience", ylabel="Score", xlabel="Year")
    style_axis(ax2, "Security", ylabel="Score", xlabel="Year")
    ax1.legend(loc='best', fontsize=8, ncol=2)
    ax2.legend(loc='best', fontsize=8, ncol=2)

    fig.suptitle("Resilience & Security — Civilizational Immune System\nSource: ALGORAPOLIS by Macha (2026)",
                 fontsize=14, fontweight='bold', color=TEXT_COLOR, y=1.02)
    add_callout_box(ax1, "§1217: Rapid algorithmic\ncoordination")
    add_callout_box(ax2, "Civilizational Immune System\nprevents capture & degradation")

    fig.tight_layout()
    return save_chart(fig, "24_resilience_security")


# ============================================================
# CHART 25: Demography & Population Dynamics
# ============================================================

def chart_demography(sim_results):
    """Chart 25: Demography and population growth."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 7))

    for gov in GOVERNANCE_SYSTEMS:
        demo = get_annual_series(sim_results, gov, "demography")
        pop = []
        for year in YEARS:
            ystr = str(year)
            if ystr in sim_results[gov]["annual_population"]:
                pop.append(sim_results[gov]["annual_population"][ystr])
            else:
                pop.append(None)
        lw = ALGORAPOLIS_LW if gov == "Algorapolis" else OTHER_LW

        ax1.plot(YEARS, demo, label=gov.replace('_', ' '), color=GOV_COLORS[gov], linewidth=lw)
        ax2.plot(YEARS, pop, label=gov.replace('_', ' '), color=GOV_COLORS[gov], linewidth=lw)

    style_axis(ax1, "Demography Score", ylabel="Score", xlabel="Year")
    style_axis(ax2, "Total Population (10 Villages)", ylabel="Population", xlabel="Year")
    ax1.legend(loc='best', fontsize=8, ncol=2)
    ax2.legend(loc='best', fontsize=8, ncol=2)

    fig.suptitle("Demography & Population Dynamics\nSource: ALGORAPOLIS by Macha (2026)",
                 fontsize=14, fontweight='bold', color=TEXT_COLOR, y=1.02)

    fig.tight_layout()
    return save_chart(fig, "25_demography_population")


# ============================================================
# CHART 26: Final Rankings Table (Visual)
# ============================================================

def chart_final_rankings(sim_results):
    """Chart 26: Visual table of final rankings across all metrics."""
    # Compute ranks
    metric_ranks = {}
    for metric in METRICS:
        scores = [(gov, sim_results[gov]["final_metrics"][metric]) for gov in GOVERNANCE_SYSTEMS]
        scores.sort(key=lambda x: x[1], reverse=True)
        metric_ranks[metric] = {gov: rank + 1 for rank, (gov, _) in enumerate(scores)}

    fig, ax = plt.subplots(figsize=(18, 8))
    ax.axis('off')

    # Build data matrix
    cell_text = []
    cell_colors = []
    for gov in GOVERNANCE_SYSTEMS:
        row_text = []
        row_colors = []
        for metric in METRICS:
            rank = metric_ranks[metric][gov]
            score = sim_results[gov]["final_metrics"][metric]
            row_text.append(f"#{rank}\n{score:.3f}")
            if rank == 1:
                row_colors.append('#d4edda')  # Green for #1
            elif rank <= 3:
                row_colors.append('#fff3cd')  # Yellow for top 3
            else:
                row_colors.append('#f8f9fa')  # Light gray
        cell_text.append(row_text)
        cell_colors.append(row_colors)

    col_labels = [METRIC_LABELS[m] for m in METRICS]
    row_labels = [g.replace('_', ' ') for g in GOVERNANCE_SYSTEMS]

    table = ax.table(cellText=cell_text, cellColours=cell_colors,
                     colLabels=col_labels, rowLabels=row_labels,
                     loc='center', cellLoc='center')

    table.auto_set_font_size(False)
    table.set_fontsize(7)
    table.scale(1.0, 1.8)

    # Highlight Algorapolis row
    algo_idx = GOVERNANCE_SYSTEMS.index("Algorapolis")
    for j in range(len(METRICS)):
        cell = table[algo_idx + 1, j]  # +1 for header
        cell.set_text_props(fontweight='bold', color=ALGORAPOLIS_COLOR)
        cell.set_edgecolor(ALGORAPOLIS_COLOR)
        cell.set_linewidth(2)

    ax.set_title("Final Rankings (Year 2125) — Green = #1, Yellow = Top 3\nSource: ALGORAPOLIS by Macha (2026)",
                 loc='left', pad=20, fontsize=14, fontweight='bold', color=TEXT_COLOR)

    fig.tight_layout()
    return save_chart(fig, "26_final_rankings")


# ============================================================
# CHART 27: Media & Information Freedom
# ============================================================

def chart_media_freedom(sim_results):
    """Chart 27: Media & information and freedom trajectories."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 7))

    for gov in GOVERNANCE_SYSTEMS:
        media = get_annual_series(sim_results, gov, "media_and_information")
        freedom = get_annual_series(sim_results, gov, "freedom")
        lw = ALGORAPOLIS_LW if gov == "Algorapolis" else OTHER_LW

        ax1.plot(YEARS, media, label=gov.replace('_', ' '), color=GOV_COLORS[gov], linewidth=lw)
        ax2.plot(YEARS, freedom, label=gov.replace('_', ' '), color=GOV_COLORS[gov], linewidth=lw)

    style_axis(ax1, "Media & Information", ylabel="Score", xlabel="Year")
    style_axis(ax2, "Freedom", ylabel="Score", xlabel="Year")
    ax1.legend(loc='best', fontsize=8, ncol=2)
    ax2.legend(loc='best', fontsize=8, ncol=2)

    fig.suptitle("Media & Information + Freedom\nSource: ALGORAPOLIS by Macha (2026)",
                 fontsize=14, fontweight='bold', color=TEXT_COLOR, y=1.02)
    add_callout_box(ax1, "NDT: National Digital Twin\nprovides transparency")
    add_callout_box(ax2, "Freedom FROM corruption\nand institutional capture")

    fig.tight_layout()
    return save_chart(fig, "27_media_freedom")


# ============================================================
# CHART 28: 100-Year Summary Dashboard
# ============================================================

def chart_summary_dashboard(sim_results, mc_stats):
    """Chart 28: Comprehensive summary dashboard."""
    fig = plt.figure(figsize=(20, 14))
    gs = GridSpec(3, 3, figure=fig, hspace=0.35, wspace=0.3)

    fig.suptitle("ALGORAPOLIS CIVILIZATION SIMULATION — 100-YEAR SUMMARY DASHBOARD\n"
                 "Source: ALGORAPOLIS by Goodluck Japhet Macha (2026)",
                 fontsize=16, fontweight='bold', color=TEXT_COLOR, y=0.98)

    # Panel 1: Composite Index
    ax1 = fig.add_subplot(gs[0, 0])
    for gov in ["Algorapolis", "Democracy", "Capitalism", "Technocracy", "Ecocracy"]:
        composite = []
        for year in YEARS:
            ystr = str(year)
            if ystr in sim_results[gov]["annual_metrics"]:
                vals = list(sim_results[gov]["annual_metrics"][ystr].values())
                composite.append(sum(vals) / len(vals))
        lw = ALGORAPOLIS_LW if gov == "Algorapolis" else OTHER_LW
        ax1.plot(YEARS, composite, label=gov, color=GOV_COLORS[gov], linewidth=lw)
    style_axis(ax1, "Composite Index (Top 5)", ylabel="Score")
    ax1.legend(fontsize=7, loc='best')

    # Panel 2: Final Rankings Bar
    ax2 = fig.add_subplot(gs[0, 1])
    gov_avgs = []
    for gov in GOVERNANCE_SYSTEMS:
        final = sim_results[gov]["final_metrics"]
        gov_avgs.append((gov, sum(final.values()) / len(final)))
    gov_avgs.sort(key=lambda x: x[1], reverse=True)
    names = [g[0][:10] for g in gov_avgs]
    vals = [g[1] for g in gov_avgs]
    colors = [ALGORAPOLIS_COLOR if n == "Algorapol" else PRIMARY_COLOR for n in names]
    ax2.barh(names, vals, color=colors, edgecolor=SECONDARY_COLOR)
    style_axis(ax2, "Overall Ranking (Avg Score)")

    # Panel 3: Algorapolis Radar
    ax3 = fig.add_subplot(gs[0, 2], polar=True)
    N = len(METRICS)
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
    angles += angles[:1]
    algo_vals = [sim_results["Algorapolis"]["final_metrics"][m] for m in METRICS]
    algo_vals += algo_vals[:1]
    ax3.plot(angles, algo_vals, color=ALGORAPOLIS_COLOR, linewidth=2)
    ax3.fill(angles, algo_vals, alpha=0.2, color=ALGORAPOLIS_COLOR)
    ax3.set_xticks(angles[:-1])
    ax3.set_xticklabels([METRIC_LABELS[m][:8] for m in METRICS], fontsize=7)
    ax3.set_title("Algorapolis Radar", fontsize=11, fontweight='bold', color=TEXT_COLOR, pad=15)

    # Panel 4: Shock Impact
    ax4 = fig.add_subplot(gs[1, 0])
    gov_shock_impact = {}
    for gov in GOVERNANCE_SYSTEMS:
        composite = []
        for year in YEARS:
            ystr = str(year)
            if ystr in sim_results[gov]["annual_metrics"]:
                vals = list(sim_results[gov]["annual_metrics"][ystr].values())
                composite.append(sum(vals) / len(vals))
        # Measure volatility
        gov_shock_impact[gov] = np.std(composite)
    sorted_impact = sorted(gov_shock_impact.items(), key=lambda x: x[1], reverse=True)
    ax4.barh([g[0][:10] for g in sorted_impact], [g[1] for g in sorted_impact],
             color=PRIMARY_COLOR, edgecolor=SECONDARY_COLOR)
    style_axis(ax4, "Volatility (Lower = Stable)")

    # Panel 5: Freedom vs Security
    ax5 = fig.add_subplot(gs[1, 1])
    for gov in GOVERNANCE_SYSTEMS:
        freedom = sim_results[gov]["final_metrics"]["freedom"]
        security = sim_results[gov]["final_metrics"]["security"]
        ms = 120 if gov == "Algorapolis" else 60
        ax5.scatter(security, freedom, s=ms, color=GOV_COLORS[gov],
                    edgecolors='black', linewidth=0.5)
    style_axis(ax5, "Freedom vs Security", xlabel="Security", ylabel="Freedom")

    # Panel 6: Equity vs Prosperity
    ax6 = fig.add_subplot(gs[1, 2])
    for gov in GOVERNANCE_SYSTEMS:
        equity = sim_results[gov]["final_metrics"]["equity"]
        prosperity = sim_results[gov]["final_metrics"]["prosperity"]
        ms = 120 if gov == "Algorapolis" else 60
        ax6.scatter(prosperity, equity, s=ms, color=GOV_COLORS[gov],
                    edgecolors='black', linewidth=0.5)
    style_axis(ax6, "Equity vs Prosperity", xlabel="Prosperity", ylabel="Equity")

    # Panel 7-9: Key trajectories
    for panel_idx, (metric, pos) in enumerate([
        ("prosperity", gs[2, 0]),
        ("resilience", gs[2, 1]),
        ("sustainability", gs[2, 2]),
    ]):
        ax = fig.add_subplot(pos)
        for gov in GOVERNANCE_SYSTEMS:
            values = get_annual_series(sim_results, gov, metric)
            lw = ALGORAPOLIS_LW if gov == "Algorapolis" else OTHER_LW
            ax.plot(YEARS, values, color=GOV_COLORS[gov], linewidth=lw, alpha=0.7)
        style_axis(ax, f"{METRIC_LABELS[metric]} Trajectory", ylabel="Score")

    return save_chart(fig, "28_summary_dashboard", dpi=200)


# ============================================================
# MAIN EXECUTION
# ============================================================

def main():
    from collections import defaultdict

    print("=" * 70)
    print("ALGORAPOLIS VISUALIZATION ENGINE V4")
    print("Source: ALGORAPOLIS by Goodluck Japhet Macha (2026)")
    print("=" * 70)

    os.makedirs(CHARTS_DIR, exist_ok=True)

    # Load data
    print("\nLoading simulation data...")
    sim_results, mc_stats, pairwise, phase_analysis, shock_log = load_data()

    # Generate all 28 charts
    print("\nGenerating 28 charts...")

    chart_funcs = [
        ("01", "Metric Trajectories (4x4 Grid)", lambda: chart_metric_trajectories(sim_results)),
        ("02", "Radar Chart — All Systems", lambda: chart_radar_final(sim_results)),
        ("03", "Radar — Algorapolis vs Best", lambda: chart_radar_algorapolis_vs_best(sim_results)),
        ("04", "Dimensional Leadership", lambda: chart_dimensional_leadership(sim_results)),
        ("05", "Monte Carlo Confidence Intervals", lambda: chart_monte_carlo_ci(mc_stats)),
        ("06", "MC Variance Heatmap", lambda: chart_mc_variance_heatmap(mc_stats)),
        ("07", "Pairwise Comparison Matrix", lambda: chart_pairwise_matrix(pairwise)),
        ("08", "Phase Analysis — Algorapolis", lambda: chart_phase_analysis(phase_analysis)),
        ("09", "Phase Comparison — All Systems", lambda: chart_phase_all_systems(phase_analysis)),
        ("10", "Shock Impact Analysis", lambda: chart_shock_impact(shock_log)),
        ("11", "Shock Recovery Trajectories", lambda: chart_shock_recovery(sim_results)),
        ("12", "Mechanism Contributions", lambda: chart_mechanism_contributions()),
        ("13", "Stability Index", lambda: chart_stability_index(sim_results)),
        ("14", "Tech & Prosperity Trajectories", lambda: chart_tech_trajectories(sim_results)),
        ("15", "Equity vs Prosperity Scatter", lambda: chart_equity_prosperity_scatter(sim_results)),
        ("16", "Freedom vs Security Scatter", lambda: chart_freedom_security_scatter(sim_results)),
        ("17", "Sustainability vs Prosperity", lambda: chart_sustainability_prosperity(sim_results)),
        ("18", "Composite Civilization Index", lambda: chart_composite_index(sim_results)),
        ("19", "Gap Analysis (Top 3 vs Bottom 3)", lambda: chart_gap_analysis(sim_results)),
        ("20", "Resource & Infrastructure", lambda: chart_resource_infrastructure(sim_results)),
        ("21", "Ecological & Agricultural", lambda: chart_eco_agri(sim_results)),
        ("22", "Monetary System & Anti-Corruption", lambda: chart_monetary(sim_results)),
        ("23", "Social Equity Deep Dive", lambda: chart_social_equity(sim_results)),
        ("24", "Resilience & Security", lambda: chart_resilience_security(sim_results)),
        ("25", "Demography & Population", lambda: chart_demography(sim_results)),
        ("26", "Final Rankings Table", lambda: chart_final_rankings(sim_results)),
        ("27", "Media & Freedom", lambda: chart_media_freedom(sim_results)),
        ("28", "Summary Dashboard", lambda: chart_summary_dashboard(sim_results, mc_stats)),
    ]

    generated = []
    for num, name, func in chart_funcs:
        print(f"\n  Chart {num}: {name}...", end=" ", flush=True)
        try:
            path = func()
            generated.append(path)
            print("OK")
        except Exception as e:
            print(f"ERROR: {e}")
            import traceback
            traceback.print_exc()

    print(f"\n\n{'='*70}")
    print(f"VISUALIZATION COMPLETE — {len(generated)}/28 charts generated")
    print(f"Output: {CHARTS_DIR}/")
    print(f"{'='*70}")


if __name__ == "__main__":
    main()
