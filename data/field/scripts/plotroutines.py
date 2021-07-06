from __future__ import print_function

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

from scipy import interpolate
from scipy.integrate import simps
from operator import methodcaller

import numpy as np
import os
import sys
sys.path.insert(0, '../../common')
import styles

#------------------------------------------------------------------------------#

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.rc('font', size=15)

# ids of the different plots
id_p_0_matrix = 0   # pressure along (0, 100, 100)-(100, 0, 0)
id_p_0_matrix_legend = 10   # pressure along (0, 100, 100)-(100, 0, 0)
id_p_1_matrix = 1   # p along (0, 100, 100)-(100, 0, 0)
id_p_1_matrix_legend = 11   # p along (0, 100, 100)-(100, 0, 0)
id_pot = 2
id_pot_legend = 12   # p along (0, 100, 100)-(100, 0, 0)

linestyle = styles.linestyle
color = styles.color

def plot_over_line(file_name, legend, ID, title, ax, lineStyle="-", clr='C0', **kwargs):

    c = lambda s: float(s.decode().replace('D', 'e'))
    N = 2
    data = np.genfromtxt(file_name, delimiter=",", converters=dict(zip(range(N), [c]*N)))

    ax.yaxis.set_major_formatter(MathTextSciFormatter(kwargs.get("fmt", "%1.2e")))

    ax.plot(data[:, 0], data[:, 1], label=legend, linestyle=lineStyle, color=clr)
    ax.grid(True)

    ax.set_xlabel( styles.getArcLengthLabel() )
    ax.grid(True)
    ax.set_ylabel( styles.getHeadLabel(3) )
    if kwargs.get("has_title", True):
        ax.set_title(title)
    if kwargs.get("has_legend", True):
        ax.legend(bbox_to_anchor=(1.0, 1.0))
    if kwargs.get("xlim", None):
        plt.xlim(kwargs.get("xlim"))
    if kwargs.get("ylim", None):
        plt.ylim(kwargs.get("ylim"))

    if ID == id_p_0_matrix:
        ax.set_xticks([0, 500, 1000, 1500])
        ax.set_yticks([0, 100, 200, 300, 400, 500, 600, 700])
    elif ID == id_p_1_matrix:
        ax.set_xticks([0, 500, 1000, 1500])
        ax.set_yticks([0, 50, 100, 150, 200, 250])


def save(simulation_id, filename, extension=".pdf", ax_title=None):
    folder = "./plots/"

    if not os.path.exists(folder):
        os.makedirs(folder)

    fig = plt.figure(simulation_id+11)

    for idx, ax in enumerate(fig.get_axes()):
        ax.label_outer()
        if len(fig.get_axes()) > 1:
            text = "\\textbf{subfig. " + chr(97+idx) + "}"
            ax.text(0.5, -0.2, text, horizontalalignment='center',
                    verticalalignment='bottom', transform=ax.transAxes)
        elif ax_title is not None:
            ax.text(0.5, -0.25, ax_title, horizontalalignment='center',
                    verticalalignment='bottom', transform=ax.transAxes)

    plt.savefig(folder+filename+extension, bbox_inches='tight')
    plt.gcf().clear()

def crop_pdf(filename):
    folder = "./plots/"
    filename = folder + filename + ".pdf"
    if os.path.isfile(filename):
        os.system("pdfcrop --margins '0 -300 0 0' " + filename + " " + filename)
        os.system("pdfcrop " + filename + " " + filename)


def plot_over_time(file_name, legend, title, ID, region, region_pos, num_regions, ax, lineStyle='-', clr='C0', **kwargs):

    c = lambda s: float(s.decode().replace('D', 'e'))
    N = 53
    data = np.genfromtxt(file_name, delimiter=",", converters=dict(zip(range(N), [c]*N)))
    ax.yaxis.set_major_formatter(MathTextSciFormatter(kwargs.get("fmt", "%1.2e")))
    plt.rcParams.update({'figure.max_open_warning': 0})

    if region_pos > 0:
        ax.yaxis.set_tick_params(length=0)

    ax.plot(data[:, 0], data[:, region+1], label=legend, linestyle=lineStyle, color=clr)

    ax.set_xlabel( styles.getTimeLabel('s') )
    ax.set_ylabel(styles.getAveragedConcentrationLabel(2))
    ax.grid(True)
    if kwargs.get("has_title", True):
        ax.set_title(title)
    if kwargs.get("has_legend", True):
        ax.legend(bbox_to_anchor=(1.0, 1.0))
    if kwargs.get("xlim", None):
        plt.xlim(kwargs.get("xlim"))
    if kwargs.get("ylim", None):
        plt.ylim(kwargs.get("ylim"))

    ax.set_xticks([0, 500, 1000, 1500])


