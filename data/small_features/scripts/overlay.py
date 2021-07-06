import os

files = ["case3_pol_p_line_0", "case3_pot_fracture_3"]

for f in files:
    os.system("pdflatex " + f)
    f_pdf = f + ".pdf"
    os.system("pdfcrop " + f_pdf)
    os.system("mv " + f + "-crop.pdf plots/" + f_pdf )


