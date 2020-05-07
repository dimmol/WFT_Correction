import pandas as pd
import numpy as np
from scipy import interpolate

if __name__ == '__main__':

#    The script assumes that the trajectory is in CSV file
#    with depth in metres and single header line.
#    There should be the following columns in the header:
#    MD, TVD, Inc
    df = pd.read_csv(r'.\DATA\G8XST3.csv', header = 0, index_col = False, skip_blank_lines=True)#, skiprows = [1]
    
    md_pts = df.MD
    tvd_pts = df.TVD
    
    inc_pts = df.Inc
    
    x_vals = [2010.31, 2021.86, 2037.5, 2057.04, 2077.87, 2082.53, 2088.01, 2094.91]

    inc_splines = interpolate.splrep(md_pts, inc_pts)

    inc_vals = np.round(interpolate.splev(x_vals, inc_splines),2)
    
    t = np.round(np.cos(np.pi*inc_vals/180),2)
    
#    Quartz gauge offsets:
#    If the gauge is deeper than the probe, its readings are high than the pressure.
#    RDT Dual probe is 2.36m shallower than the gauge.
#    RDT Oval probe is 5.60m shallower than the gauge.
#    Assuming HAL is handling surface eqt correctly, FPRE data channel should be
#    taking gauge offset into account.
#    MDT QG is 1.06m (42'' - need to confirm 52'' from another source) shallower than the probe (MRPS)
#    RFT HP gauge is a separate module and is normally 1.85m deeper than the probe
    
    gauge_offset = 1.85
    
#---------------------------------
    tvd_splines = interpolate.splrep(md_pts, tvd_pts)

    tvd_vals = np.round(interpolate.splev(x_vals, tvd_splines), 2)
    
    
    df = pd.DataFrame()
    df['MD'] = x_vals
    df['TVD'] = tvd_vals
    df['Incl'] = inc_vals
    df['Cosine'] = t
    df['Probe Correction'] = np.round(gauge_offset * t * 1.44, 2)
    
    print(df)