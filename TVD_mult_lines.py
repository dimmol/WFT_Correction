# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 15:32:41 2020

@author: dmolokho
"""
from scipy import interpolate
import pandas as pd
import numpy as np
if __name__ == '__main__':
    
    df = pd.read_csv(r'C:\Users\dmolokho\Documents\Py\TVD_Calc\DATA\IDT_4ST1.csv', header = 0, index_col = False) #skip_blank_lines=True, skiprows = [2], 
    
#    fig = plt.figure()
#    ax = Axes3D(fig)
#    surf = ax.plot(df.NORTHING, df.EASTING, df.TVD, linewidth=1, antialiased=False)
#    ax.invert_zaxis()
#    plt.show()
    
#    print(df.head())
#    print(df.columns)

    
#    f = open(r'C:\Users\dmolokho\Documents\Py\TVD_Calc\DATA\test_utf.csv', 'r')
#    
#    for line in f:
#        print(line)
    
#    print(os.getcwd())
    
#    x_vals = np.linspace(df.MD.min(), df.MD.max(), 100)
    print(df.columns)
    
    print(df.head())
    
    md_pts = df.MD
    tvd_pts = df.TVD
    
    tvdss_pts = df.TVDSS
    
#    print(md_pts)
    df_out = pd.DataFrame(columns=['MD', 'TVD', 'TVDSS'])
    
    x_vals = [2135.21, 2174.1]
    
    for i in x_vals:
        tvd_splines = interpolate.splrep(md_pts, tvd_pts)
        tvd_vals = interpolate.splev(i, tvd_splines)
        
        tvdss_splines = interpolate.splrep(md_pts, tvdss_pts)
        tvdss_vals = interpolate.splev(i, tvdss_splines)
        print(type(tvdss_vals))
        df_out = df_out.append(pd.Series([i, np.round(tvd_vals, 2), np.round(tvdss_vals, 2)], index = ['MD', 'TVD', 'TVDSS']), ignore_index=True)
    
#    print('md: ', x_vals)
#    print('tvd: ', tvd_vals)
#    print('tvdss: ', tvdss_vals)
        
    print(df_out.head())
#    t = np.cos(np.pi*inc_vals/180)
    
#    print('angle: ', inc_vals)
#    print('cosine: ', t)
#    print('Dual probe correction ', 2.36 * t * 1.44)
#    print('Oval probe correction ', 5.60 * t * 1.44)

#    print(y_vals)
#    print(y_vals1)
    
#    plt.plot(df.MD, df.TVD, 'o')
#    plt.plot(x_vals, y_vals, '-x')
#    plt.show()