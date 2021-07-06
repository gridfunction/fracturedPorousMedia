import os
import re

def natural_sort(l):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(l, key = alphanum_key)


def main():

    path = "../plots/"
    outfile = "document.pdf"
    figures = ""

    for root, _, files in os.walk(path):
        for f in natural_sort(files):
            figures += root + "/" + f + " "

    figures += " " + outfile
    os.system("pdfunite " + figures)

if __name__ == "__main__":
    main()
