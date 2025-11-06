import os
import argparse
import glob
import numpy as np
import xarray as xr

import pandas as pd

if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('--inpath', 
                        type=str, 
                        required=True,
                        help='Path to input directory.')
    
    parser.add_argument('--file', 
                        type=str, 
                        required=True,
                        help='Input files* name pattern (e.g., "*.nc").')
    
    parser.add_argument('--outpath', 
                        type=str, 
                        required=True,
                        help='Path to output directory.')
    
    parser.add_argument('--tres', 
                        type=str, 
                        required=True,
                        help='Temporal aggregation period.')
    
    parser.add_argument('--tres_clm', 
                        type=str, 
                        default='1D',
                        help='Temporal resolution of clm history data (default: 1D).')
    
    parser.add_argument('--method', 
                        type=str, 
                        default='mean',
                        help='Aggregation method (default: mean).')
    
    parser.add_argument('--vars', 
                        type=str, 
                        nargs='+',
                        default=None,
                        help='Variables to process (default: all).')
    
    parser.add_argument('--year_start', 
                        type=int,
                        required=True,
                        help='Start year.')
    
    parser.add_argument('--year_end', 
                        type=int, 
                        required=True,
                        help='End year.')
    
    args = parser.parse_args()

    os.makedirs(args.outpath, exist_ok=True)

    files = sorted(glob.glob(os.path.join(args.inpath, args.file)))

    for year in np.arange(args.year_start, args.year_end + 1):

        print(f'Processing year: {year}')

        files_year = [f for f in files if f'{year}' in os.path.basename(f)]

        data = xr.open_mfdataset(files_year, data_vars=None, combine='by_coords')

        data_year = data.sel(time=data.time.dt.year == year)
    
        if args.vars is not None: data_year = data_year[args.vars]

        drop_vars = []

        for var in data_year.variables:

            if data_year[var].dtype not in ['float64', 'float32', 'int64', 'int32']:
                
                drop_vars.append(var)
        
        data_year = data_year.drop_vars(drop_vars)

        time = time_raw = pd.date_range(f'{year}-01-01 00:00:00', 
                                        f'{year}-12-31 23:59:59', 
                                        freq=args.tres_clm).to_series()

        mask = [False if (t.month == 2 and t.day == 29) else True for t in time.index]

        time = time[mask]

        data_year['time'] = ('time', time)

        func_ = getattr(xr.DataArray, args.method)

        resampler = data_year.resample(time=args.tres)

        data_resampled = func_(resampler)

        out_file = os.path.join(args.outpath, f'{year}.nc')

        data_resampled.to_netcdf(out_file, 
                                 format='NETCDF4_CLASSIC', 
                                 unlimited_dims=['time'])
