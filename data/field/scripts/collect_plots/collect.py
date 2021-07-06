import os

def main():

    path = "../plots/"
    outfile = "document.pdf"
    figures = ""

    for root, _, files in os.walk(path):
        for f in sorted(files):
            figures += root + "/" + f + " "

    figures += " " + outfile
    os.system("pdfunite " + figures)

if __name__ == "__main__":
    main()
