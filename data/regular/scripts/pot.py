import numpy as np
import plotroutines as plot

#------------------------------------------------------------------------------#

# Insert here your data for the plotting, see the file 'color_regions.vtu'
# for the coloring code of each region.

titles = ['$\\sim 4k$ cells  - permeability 1e4', '$\\sim 4k$ cells  - permeability 1e-4']
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
#    "DTU": ["FEM\_COMSOL"]
};

regions = np.array([1, 10, 11])
regions_fig = {1: "case2_region10pic.png", 10: "case2_region11pic.png", 11: "case2_region1pic.png"}

#------------------------------------------------------------------------------#

for cond, title in zip(conds, titles):

    fig = plot.plt.figure(cond+11, figsize=(16, 6))
    fig.subplots_adjust(hspace=0, wspace=0)
    if cond == 0:
        ylim = (0, 0.475)
    else:
        ylim = (0, 0.4)

    for region_pos, region in enumerate(regions):
        ax = fig.add_subplot(1, regions.size, region_pos + 1, ylim=ylim)

        for place in places_and_methods:
            for method in places_and_methods[place]:
                folder = "../results/" + place + "/" + method + "/"
                data = folder.replace("\\", "") + "/dot_cond_" + str(cond) + ".csv"
                label = place + "\_" + method

                plot.plot_over_time(data, label, title, cond, region, region_pos, regions.size, ax,
                                    lineStyle=plot.linestyle[place][method],
                                    clr=plot.color[place][method],
                                    has_legend=False, fmt="%1.2f")

    # save figures
    plot.save(cond, "case2_cot_cond_"+str(cond), starting_from=3*cond)

ncol = 4
for cond in conds:
    for place in places_and_methods:
        for method in places_and_methods[place]:
            label = "\\texttt{" + place + "-" + method + "}"
            plot.plot_legend(label, cond, plot.linestyle[place][method],
                             plot.color[place][method], ncol)

    plot.save(cond, "case2_cot_cond_"+str(cond)+"_legend")
    plot.crop_pdf("case2_cot_cond_"+str(cond)+"_legend")

#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
