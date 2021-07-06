import numpy as np
import plotroutines as plot

places_and_methods = {
    "UiB": ["TPFA", "MPFA", "MVEM", "RT0"],
    "USTUTT": ["MPFA", "TPFA\_Circ"],
    "LANL": ["MFD"],
    #"NCU\_TW": ["Hybrid\_FEM"],
    "UNICE\_UNIGE": ["VAG\_Cont", "HFV\_Cont", "VAG\_Disc", "HFV\_Disc"],
    "ETHZ\_USI": ["FEM\_LM"],
    "UNICAMP": ["Hybrid\_Hdiv"],
    #"UNIL\_USI": ["FE\_AMR\_AFC"],
    #"INM": ["EDFM"],
    "DTU": ["FEM\_COMSOL"]
};

for ref in ["0", "1"]:
    fig = plot.plt.figure(int(ref)+11)
    fig.subplots_adjust(hspace=0, wspace=0)

    if ref == "0":
        ax = fig.add_subplot(ylim=(-50, 720), xlim=(-100, 1800))
    else:
        ax = fig.add_subplot(ylim=(-20, 280), xlim=(-100, 1800))
    plot.plot_percentiles(ref, places_and_methods, ax)

    # save figures
    if ref == "0":
        ax_title = "\\textbf{subfig. d}"
    else:
        ax_title = "\\textbf{subfig. c}"

    plot.save(int(ref), "case4_pol_p_line_"+ref+"_matrix_percentile_90_10", ax_title=ax_title)
