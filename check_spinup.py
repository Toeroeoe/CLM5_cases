


def check_steady_state(name_case: str, 
                       subperiod: int, 
                       path_hist: str,
                       year_start: None | int = None, 
                       year_end: None | int = None,
                       glob_thresh: dict = { 
                            'TOTECOSYSC': 0.02,
                            'TOTSOMC': 0.02, 
                            'TOTVEGC': 0.02, 
                            'TLAI': 0.02, 
                            'GPP': 0.02, 
                            'TWS': 0.001 },
                       agg_method: dict = { 
                            'TOTECOSYSC': 'sum',
                            'TOTSOMC': 'sum', 
                            'TOTVEGC': 'sum', 
                            'TLAI': 'sum', 
                            'GPP': 'sum', 
                            'TWS': 'mean' },
                       landarea_agg_method: dict = {
                            'TOTECOSYSC': 'multiply',
                            'TOTSOMC': 'multiply', 
                            'TOTVEGC': 'multiply', 
                            'TLAI': 'divide', 
                            'GPP': 'multiply', 
                            'TWS': '' },
                       var_factor: dict = {
                            'TOTECOSYSC': 1,
                            'TOTSOMC': 1, 
                            'TOTVEGC': 1, 
                            'TLAI': 1, 
                            'GPP': 60 * 60 * 24 * 365.25, 
                            'TWS': 1 },
                       units: dict = {
                            'TOTECOSYSC': r'$\mathdefault{g\;C}$', 
                            'TOTSOMC': r'$\mathdefault{g\;C}$', 
                            'TOTVEGC': r'$\mathdefault{g\;C}$',
                            'TLAI': r'$\mathdefault{m^{2}\;m^{2}}$', 
                            'GPP': r'$\mathdefault{g\;C\;year^{-1}}$', 
                            'TWS': r'$\mathdefault{m}$' },
                       relative_area_thresh: float = 3.0, 
                       cell_thresh: float = 1.0,
                       magnitudes: dict = {
                            'TOTECOSYSC': 14, 
                            'TOTSOMC': 14, 
                            'TOTVEGC': 14, 
                            'TLAI': 0, 
                            'GPP': 0, 
                            'TWS': 0 },
                       path_grid: str = '', 
                       file_grid: str = '', 
                       var_lat: str = '', 
                       var_lon: str = '',
                       variables: list = [
                            'TOTECOSYSC', 
                            'TOTSOMC', 
                            'TOTVEGC', 
                            'TLAI', 
                            'GPP', 
                            'TWS']):
    
    from glob import glob
    import numpy as np
    from netCDF4 import Dataset, MFDataset
    import matplotlib.pyplot as plt
    import matplotlib as mpl
    from matplotlib.backends.backend_pdf import PdfPages
    from cartopy import crs
    from matplotlib.gridspec import GridSpec
    import matplotlib.ticker as mticker

    unit_prefixes               = {15: 'Peta', 14: '*10^2 Tera', 13: '*10^1 Tera', 12: 'Tera', 9: 'Giga', 0: ''}

    file_data                   = [glob(f'{path_hist}/{name_case}*.clm2.h0.{yy:04d}*')[0] for yy in range(year_start, year_end + 1)]

    data_grid                   = Dataset(f'{path_grid}/{file_grid}')

    lat                         = data_grid.variables[var_lat][:]
    lon                         = data_grid.variables[var_lon][:]

    if not file_data: print('No files available. Check path! Ciao.')

    if len(file_data) == 1: data = Dataset(file_data)
    if len(file_data) > 1: data = MFDataset(file_data)

    time                        = np.arange(f'{year_start}-01-01', f'{year_end + 1}-01-01', dtype = 'datetime64[M]')
        
    time_plot                   = np.arange(f'{year_start}-01-01', f'{year_end + 1}-01-01', subperiod, dtype = 'datetime64[Y]')
        
    time_sub                    = [i for i in range(len(time)) if time[i].astype('datetime64[Y]') in time_plot]

    landfrac                    = data.variables['landfrac'][:,:]
    area                        = data.variables['area'][:,:]
    area_meter                  = area * 10**6 
    landarea                    = landfrac * area_meter

    for var in variables:
        
        print(f'Check variable: {var}...\n')
        print('Load variable in all sub-periods...\n')
        var_sub                 = data.variables[var][time_sub,:,:] * var_factor[var]
        
        print('Calculate means of each year in each subperiod...\n')
        var_sub_yr_mean         = var_sub.reshape((-1, 12, *lat.shape)).mean(axis = 1)

        print('Determine subperiod change maps...\n')
        var_sub_yr_mean_diff    = np.ma.diff(var_sub_yr_mean, axis = 0)
        delta_map_0             = var_sub_yr_mean_diff[-1]
        delta_map_1             = var_sub_yr_mean_diff[-2]
        
        print('Calculate mean of each year in each subperiod...\n')
        if landarea_agg_method[var] == '':
          var_area              = var_sub_yr_mean
        else:
          land_factor           = landarea / np.sum(landarea) if var == 'TLAI' else landarea
          landarea_agg_func     = getattr(np, landarea_agg_method[var])
          var_area              = landarea_agg_func(var_sub_yr_mean, land_factor)

        print('Adjust units and magnitudes...\n')
        var_area_unit           = var_area * 10**-magnitudes[var]

        print('Calculate global aggregate time series...\n')
        agg_func                = getattr(np, agg_method[var])
        var_glob_agg            = agg_func(var_area_unit, axis = (1,2))
        
        print('Calculate the delta between the sub-periods...\n')
        var_glob_diff           = np.ma.diff(var_glob_agg / subperiod, axis = 0)

        print('Check where the delta thresholds were kept...\n')
        mask_threshold          = np.ma.where(np.abs(var_glob_diff) < glob_thresh[var], True, False)

        print('Check which year the threshold was reached...\n')
        threshold_year          = None if not any(mask_threshold) else time_plot[np.argwhere(mask_threshold).item(0)]

        print('Quantify landarea in disequilibrium...\n')
        landarea_disequil       = np.ma.where(var_sub_yr_mean_diff / subperiod > cell_thresh, landarea, 0)
        
        percent_landarea_disequil = 100 * np.sum(landarea_disequil, axis = (1, 2)) / np.sum(landarea)

        mask_area_threshold     = np.ma.where(np.abs(percent_landarea_disequil) < relative_area_thresh, True, False)

        threshold_year_area     = None if not any(mask_area_threshold) else time_plot[np.argwhere(mask_area_threshold).item(0)]

        print('========================================================================')
        print(f'{var} steady state check summary')
        print('========================================================================\n')

        if threshold_year is None: print(f'{var} is NOT in steady state.\n')
        else: print(f'{var} is in steady state! It was reached after {threshold_year} years.\n')

        if threshold_year_area is None: 
            print(f'{var} relative land area steady state threshold not reached.')
            print(f'{percent_landarea_disequil[-1]}% of land area in steady state > {relative_area_thresh}%')
        else: print(f'{var} relative land area steady state threshold was reached in year {threshold_year_area}.\n')

        with PdfPages(f'spinup_output/spinup_{var}_{name_case}_{time_plot[-1]}.pdf') as pdf:

            fig                 = plt.figure(figsize=(5, 5), dpi = 300)
            ax                  = fig.add_subplot(111, frameon = False)
            ax.set_title(var)
            ax.set_ylabel(f'{unit_prefixes[magnitudes[var]]} {units[var]}')
            ax.set_xlabel('Year')
            ax.grid(which = 'major', color = 'dimgray', visible = True, ls = '--', alpha = 0.6, zorder = 0)
            ax.plot(np.arange(year_start, year_end, subperiod), var_glob_agg, c = 'darkgreen', ls = '-', lw = 3)
            pdf.savefig()
            plt.close()

            fig                 = plt.figure(figsize=(5, 5), dpi = 300)
            ax                  = fig.add_subplot(111, frameon = False)
            ax.set_title(f'\u0394{var}')
            ax.set_ylabel(f'\u0394 {unit_prefixes[magnitudes[var]]} {units[var]} ' + r'$\mathdefault{year^{-1}}$')
            ax.set_xlabel('Year')
            ax.grid(which = 'major', color = 'dimgray', visible = True, ls = '--', alpha = 0.6, zorder = 0)
            ax.axhline(glob_thresh[var], c = 'k', ls='--', lw = 1.1 )
            ax.axhline(-glob_thresh[var], c = 'k', ls='--', lw = 1.1)
            ax.plot(np.arange(year_start, year_end, subperiod)[1:], var_glob_diff, c = 'firebrick', ls = '-', lw = 3)
            pdf.savefig()
            plt.close()

            fig                 = plt.figure(figsize=(5, 5), dpi = 300)
            ax                  = fig.add_subplot(111, frameon = False)
            ax.set_title(f'% of total land area in {var} disequilibrium')
            ax.set_ylabel(r'$\mathdefault{\%}$')
            ax.set_xlabel('Year')
            ax.grid(which = 'major', color = 'dimgray', visible = True, ls = '--', alpha = 0.6, zorder = 0)
            ax.axhline(relative_area_thresh, c = 'k', ls='--', lw = 1.1 )
            ax.plot(np.arange(year_start, year_end, subperiod)[1:], percent_landarea_disequil, c = 'firebrick', ls = '-', lw = 3)
            pdf.savefig()
            plt.close()


            fig                 = plt.figure(figsize=(7, 5), dpi = 300, constrained_layout = True)
            rp                  = crs.RotatedPole(pole_longitude = -162.0,
                                    pole_latitude = 39.25,
                                    globe = crs.Globe(semimajor_axis = 6370000,
                                    semiminor_axis = 6370000))

            gs                  = GridSpec(figure = fig, 
                                    ncols = 2, nrows = 1, 
                                    width_ratios = [12, 1],
                                    wspace = 0.1)

            ax                  = fig.add_subplot(gs[0,0], projection = rp, frameon = True)
            cax                 = fig.add_subplot(gs[0,1], frameon = False)

            ax.set_title(f'{var} steady state reached?')
            pc                  = crs.PlateCarree()
            xs, ys, _           = rp.transform_points(pc, np.array([351.1, 58]), np.array([26, 65.5])).T
            ax.set_extent([*xs,*ys])
            cmap                = mpl.colormaps.get_cmap('coolwarm').resampled(2)
            artist = ax.pcolormesh(lon, lat, landarea_disequil[-1,:,:], rasterized=True, cmap = cmap, vmin = 0, vmax = 1, transform = pc, zorder = 0)
            
            ax.coastlines(linewidth = 1, zorder=2)
    
            gl                  = ax.gridlines(crs = pc, 
                                        linewidth = 0.8,
                                        color = 'dimgray', 
                                        linestyle = '--', 
                                        draw_labels = True, 
                                        x_inline = False, 
                                        y_inline = False, 
                                        zorder = 3)
            
            gl.top_labels       = False
            gl.left_labels      = False
            gl.xlocator         = mticker.FixedLocator([-40, -20, 0, 20, 40, 60, 80])
            gl.ylocator         = mticker.FixedLocator([-20, 0, 20, 40, 60, 80])

            cbar = plt.colorbar(artist, cax = cax, extend = 'neither')
            cbar.ax.set_yticks([0.25, 0.75], ['Yes', 'No'])
            
            pdf.savefig()
            plt.close()


            fig                 = plt.figure(figsize=(7, 5), 
                                             dpi = 300, 
                                             constrained_layout = True)
            
            rp                  = crs.RotatedPole(pole_longitude = -162.0,
                                    pole_latitude = 39.25,
                                    globe = crs.Globe(semimajor_axis = 6370000,
                                    semiminor_axis = 6370000))

            gs                  = GridSpec(figure = fig, 
                                    ncols = 2, nrows = 1, 
                                    width_ratios = [12, 1],
                                    wspace = 0.1)

            ax                  = fig.add_subplot(gs[0,0], projection = rp, frameon = True)
            cax                 = fig.add_subplot(gs[0,1], frameon = False)
            ax.set_title(f'Last subperiod \u0394 {var}')
            pc                  = crs.PlateCarree()
            xs, ys, _           = rp.transform_points(pc, np.array([351.1, 58]), np.array([26, 65.5])).T
            ax.set_extent([*xs,*ys])
            cmap                = mpl.colormaps.get_cmap('coolwarm')
            artist = ax.pcolormesh(lon, lat, delta_map_0, rasterized=True, vmin = -10, vmax = 10, cmap = cmap, transform = pc, zorder = 0)
            
            ax.coastlines(linewidth = 1, zorder=2)
    
            gl                  = ax.gridlines(crs = pc, 
                                        linewidth = 0.8,
                                        color = 'dimgray', 
                                        linestyle = '--', 
                                        draw_labels = True, 
                                        x_inline = False, 
                                        y_inline = False, 
                                        zorder = 3)
            
            gl.top_labels       = False
            gl.left_labels      = False
            gl.xlocator         = mticker.FixedLocator([-40, -20, 0, 20, 40, 60, 80])
            gl.ylocator         = mticker.FixedLocator([-20, 0, 20, 40, 60, 80])

            cbar = plt.colorbar(artist, cax = cax, extend = 'neither')
            cbar.ax.set_ylabel(f'\u0394 {units[var]}', rotation = 270)
            
            pdf.savefig()
            plt.close()

if __name__ == '__main__':

    #from argparse import ArgumentParser
    
    #parser                          = ArgumentParser()

    #parser.add_argument('--name', '-n', help = 'Name for your work', type = str)

    check_steady_state(name_case = 'CLM5-EUR0275-BGC_spinup_0001', 
                       subperiod = 10,
                       path_hist = '/p/scratch/cjibg31/jibg3105/data/CLM5EUR0275/spinup/history/',
                       year_start = 438, 
                       year_end = 833,
                       path_grid = '/p/scratch/cjibg31/jibg3105/CESMDataRoot/InputData/share/domains/',
                       file_grid = 'domain.lnd.CLM5EU3_v4.nc',
                       var_lat = 'yc', 
                       var_lon = 'xc' )