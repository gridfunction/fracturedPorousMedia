import numpy as np
import plotroutines as plot

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

title = ""
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
    #"DTU": ["FEM\_COMSOL"]
};

regions = [15, 45, 48]

for region_pos, region in enumerate(regions):

    title = "fracture " + str(region)
    fig = plot.plt.figure(plot.id_pot+11, figsize=(16, 6))
    fig.subplots_adjust(hspace=0, wspace=0)

    ax = fig.add_subplot(1, len(regions), region_pos + 1, ylim=(0-0.01, 1+0.01), xlim=(-100, 1800))

    for place in places_and_methods:
        for method in places_and_methods[place]:
            folder = "../results/" + place + "/" + method + "/"
            data = folder.replace("\\", "") + "dot.csv"
            label = place + "\_" + method

            plot.plot_over_time(data, label, title, plot.id_pot, region, region_pos, len(regions), ax,
                                plot.linestyle[place][method], plot.color[place][method],
                                has_legend=False, fmt="%1.2f")

# save figures
plot.save(plot.id_pot, "case4_pot")

ncol = 4
for place in places_and_methods:
    for method in places_and_methods[place]:
        label = "\\texttt{" + place + "-" + method + "}"
        plot.plot_legend(label, plot.id_pot_legend, plot.linestyle[place][method],
                         plot.color[place][method], ncol)

plot.save(plot.id_pot_legend, "case4_pot_legend")
plot.crop_pdf("case4_pot_legend")

#------------------------------------------------------------------------------#
