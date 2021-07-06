import os

files = ["case2_pol_cond_0", "case2_pol_cond_1",
         "overlay_fig1", "overlay_fig2"]

for f in files:
    os.system("pdflatex " + f)
    f_pdf = f + ".pdf"
    os.system("pdfcrop " + f_pdf)
    os.system("mv " + f + "-crop.pdf plots/" + f_pdf )


