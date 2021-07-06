import os

files = ["case4_pol_line_1", "case4_pol_line_2",
         "case4_pot"]

for f in files:
    os.system("pdflatex " + f)
    f_pdf = f + ".pdf"
    os.system("pdfcrop " + f_pdf)
    os.system("mv " + f + "-crop.pdf plots/" + f_pdf )


