"""
Collect data at boundary for all methods, including the refined USTUTT MPFA.
The data is fluxes at the two outflow boundaries and hydraulic head at the inflow
boundary. The reported data are the total outflux, the proportion of the flux exiting
at the first outflow region and the hydraulic head, all for both refinement levels.
"""
import numpy as np
import csv
import plotroutines as plot

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

all_data = []
methods = []
colors = []
linestyle = []
with open("case3_boundary_data_table.csv", "w", newline="") as outfile:
    writer = csv.writer(outfile, delimiter=",")
    writer.writerow(
        [
            "Method",
            "Outflow 30k",
            "Outflow 150k",
            "Out0/Out 30k",
            "Out0/Out 150k",
            "Inflow 30k",
            "Inflow 150k",
        ]
    )
    for place in places_and_methods:
        for method in places_and_methods[place]:
            folder = "../results/" + place + "/" + method + "/"
            file_name = folder.replace("\\", "") + "/results.csv"
            label = "\\texttt{" + place + "-" + method + "}"
            d = np.genfromtxt(file_name, delimiter=",")
            out = np.sum(d[:2, 6:8], axis=1)
            data = [
                out[0],
                out[1],
                d[0, 6] / out[0],
                d[1, 6] / out[1],
                d[0, 8],
                d[1, 8],
            ]
            row = label + ",{0:.3f},{1:.3f},{2:.3f},{3:.3f},{4:.3f},{5:.3f}".format(
                *data
            )
            writer.writerow(row.split(","))
            all_data.append(data)
            methods.append(method)
            colors.append(plot.color[place][method])
            linestyle.append(plot.linestyle[place][method])
    # reference
    folder = "../results/USTUTT/MPFA/"
    file_name = folder + "/results.csv"
    d = np.genfromtxt(file_name, delimiter=",")
    ind = 5
    out = np.sum(d[ind, 6:8])
    # Collect reference data: sum out, ratio of outfluxes, head
    data_ref = np.array([out, d[ind, 6] / out, d[ind, 8]])

    all_data = np.array(all_data)
    means = np.mean(all_data.copy(), axis=0)
    stdvs = np.std(all_data, axis=0)
    writer.writerow(["Reference", "-", data_ref[0], "-", data_ref[1], "-", data_ref[2]])
    writer.writerow(
        ["Standard deviation", stdvs[0], stdvs[1], "-", "-", stdvs[4], stdvs[5]]
    )
    plot.plot_boundary_data(all_data, methods, data_ref, colors, linestyle)


ncol = 4
id_legend = 0
ind = 0
for place in places_and_methods:
    for method in places_and_methods[place]:
        label = "\\texttt{" + place + "-" + method + "} - \\textbf{" + str(ind) + "}"
        plot.plot_legend(label, id_legend, plot.linestyle[place][method],
                         plot.color[place][method], ncol)
        ind += 1

plot.save(id_legend, "case3_bar_legend")
plot.crop_pdf("case3_bar_legend")

