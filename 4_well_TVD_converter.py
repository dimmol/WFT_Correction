# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 11:34:27 2020

@author: dmolokho
"""

import pandas as pd
import numpy as np
from scipy import interpolate



if __name__ == '__main__':

#    Change file name to required well trajectory file name
#    Options are:
#    IDT4ST1.csv
#    IDT13.csv
#    IDD4.csv
#    IDD5.csv
    df = pd.read_csv(r'C:\Users\dmolokho\Documents\Py\TVD_Calc\TRAJ\Survey.csv', header = 0, index_col = False, skip_blank_lines=True)#, skiprows = [1]
    
    md_pts = df.MD
    tvd_pts = df.TVD
    
#    tvdss_pts = df.Z

#    Update this list with your MD values (in metres)
    x_vals = [1000, 1500, 2000, 2500, 2900, 3100, 3200, 3407]
    

#---------------------------------
    tvd_splines = interpolate.splrep(md_pts, tvd_pts)

    tvd_vals = np.round(interpolate.splev(x_vals, tvd_splines), 2)
    
#    tvdss_splines = interpolate.splrep(md_pts, tvdss_pts)

#    tvdss_vals = np.round(interpolate.splev(x_vals, tvdss_splines), 2)

    
    df_out = pd.DataFrame()
    df_out['MD'] = x_vals
    df_out['TVD'] = tvd_vals
#    df_out['TVDSS'] = tvdss_vals
    
    print(df_out)
    

