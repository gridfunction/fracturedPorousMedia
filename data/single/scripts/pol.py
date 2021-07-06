import plotroutines as plot

#------------------------------------------------------------------------------#

# add data to plots

# add plots for the different schemes
# The first argument is the path to your data, where the data is assumed to be ordered comma-separated in the following order:
#   -> 1. arc length, 2. value of either c or pressure
# The second argument defines the legend you want to add to your data (Institution / Numerical method)

titles = ['$\\sim 1k$ cells', '$\\sim 10k$ cells', '$\\sim 100k$ cells']
refinement_index = ['0', '1', '2']

places_and_methods = {
    "UiB": ["TPFA", "MPFA", "MVEM", "RT0"],
    "USTUTT": ["MPFA", "TPFA\_Circ"],
    "LANL": ["MFD"],
    "NCU\_TW": ["Hybrid\_FEM"],
    "UNICE\_UNIGE": ["VAG\_Cont", "HFV\_Cont", "VAG\_Disc", "HFV\_Disc"],
    "ETHZ\_USI": ["FEM\_LM"],
    "UNICAMP": ["Hybrid\_Hdiv"],
    "UNIL\_USI": ["FE\_AMR\_AFC"],
    "INM": ["EDFM"],
    "DTU": ["FEM\_COMSOL"]
};

fig_p_matrix = plot.plt.figure(plot.id_p_matrix+11, figsize=(16, 6))
fig_p_matrix.subplots_adjust(hspace=0, wspace=0)
fig_c_matrix = plot.plt.figure(plot.id_c_matrix+11, figsize=(16, 6))
fig_c_matrix.subplots_adjust(hspace=0, wspace=0)
fig_c_fracture = plot.plt.figure(plot.id_c_fracture+11, figsize=(16, 6))
fig_c_fracture.subplots_adjust(hspace=0, wspace=0)

for title, ref in zip(titles, refinement_index):

    axes_p_matrix = fig_p_matrix.add_subplot(1, 3, int(ref) + 1, ylim=(1-0.1, 4+0.1))
    axes_c_matrix = fig_c_matrix.add_subplot(1, 3, int(ref) + 1, ylim=(0-0.0005, 0.01+0.0005))
    axes_c_fracture = fig_c_fracture.add_subplot(1, 3, int(ref) + 1, ylim=(0.0075, 0.0101))

    for place in places_and_methods:
        for method in places_and_methods[place]:
            folder = "../results/" + place + "/" + method + "/"
            data = folder.replace("\\", "") + "dol_refinement_" + ref + ".csv"
            label = place + "-" + method

            plot.plot_over_line(data, label, ref, plot.id_p_matrix, title, axes_p_matrix,
                                plot.linestyle[place][method], plot.color[place][method],
                                has_legend=False, ylim=(1-0.1, 4+0.1))

            # DTU could only provide results for pressure
            if place != "DTU":
                plot.plot_over_line(data, label, ref, plot.id_c_matrix, title, axes_c_matrix,
                                    plot.linestyle[place][method], plot.color[place][method],
                                    has_legend=False, ylim=(0-0.0005, 0.01+0.0005))
                plot.plot_over_line(data, label, ref, plot.id_c_fracture, title, axes_c_fracture,
                                    plot.linestyle[place][method], plot.color[place][method],
                                    has_legend=False, ylim=(0.0075, 0.0101))

    # add reference (5th refinement USTUTT-MPFA)
    place = "USTUTT"
    method = "reference"
    label = "reference"
    data = "../results/USTUTT/MPFA/dol_refinement_5.csv"
    plot.plot_over_line(data, label, ref, plot.id_p_matrix, title, axes_p_matrix,
                        plot.linestyle[place][method], plot.color[place][method],
                        has_legend=False, ylim=(1-0.1, 4+0.1))

# save figures
plot.save(plot.id_p_matrix, "case1_pol_p_matrix")
plot.save(plot.id_c_matrix, "case1_pol_c_matrix")
plot.save(plot.id_c_fracture, "case1_pol_c_fracture")

ncol = 4
for place in places_and_methods:
    for method in places_and_methods[place]:
        label = "\\texttt{" + place + "-" + method + "}"
        plot.plot_legend(label, plot.id_p_matrix_legend, plot.linestyle[place][method],
                         plot.color[place][method], ncol)

        # DTU could only provide results for pressure
        if place != "DTU":
            plot.plot_legend(label, plot.id_c_matrix_legend, plot.linestyle[place][method],
                             plot.color[place][method], ncol)
            plot.plot_legend(label, plot.id_c_fracture_legend, plot.linestyle[place][method],
                             plot.color[place][method], ncol)

# add reference to the pressure legend
plot.plot_legend("reference", plot.id_p_matrix_legend, plot.linestyle["USTUTT"]["reference"],
                 plot.color["USTUTT"]["reference"], ncol)

plot.save(plot.id_p_matrix_legend, "case1_pol_p_matrix_legend")
plot.crop_pdf("case1_pol_p_matrix_legend")
plot.save(plot.id_c_matrix_legend, "case1_pol_c_matrix_legend")
plot.crop_pdf("case1_pol_c_matrix_legend")
plot.save(plot.id_c_fracture_legend, "case1_pol_c_fracture_legend")
plot.crop_pdf("case1_pol_c_fracture_legend")

#------------------------------------------------------------------------------#
