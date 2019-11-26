

import os
# import os.path as op
import matplotlib.pyplot as plt

def mySaveFig(filename):
    try:
        plt.savefig(filename)
    except FileNotFoundError:
        directoryname = os.path.dirname(filename)
        os.mkdir(directoryname)
        plt.savefig(filename)

#
# os.path.exists("some_folder")
# Out[3]: False
# os.path.exists("figures")
# Out[4]: True