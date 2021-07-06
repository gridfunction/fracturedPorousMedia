import plotroutines as plot
from matplotlib import rc

# ------------------------------------------------------------------------------#
# add data to plots

# add plots for the different schemes
# The first argument is the path to your data, where the data is assumed to be ordered comma-separated in the following order:
#   -> 1. arc length, 2. value of either c or pressure
# The second argument defines the legend you want to add to your data (Institution / Numerical method)

titles = ["$\\sim 30k$ cells", "$\\sim 150k$ cells"]
refinement_index = ["0", "1"]

places_and_methods = {
    "UiB": ["TPFA", "MPFA", "MVEM", "RT0"],
    "USTUTT": ["MPFA", "TPFA\_Circ"],
    "LANL": ["MFD"],
    #"NCU\_TW": ["Hybrid\_FEM"],
    "UNICE\_UNIGE": ["VAG\_Cont", "HFV\_Cont", "VAG\_Disc", "HFV\_Disc"],
    "ETHZ\_USI": ["FEM\_LM"],
    "UNICAMP": ["Hybrid\_Hdiv"],
    "UNIL\_USI": ["FE\_AMR\_AFC"],
    "INM": ["EDFM"],
    "DTU": ["FEM\_COMSOL"]
};

fig_p_0 = plot.plt.figure(plot.id_p_0_matrix+11, figsize=(16, 6))
fig_p_0.subplots_adjust(hspace=0, wspace=0)
fig_p_1 = plot.plt.figure(plot.id_p_1_matrix+11, figsize=(16, 6))
fig_p_1.subplots_adjust(hspace=0, wspace=0)

for title, ref in zip(titles, refinement_index):

    ax_p_0 = fig_p_0.add_subplot(1, 2, int(ref) + 1, ylim=(0.03-0.005, 0.07+0.01))
    ax_p_1 = fig_p_1.add_subplot(1, 2, int(ref) + 1, ylim=(0.02-0.001, 0.07+0.005))

    for place in places_and_methods:
        for method in places_and_methods[place]:
            folder = "../results/" + place + "/" + method + "/"
            label = place + "\_" + method
            data = folder.replace("\\", "") + "dol_line_0_refinement_" + ref + ".csv"
            plot.plot_over_line(data, label, ref,
                                plot.id_p_0_matrix, title, ax_p_0,
                                plot.linestyle[place][method], plot.color[place][method],
                                has_legend=False, fmt="%1.2f")

            data = folder.replace("\\", "") + "dol_line_1_refinement_" + ref + ".csv"
            plot.plot_over_line(data, label, ref,
                                plot.id_p_1_matrix, title, ax_p_1,
                                plot.linestyle[place][method], plot.color[place][method],
                                has_legend=False, fmt="%1.2f")

    # Reference
    folder = "../results/USTUTT/MPFA/"
    ref_label = "USTUTT\_MPFA\_refined"
    data = folder + "dol_line_0_refinement_5.csv"
    plot.plot_over_line(data, ref_label, ref,
                        plot.id_p_0_matrix, title, ax_p_0,
                        plot.linestyle["USTUTT"]["reference"], plot.color["USTUTT"]["reference"],
                        has_legend=False, fmt="%1.2f")
    data = folder + "dol_line_1_refinement_5.csv"
    plot.plot_over_line(data, ref_label, ref,
                        plot.id_p_1_matrix, title, ax_p_1,
                        plot.linestyle["USTUTT"]["reference"], plot.color["USTUTT"]["reference"],
                        has_legend=False, fmt="%1.2f")

# save figures
plot.save(plot.id_p_0_matrix, "case3_pol_p_line_0")
plot.save(plot.id_p_1_matrix, "case3_pol_p_line_1")

ncol = 4
for place in places_and_methods:
    for method in places_and_methods[place]:
        label = "\\texttt{" + place + "-" + method + "}"
        plot.plot_legend(label, plot.id_p_0_matrix_legend, plot.linestyle[place][method],
                         plot.color[place][method], ncol)

        plot.plot_legend(label, plot.id_p_1_matrix_legend, plot.linestyle[place][method],
                             plot.color[place][method], ncol)

# add reference to legend
plot.plot_legend("reference", plot.id_p_0_matrix_legend, plot.linestyle["USTUTT"]["reference"],
                 plot.color["USTUTT"]["reference"], ncol)

plot.plot_legend("reference", plot.id_p_1_matrix_legend, plot.linestyle["USTUTT"]["reference"],
                 plot.color["USTUTT"]["reference"], ncol)

plot.save(plot.id_p_0_matrix_legend, "case3_pol_p_0_matrix_legend")
plot.crop_pdf("case3_pol_p_0_matrix_legend")
plot.save(plot.id_p_1_matrix_legend, "case3_pol_p_1_matrix_legend")
plot.crop_pdf("case3_pol_p_1_matrix_legend")

# ------------------------------------------------------------------------------#
