import pandas as pd
#import os

#from mpl_toolkits.mplot3d import axes3d, Axes3D
#import matplotlib.pyplot as plt
import numpy as np
#from matplotlib import cm
from scipy import interpolate
import pandas as pd
#from matplotlib.mlab import bivariate_normal


if __name__ == '__main__':
    
    df = pd.read_csv(r'C:\Users\dmolokho\Documents\Py\TVD_Calc\DATA\well_survey.csv', header = 20, skip_blank_lines=True, skiprows = [21, 22, 23])
    
#    fig = plt.figure()
#    ax = Axes3D(fig)
#    surf = ax.plot(df.NORTHING, df.EASTING, df.TVD, linewidth=1, antialiased=False)
#    ax.invert_zaxis()
#    plt.show()
#    print(df.index)
#    print(df.head())
#    print(df.columns)

    
#    f = open(r'C:\Users\dmolokho\Documents\Py\TVD_Calc\DATA\test_utf.csv', 'r')
#    
#    for line in f:
#        print(line)
    
#    print(os.getcwd())
    
#    x_vals = np.linspace(df.MD.min(), df.MD.max(), 100)
    print(df.columns)
    
    md_pts = df.MD
    tvd_pts = df.TVD
    
    inc_pts = df.Inc
    
    x_vals = [3802.66, 3816.43, 3823.49, 3841.38, 4139.03]
#    y_vals = np.interp(x_vals, df.MD, df.TVD)
    
#    splines = interpolate.splrep(x_pts, y_pts)
    inc_splines = interpolate.splrep(md_pts, inc_pts)
#    y_vals1 = interpolate.splev(x_vals, splines)
    inc_vals = interpolate.splev(x_vals, inc_splines)
    
    t = np.cos(np.pi*inc_vals/180)
    
    print('angle: ', inc_vals)
    print('cosine: ', t)
    print('Dual probe correction ', 2.36 * t * 1.44)
    print('Oval probe correction ', 5.60 * t * 1.44)

#---------------------------------
    tvd_splines = interpolate.splrep(md_pts, tvd_pts)
#    y_vals1 = interpolate.splev(x_vals, splines)
    tvd_vals = np.round(interpolate.splev(x_vals, tvd_splines), 2)
    
#    print('MD: ', x_vals)
#    print('TVD: ', np.round(tvd_vals, 2))
    
    df = pd.DataFrame()
    df['MD'] = x_vals
    df['TVD'] = tvd_vals
    
    print(df)

#    print(y_vals)
#    print(y_vals1)
    
#    plt.plot(df.MD, df.TVD, 'o')
#    plt.plot(x_vals, y_vals, '-x')
#    plt.show()
    

