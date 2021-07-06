import os

def main():

    path = "../plots/"
    outfile = "document.pdf"
    figures = ""

    for _, _, files in os.walk(path):
        for f in sorted(files):
            figures += path + f + " "

    figures += " " + outfile
    os.system("pdfunite " + figures)

if __name__ == "__main__":
    main()
