linestyle = {"UiB" : {"MVEM": "-", "TPFA": "-", "MPFA": "-", "RT0": ":"},
             "USTUTT" : {"MPFA": "-", "TPFA\_Circ": "-", "reference": "-", "TPFA_Circ": "-"},
             "UNICE\_UNIGE" : {"HFV\_Cont": "-", "HFV\_Disc": ":", "VAG\_Cont": "-", "VAG\_Disc": ":"},
             "UNICE_UNIGE" : {"HFV_Cont": "-", "HFV_Disc": ":", "VAG_Cont": "-", "VAG_Disc": ":"},
             "NCU\_TW" : {"Hybrid\_FEM": "--"},
             "NCU_TW" : {"Hybrid_FEM": "--"},
             "LANL" : {"MFD\_Tet": "--", "MFD\_Hex": "--", "MFD\_Ex": "--", "MFD_Tet": "--", "MFD_Hex": "--", "MFD_Ex": "--", "MFD": "--"},
             "ETHZ\_USI" : {"FEM\_LM": "--"},
             "ETHZ_USI" : {"FEM_LM": "--"},
             "UNIL\_USI" : {"FE\_AMR\_AFC": "--"},
             "UNIL_USI" : {"FE_AMR_AFC": "--"},
             "UNICAMP" : {"Hybrid\_Hdiv": "--", "Hybrid_Hdiv": "--"},
             "INM" : {"EDFM": "--"},
             "DTU" : {"FEM\_COMSOL": "--", "FEM_COMSOL": "--"},
            }

color = {"UiB" : {"MVEM": "C0", "TPFA": "C1", "MPFA": "C2", "RT0": "C3"},
         "USTUTT" : {"MPFA": "C4", "TPFA\_Circ": "C5", "reference": "black", "TPFA_Circ": "C5"},
         "UNICE\_UNIGE" : {"HFV\_Cont": "C6", "HFV\_Disc": "C7", "VAG\_Cont": "C8", "VAG\_Disc": "C9"},
         "UNICE_UNIGE" : {"HFV_Cont": "C6", "HFV_Disc": "C7", "VAG_Cont": "C8", "VAG_Disc": "C9"},
         "NCU\_TW" : {"Hybrid\_FEM": "C0"},
         "NCU_TW" : {"Hybrid_FEM": "C0"},
         "LANL" : {"MFD\_Tet": "C1", "MFD\_Hex": "C2", "MFD\_Ex": "C1", "MFD_Tet": "C1", "MFD_Hex": "C2", "MFD_Ex": "C1", "MFD": "C2"},
         "ETHZ\_USI" : {"FEM\_LM": "C3"},
         "ETHZ_USI" : {"FEM_LM": "C3"},
         "UNIL\_USI" : {"FE\_AMR\_AFC": "C4"},
         "UNIL_USI" : {"FE_AMR_AFC": "C4"},
         "UNICAMP" : {"Hybrid\_Hdiv": "C5", "Hybrid_Hdiv": "C5"},
         "INM" : {"EDFM": "C6"},
         "DTU" : {"FEM\_COMSOL": "C7", "FEM_COMSOL": "C7"}
        }

# Returns the label used for time
def getTimeLabel(unit='s'):
    label = "$t \, [\mathrm{"
    label += unit
    label += "}]$"
    return label

# Returns the label used for arc lengths
def getArcLengthLabel():
    return "$\mathrm{arc} \, \mathrm{length} \, [m]$"

# Returns the label used for piezometric head
def getHeadLabel(dimension):
    label = "$h_"
    label += str(dimension)
    label += " \, [\mathrm{m}]$"
    return label

# Returns the label used for concentrations
def getConcentrationLabel(dimension):
    label = "$c_"
    label += str(dimension)
    label += " \, [\mathrm{m}^{-3}]$"
    return label

# Returns the label used for avered concentrations
def getAveragedConcentrationLabel(dimension):
    label = "$\overline{c_"
    label += str(dimension)
    label += "} \, [\mathrm{m}^{-3}]$"
    return label
