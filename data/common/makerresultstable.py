import numpy as np
import sys
import os

places_and_methods = {
    "UiB": ["MVEM", "TPFA", "MPFA", "RT0"],
    "USTUTT": ["MPFA", "TPFA_Circ"],
    "UNICE_UNIGE": ["HFV_Cont", "HFV_Disc", "VAG_Cont", "VAG_Disc"],
    "NCU_TW": ["Hybrid_FEM"],
    "LANL": ["MFD"],
    "ETHZ_USI": ["FEM_LM"],
    "UNIL_USI": ["FE_AMR_AFC"],
    "UNICAMP": ["Hybrid_Hdiv"],
    "INM": ["EDFM"],
    "DTU": ["FEM_COMSOL"]
};

if len(sys.argv) < 2:
    sys.stderr.write("Please provide the sub-folder of the case you want to consider and the file name of the results files (optional, defaults to \"results.csv\")\n")
    sys.exit(1)

# extract names and data for all methods that submitted results.
# The method names will not be exactly as in the document and will
# have to be replaced by the respective macros manually. Also, if your
# case considers more data than listed in places_and_methods, you should
# add it manually or extend places_and_methods for your case.
methodNames = []
methodData = []

caseSubFolder = sys.argv[1]
caseSubFolder = caseSubFolder.strip("/")
resultsFileName = "results.csv"
if (len(sys.argv) > 2):
    resultsFileName = sys.argv[2]

for place in places_and_methods:
    placeSubFolder = caseSubFolder + "/results/" + place

    # continue only if place submitted results
    if os.path.exists(placeSubFolder):
        for method in places_and_methods[place]:
            methodSubFolder = placeSubFolder + "/" + method

            # continue only if results were submitted for method
            if os.path.exists(methodSubFolder) and os.path.isfile(methodSubFolder + "/" + resultsFileName):
                print("Loading data for scheme " + methodSubFolder)
                curData = np.loadtxt(methodSubFolder + "/" + resultsFileName, delimiter=',', ndmin=2)

                methodData.append([])
                methodNames.append(place + "-" + method)

                for refinementData in curData:
                    if len(refinementData) < 6:
                        methodData[len(methodData)-1].append(refinementData)
                    else:
                        methodData[len(methodData)-1].append(refinementData[0:6])


# check if any scheme reported multiple refinements
hasRefinements = False
for curData in methodData:
    if len(curData) > 1:
        hasRefinements = True

# make sure lists have the same size
if len(methodData) != len(methodNames):
    sys.stderr.write("Error! Name and data arrays do not have the same size!\n")
    sys.exit(1)


# write data into latex table
latexFile = open(caseSubFolder + '_resultstable.tex', 'w')
latexFile.write('\\begin{table}\n')
latexFile.write('\\begin{center}\n')
latexFile.write('\\begin{tabular}{|l|l|l|l|l|l|l|l|}\\hline\n')

# write column specifications
if hasRefinements == True:
    latexFile.write('Method & Refinement & 0d cells & 1d cells & 2d cells & 3d cells & dofs & nnz \\\\ ')
else:
    latexFile.write('Method & 0d cells & 1d cells & 2d cells & 3d cells & dofs & nnz \\\\ ')

latexFile.write('\\hline\n')

for methodIdx in range(0, len(methodNames)):
    name = methodNames[methodIdx]
    data = methodData[methodIdx]

    # start a new line
    if hasRefinements == True:
        latexFile.write("\t\\multirow{" + str(len(data)) + "}{*}{" + name + "}\n")
    else:
        latexFile.write("\t" + name)

    # write the data
    for dataIdx in range(0, len(data)):

        # put indentation if multirow
        if hasRefinements == True:
            latexFile.write("\t\t\t & " + str(dataIdx))

        # write values
        for valueIdx in range(0, len(data[dataIdx])):
            latexFile.write(" & " + str( int(data[dataIdx][valueIdx]) ))

        # add "not available" if not all data was reported
        if len(data[dataIdx] < 6):
            for i in range(len(data[dataIdx]), 6):
                latexFile.write(" & n.\\ a.\\ ")

        # finish the line in the table
        latexFile.write("\\\\")
        if hasRefinements == True and dataIdx == len(data) - 1:
            latexFile.write(" \\hline ")

        # finish a table without several refinements with an hline
        if hasRefinements == False and methodIdx == len(methodNames) - 1:
            latexFile.write(" \\hline ")

        latexFile.write("\n")

latexFile.write('\\end{tabular}\n')
latexFile.write('\\end{center}\n')
latexFile.write('\\end{table}\n')
