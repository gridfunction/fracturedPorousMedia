import subprocess
import os

def main():

    path = "../plots/"
    figures = ""

    for _, _, files in os.walk(path):
        for f in sorted(files):
            figures += "\\begin{figure}\n\t\\centering\n"
            figures += "\t\\includegraphics[width=1\\textwidth]{" + path + f + "}\n"
            figures += "\t\\caption{" + f.replace("_", "\_") + "}\n"
            figures += "\\end{figure}\n"

    document = "\\documentclass{article}\n\\usepackage{graphicx}\n\\begin{document}\n"
    document += figures
    document += "\end{document}"

    tex_file_name = "document.tex"
    with open(tex_file_name, "w") as tex_file:
        tex_file.write("{0}".format(document))

    subprocess.run(["pdflatex", tex_file_name])

if __name__ == "__main__":
    main()