def save_over_time(filename, extension=".pdf"):
    folder = "./plots/"

    if not os.path.exists(folder):
        os.makedirs(folder)

    for ID in np.arange(52):
        plt.figure(ID)
        plt.savefig(folder+filename+"_fracture_"+str(ID)+extension, bbox_inches='tight')
        plt.gcf().clear()

def plot_legend(legend, ID, lineStyle="-", clr="C0", ncol=1):
    # it looks like that figure_ID = 1 gives problems, so we add a random number = 11
    plt.figure(ID+11)
    plt.plot(np.zeros(1), label=legend, linestyle=lineStyle, color=clr)
    plt.legend(bbox_to_anchor=(1, -0.2), ncol=ncol)

class MathTextSciFormatter(mticker.Formatter):
    def __init__(self, fmt="%1.2e"):
        self.fmt = fmt
    def __call__(self, x, pos=None):
        s = self.fmt % x
        if "f" in self.fmt:
            return "${}$".format(s)
        decimal_point = '.'
        positive_sign = '+'
        tup = s.split('e')
        significand = tup[0].rstrip(decimal_point)
        sign = tup[1][0].replace(positive_sign, '')
        exponent = tup[1][1:].lstrip('0')
        if exponent:
            exponent = '10^{%s%s}' % (sign, exponent)
        if significand and exponent:
            s =  r'%s{\times}%s' % (significand, exponent)
        else:
            s =  r'%s%s' % (significand, exponent)
        return "${}$".format(s)

def plot_percentiles(ref, places_and_methods, ax, **kwargs):

    c = lambda s: float(s.decode().replace('D', 'e'))
    N = 2

    ax.yaxis.set_major_formatter(MathTextSciFormatter("%1.2e"))

    f = []
    minX = -np.inf
    maxX = np.inf

    for place in places_and_methods:
        for method in places_and_methods[place]:
            folder = "../results/" + place + "/" + method + "/"
            datafile = folder.replace("\\", "") + "dol_line_" + ref + ".csv"
            data = np.genfromtxt(datafile, delimiter=",", converters=dict(zip(range(N), [c]*N)))
            # only take the interesting columns and eleminate nan rows
            data = data[:, 0:2];
            data = data[~np.isnan(data).any(axis=1)]

            f.append(interpolate.interp1d(data[:, 0], data[:, 1]))
            minX = max(minX, data[0, 0])
            maxX = min(maxX, data[-1, 0])

    ls = np.linspace(minX, maxX, num=1000)
    interpolateddata = list(map(methodcaller('__call__', ls), f))
    meanvalues = np.mean(interpolateddata, axis=0)
    variance = np.var(interpolateddata, axis=0)
    lowerpercentile = np.percentile(interpolateddata, 10, axis=0)
    upperpercentile = np.percentile(interpolateddata, 90, axis=0)

    ax.fill_between(ls, lowerpercentile, upperpercentile, color="gray")
    ax.grid(True)
    ax.set_xlabel( styles.getArcLengthLabel() )
    weightedarea = (simps(upperpercentile, ls) -
                    simps(lowerpercentile, ls))/simps(meanvalues, ls)
    title = "weighted area " + MathTextSciFormatter("%1.2e")(weightedarea)
    ax.title.set_text(title)
    if kwargs.get("ylim", None):
        ax.set_ylim(kwargs.get("ylim"))
    if kwargs.get("xlim", None):
        ax.set_xlim(kwargs.get("xlim"))

    ax.set_xticks([0, 500, 1000, 1500])
    if ref == "0":
        ax.set_yticks([0, 100, 200, 300, 400, 500, 600, 700])
    elif ref == "1":
        ax.set_yticks([0, 50, 100, 150, 200, 250])

    # choose y-label depending on plot id
    ax.set_ylabel( styles.getHeadLabel(3) )

    return (ls, lowerpercentile, upperpercentile)
