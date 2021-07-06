import os

files = ["case1_pol_c_fracture", "case1_pol_c_matrix",
         "case1_pol_p_matrix", "case1_pot_outflux"]

for f in files:
    os.system("pdflatex " + f)
    f_pdf = f + ".pdf"
    os.system("pdfcrop " + f_pdf)
    os.system("mv " + f + "-crop.pdf plots/" + f_pdf )


