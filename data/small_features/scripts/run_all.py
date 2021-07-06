import os

os.system("python pol.py")
os.system("python boundarydata.py")
os.system("python pot.py")

# this goes after the others
os.system("python overlay.py")
