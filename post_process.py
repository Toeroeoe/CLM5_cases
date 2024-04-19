
import xarray as xr
import numpy as np
from glob import glob
from my_.files.handy import check_file_exists, create_dirs


def join_west_east(dir_west: str,
                   dir_east: str,
                   files_west: str = '*.nc',
                   files_east: str = '*.nc',
                   path_out: str = 'out_join/',
                   sel_vars: None | list = None,):
    
    
    create_dirs(path_out)
    
    files_west = sorted(glob(f'{dir_west}/{files_west}'))

    files_east = sorted(glob(f'{dir_east}/{files_east}'))

    assert len(files_east) == len(files_west)

    for i in range(len(files_east)):

        file_west = files_west[i]
        file_east = files_east[i]

        data_w = xr.open_dataset(f'{file_west}')
        data_e = xr.open_dataset(f'{file_east}')

        if sel_vars is not None:

            data_w = data_w[sel_vars]
            data_e = data_e[sel_vars]
        
        year = np.unique(data_e.time.dt.year.values).item()

        if check_file_exists(f'{path_out}/{year}.nc'): continue

        print(f'\nCreate yearly file for year {year}')
        print(f'by joining {file_west} and {file_east}...\n')
        
        data_joined = xr.concat([data_w, data_e], dim = 'lon')

        data_y = data_joined.sel(time = data_joined.time.dt.year.isin(year))

        data_y.to_netcdf(f'{path_out}/{year}.nc',
                         format = 'NETCDF4_CLASSIC', 
                         unlimited_dims = ['time'])
        

def resample(path_hist: str,
             files_hist: str = '*.nc',
             dst_resolution: str = 'D',
             method: str = 'mean',
             path_out: str = 'out_resample/'):
    
    create_dirs(path_out)

    files = sorted(glob(f'{path_hist}/{files_hist}'))

    for f in files:

        data = xr.open_dataset(f'{f}')

        year = np.unique(data.time.dt.year.values).item()

        print(f'\nCreate resampled file for {year}')
        print(f'by using {method} to resolution: {dst_resolution}...\n')

        if check_file_exists(f'{path_out}/{year}.nc'): return

        xr_func = getattr(xr.Dataset, method)
        
        resampler = data.resample({'time': time_res})

        data_s = xr_func(resampler)

        data_s.to_netcdf(f'{path_out}/{year}.nc',
                         format = 'NETCDF4_CLASSIC', 
                         unlimited_dims = ['time'])


def drop_vars(path_hist: str,
              files_hist: str = '*.nc',
              drop_vars: list = ['ZSOI', 
                                 'DZSOI',
                                 'WATSAT',
                                 'SUCSAT',
                                 'BSW',
                                 'HKSAT',
                                 'ZLAKE',
                                 'DZLAKE'],
              path_out: str = 'out_drop_vars/'):
    

    create_dirs(path_out)

    files = sorted(glob(f'{path_hist}/{files_hist}'))

    for f in files:

        data = xr.open_dataset(f'{f}')

        year = np.unique(data.time.dt.year.values).item()

        print(f'\nDrop variables {drop_vars} for year {year}...\n')

        if check_file_exists(f'{path_out}/{year}.nc'): continue

        data_d = data.drop_vars(drop_vars, errors = 'ignore')

        data_d.to_netcdf(f'{path_out}/{year}.nc',
                         format = 'NETCDF4_CLASSIC', 
                         unlimited_dims = ['time'])
        


if __name__ == '__main__':

    dir_west = '/p/scratch/cjibg31/jibg3105/data/CLM5EU3/007/west/'
    files_west = '*.nc'

    dir_east = '/p/scratch/cjibg31/jibg3105/data/CLM5EU3/007/east/'
    files_east = '*.nc'

    path_out_join = '/p/scratch/cjibg31/jibg3105/data/CLM5EU3/007/join/'
    path_out_resample = '/p/scratch/cjibg31/jibg3105/data/CLM5EU3/007/join/8daily/'
    path_out_drop = '/p/scratch/cjibg31/jibg3105/data/CLM5EU3/007/join/8daily/drop/'
    time_res = '8D'

    sel_vars = ['GPP', 
                'QFLX_EVAP_TOT',
                'QFLX_EVAP_GRND',
                'QFLX_EVAP_VEG',
                'BTRANMN',
                'GSSHA',
                'QOVER',
                'H2OSOI',
                'ZWT']
    
    join_west_east(dir_west,
                   dir_east,
                   files_west,
                   files_east,
                   path_out_join,
                   sel_vars)
    
    resample(path_out_join,
             '*.nc',
             time_res,
             path_out = path_out_resample)
    

    drop_vars(path_out_resample,
              path_out = path_out_drop)