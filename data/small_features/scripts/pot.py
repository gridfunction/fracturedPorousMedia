import plotroutines as plot
import numpy as np

#------------------------------------------------------------------------------#
# add data to plots

# add plots for the different schemes
# The first argument is the path to your data, where the data is assumed to be ordered comma-separated in the following order:
#   -> 1. time
#      2. integral of \phi c within matrix sub-domain \Omega_3
#      3. integral of \phi c within fracture domain \Omega_f
#      4. outlux of the domain across the outfow boundary
# The second argument defines the legend you want to add to your data (Institution / Numerical method)
# The third argument specifies the plot id - use the ids defined in lines 35-37 for the different plots

# TODO: add reference solution to plots as soon as available

titles = ['$\\sim 30k$ cells', '$\\sim 150k$ cells']
refinement_index = ['0', '1']

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
    #"DTU": ["FEM\_COMSOL"]
};

for ID in np.arange(8):

    fig = plot.plt.figure(ID+11, figsize=(16, 6))
    fig.subplots_adjust(hspace=0, wspace=0)

    for title, ref in zip(titles, refinement_index):

        ax = fig.add_subplot(1, 2, int(ref) + 1, ylim=((0-0.01, 1+0.01)))

        for place in places_and_methods:
            for method in places_and_methods[place]:
                folder = "../results/" + place + "/" + method + "/"
                data = folder.replace("\\", "") + "/dot_refinement_"+ref+".csv"
                label = place + "\_" + method
                plot.plot_over_time(data, label, ref, ID, title, ax,
                                    lineStyle=plot.linestyle[place][method], clr=plot.color[place][method],
                                    has_legend=False)

# save figures
plot.save_over_time("case3_pot")

ncol = 4
for place in places_and_methods:
    for method in places_and_methods[place]:
        label = "\\texttt{" + place + "-" + method + "}"
        plot.plot_legend(label, plot.id_pot_legend, plot.linestyle[place][method],
                         plot.color[place][method], ncol)

plot.save(plot.id_pot_legend, "case3_pot_legend")
plot.crop_pdf("case3_pot_legend")

#------------------------------------------------------------------------------#
