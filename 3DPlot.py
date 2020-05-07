# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 14:48:30 2020

@author: dmolokho
"""

import pandas as pd
#import os

from mpl_toolkits.mplot3d import axes3d, Axes3D
import matplotlib.pyplot as plt
#from matplotlib import cm
#import numpy as np
#from matplotlib.mlab import bivariate_normal


if __name__ == '__main__':
    
    df = pd.read_csv(r'C:\Users\dmolokho\Documents\Py\TVD_Calc\DATA\well_survey.csv', header = 20, skip_blank_lines=True, skiprows = [21, 22, 23])
    
    fig = plt.figure()
    ax = Axes3D(fig)
    surf = ax.plot(df.NORTHING, df.EASTING, df.TVD, linewidth=1, antialiased=False)
    ax.invert_zaxis()
    plt.show()