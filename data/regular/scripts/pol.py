import plotroutines as plot

#------------------------------------------------------------------------------#
# Insert here your data for the plotting, see the file 'color_regions.vtu'
# for the coloring code of each region.

titles = ['$\\sim 500$ cells', '$\\sim 4k$ cells', '$\\sim 32k$ cells']
refinement_index = [0, 1, 2]
conds = [0, 1]

places_and_methods = {
    "UiB": ["TPFA", "MPFA", "MVEM", "RT0"],
    "USTUTT": ["MPFA", "TPFA\_Circ"],
    "LANL": ["MFD"],
#    "NCU\_TW": ["Hybrid\_FEM"],
    "UNICE\_UNIGE": ["VAG\_Cont", "HFV\_Cont", "VAG\_Disc", "HFV\_Disc"],
    "ETHZ\_USI": ["FEM\_LM"],
    "UNICAMP": ["Hybrid\_Hdiv"],
    "UNIL\_USI": ["FE\_AMR\_AFC"],
#    "INM": ["EDFM"],
    "DTU": ["FEM\_COMSOL"]
};

for cond in conds:

    fig = plot.plt.figure(cond+11, figsize=(16, 6))
    fig.subplots_adjust(hspace=0, wspace=0)
    if cond == 0:
        ylim = (0.5, 2.75)
        fmt = "%1.2f"
    else:
        ylim = (0.4, 5.75)
        fmt = "%1.2e"

    for title, ref in zip(titles, refinement_index):

        ax = fig.add_subplot(1, 3, ref + 1, ylim=ylim)

        for place in places_and_methods:
            for method in places_and_methods[place]:
                folder = "../results/" + place + "/" + method + "/"
                data = folder.replace("\\", "") + "dol_cond_" + str(cond) + "_refinement_" + str(ref) + ".csv"
                label = place + "\_" + method

                plot.plot_over_line(data, label, ref, title, cond, ax,
                                    plot.linestyle[place][method], plot.color[place][method],
                                    has_legend=False, fmt=fmt)

        # add reference (4th refinement of USTUTT-MPFA)
        place = "USTUTT"
        method = "reference"
        label = "reference"
        data = "../results/USTUTT/MPFA/dol_cond_" + str(cond) + "_refinement_4.csv"
        plot.plot_over_line(data, label, ref, title, cond, ax,
                            plot.linestyle[place][method], plot.color[place][method],
                            has_legend=False, fmt=fmt)

    # save figures
    plot.save(cond, "case2_pol_cond_"+str(cond), starting_from=3*cond)

ncol = 4
for cond in conds:
    for place in places_and_methods:
        for method in places_and_methods[place]:
            label = "\\texttt{" + place + "-" + method + "}"
            plot.plot_legend(label, cond, plot.linestyle[place][method],
                             plot.color[place][method], ncol)

    # add reference to legend
    plot.plot_legend("reference", cond, plot.linestyle["USTUTT"]["reference"],
                     plot.color["USTUTT"]["reference"], ncol)

    plot.save(cond, "case2_pol_cond_"+str(cond)+"_legend")
    plot.crop_pdf("case2_pol_cond_"+str(cond)+"_legend")

#------------------------------------------------------------------------------#
