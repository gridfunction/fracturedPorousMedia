import numpy as np
import plotroutines as plot

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

for ref in ["0", "1", "2"]:
    axes_p_matrix = fig_p_matrix.add_subplot(1, 3, int(ref) + 1, ylim=(1-0.1, 4+0.1))
    axes_c_matrix = fig_c_matrix.add_subplot(1, 3, int(ref) + 1, ylim=(0-0.0005, 0.01+0.0005))
    axes_c_fracture = fig_c_fracture.add_subplot(1, 3, int(ref) + 1, ylim=(0.0075, 0.0101))
    plot.plot_percentiles(ref, plot.id_p_matrix, places_and_methods, axes_p_matrix)
    plot.plot_percentiles(ref, plot.id_c_matrix, places_and_methods, axes_c_matrix)
    plot.plot_percentiles(ref, plot.id_c_fracture, places_and_methods, axes_c_fracture)

# save figures
plot.save(plot.id_p_matrix, "case1_pol_p_matrix_percentile_90_10", starting_from=3)
plot.save(plot.id_c_matrix, "case1_pol_c_matrix_percentile_90_10", starting_from=3)
plot.save(plot.id_c_fracture, "case1_pol_c_fracture_percentile_90_10", starting_from=3)
