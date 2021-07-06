import os
import sys
sys.path.insert(0, 'data/common')
import data.single.scripts.plotroutines as case1
import data.regular.scripts.plotroutines as case2
import data.small_features.scripts.plotroutines as case3
import data.field.scripts.plotroutines as case4
import matplotlib.pyplot as plt
import numpy as np
import styles

linestyle = styles.linestyle
color = styles.color

def calculate_match(x, y, ls, lowerpercentile, upperpercentile):
    x_eval = np.linspace(min(ls), max(ls), 100)
    y_eval = np.interp(x_eval, x, y)
    lower_eval = np.interp(x_eval, ls, lowerpercentile)
    upper_eval = np.interp(x_eval, ls, upperpercentile)
    inbetween = np.logical_and(np.less_equal(lower_eval, y_eval), np.greater_equal(upper_eval, y_eval))
    return sum(inbetween.astype(int))

def evaluate(x, y, case, plot_id, ref_index=0, subdomain_id=0, name="your method"):
    ax = plt.gca()

    if case == 1:

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
        os.chdir("data/single/scripts")

        if plot_id == "a":
            (ls, lp, up) = case1.plot_percentiles(str(ref_index), case1.id_p_matrix,
                                                  places_and_methods, ax)
            data = "../results/USTUTT/MPFA/dol_refinement_5.csv"
            case1.plot_over_line(data, "reference", ref_index, case1.id_p_matrix, "", ax,
                                 linestyle["USTUTT"]["reference"], color["USTUTT"]["reference"],
                                 has_legend=False, ylim=(1-0.1, 4+0.1))
        elif plot_id == "b":
            (ls, lp, up) = case1.plot_percentiles(str(ref_index), case1.id_c_matrix,
                                                  places_and_methods, ax)
        elif plot_id == "c":
            (ls, lp, up) = case1.plot_percentiles(str(ref_index), case1.id_c_fracture,
                                                  places_and_methods, ax)
        else:
            print("Error. Invalid plot id " + plot_id + " provided.")
            os.chdir("../../..")
            sys.exit(1)

    elif case == 2.1:

        places_and_methods = {
            "UiB": ["TPFA", "MPFA", "MVEM", "RT0"],
            "USTUTT": ["MPFA", "TPFA\_Circ"],
            "LANL": ["MFD"],
            "UNICE\_UNIGE": ["VAG\_Cont", "HFV\_Cont", "VAG\_Disc", "HFV\_Disc"],
            "ETHZ\_USI": ["FEM\_LM"],
            "UNICAMP": ["Hybrid\_Hdiv"],
            "UNIL\_USI": ["FE\_AMR\_AFC"],
            "DTU": ["FEM\_COMSOL"]
        };
        os.chdir("data/regular/scripts")

        if plot_id == "a":
            (ls, lp, up) = case2.plot_percentiles(str(ref_index), "0",
                                                  places_and_methods, ax)
            data = "../results/USTUTT/MPFA/dol_cond_0_refinement_4.csv"
            case2.plot_over_line(data, "reference", ref_index, "", 0, ax,
                                 linestyle["USTUTT"]["reference"], color["USTUTT"]["reference"],
                                 has_legend=False, fmt="%1.2e")

        else:
            print("Error. Invalid plot id " + plot_id + " provided.")
            os.chdir("../../..")
            sys.exit(1)

    elif case == 2.2:

        # only include methods admitting discontinuous pressure
        places_and_methods = {
            "UiB": ["TPFA", "MPFA", "MVEM", "RT0"],
            "USTUTT": ["MPFA", "TPFA\_Circ"],
            "LANL": ["MFD"],
            "UNICE\_UNIGE": ["VAG\_Disc", "HFV\_Disc"],
            "UNICAMP": ["Hybrid\_Hdiv"],
            "UNIL\_USI": ["FE\_AMR\_AFC"],
        };
        os.chdir("data/regular/scripts")

        if plot_id == "a":
            (ls, lp, up) = case2.plot_percentiles(str(ref_index), "1",
                                                  places_and_methods, ax)
            data = "../results/USTUTT/MPFA/dol_cond_1_refinement_4.csv"
            case2.plot_over_line(data, "reference", ref_index, "", 1, ax,
                                 linestyle["USTUTT"]["reference"], color["USTUTT"]["reference"],
                                 has_legend=False, fmt="%1.2e")

        else:
            print("Error. Invalid plot id " + plot_id + " provided.")
            os.chdir("../../..")
            sys.exit(1)

    elif case == 3:

        places_and_methods = {
            "UiB": ["TPFA", "MPFA", "MVEM", "RT0"],
            "USTUTT": ["MPFA", "TPFA\_Circ"],
            "LANL": ["MFD"],
            "UNICE\_UNIGE": ["VAG\_Cont", "HFV\_Cont", "VAG\_Disc", "HFV\_Disc"],
            "ETHZ\_USI": ["FEM\_LM"],
            "UNICAMP": ["Hybrid\_Hdiv"],
            "UNIL\_USI": ["FE\_AMR\_AFC"],
            "INM": ["EDFM"],
            "DTU": ["FEM\_COMSOL"]
        };
        os.chdir("data/small_features/scripts")

        if plot_id == "a":
            (ls, lp, up) = case3.plot_percentiles(str(ref_index), str(subdomain_id),
                                                  places_and_methods, ax)
            data = "../results/USTUTT/MPFA/dol_line_" + str(subdomain_id) + "_refinement_5.csv"
            case3.plot_over_line(data, "reference", ref_index, subdomain_id, "", ax,
                                 linestyle["USTUTT"]["reference"], color["USTUTT"]["reference"],
                                 has_legend=False, fmt="%1.2f")

        else:
            print("Error. Invalid plot id " + plot_id + " provided.")
            os.chdir("../../..")
            sys.exit(1)

    elif case == 4:

        places_and_methods = {
            "UiB": ["TPFA", "MPFA", "MVEM", "RT0"],
            "USTUTT": ["MPFA", "TPFA\_Circ"],
            "LANL": ["MFD"],
            "UNICE\_UNIGE": ["VAG\_Cont", "HFV\_Cont", "VAG\_Disc", "HFV\_Disc"],
            "ETHZ\_USI": ["FEM\_LM"],
            "UNICAMP": ["Hybrid\_Hdiv"],
            "DTU": ["FEM\_COMSOL"]
        };
        os.chdir("data/field/scripts")

        if plot_id == "a":
            if subdomain_id == 2:
                subdomain_id = 0
            (ls, lp, up) = case4.plot_percentiles(str(subdomain_id), places_and_methods, ax)
        else:
            print("Error. Invalid plot id " + plot_id + " provided.")
            os.chdir("../../..")
            sys.exit(1)

    else:

        print("Error. Invalid case id " + str(case) + " provided.")
        sys.exit(1)

    match = calculate_match(x, y, ls, lp, up)

    ax.plot(x, y, 'C1', linewidth=3)
    ax.set_title("match: " + str(match))

    if case < 4:
        ax.legend(["reference", name, "published spread"])#, bbox_to_anchor=(1.05, 1), loc='upper left')
    else:
        ax.legend([name, "published spread"])#, bbox_to_anchor=(1.05, 1), loc='upper left')

    os.chdir("../../..")
