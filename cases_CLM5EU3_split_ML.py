CLM5_BGC_EUR_0275_ML_west = {

    'dir_script': '/p/project/cjibg31/jibg3105/clm5.0/cime/scripts',
    'name': 'CLM5_BGC_EUR_0275_ML_west_0010_JW',
    'compset': 'I2000Clm50BgcCruGs',
    'n_cpu': 384,
    'ncpl': 24,
    'wallclock': '24:00:00',
    'dir_output': '/p/scratch/cjibg31/jibg3105/CESMDataRoot/CaseOutputs',
    
    'months_per_wallclock': 120,
    
    'hist_frq_grid': -24,
    'hist_flt_grid': 365,
    'hist_frq_pft': -24,
    'hist_flt_pft': 365,
    'mode_datm': 'CLMCRUNCEPv7',
    'hist_vars_grid': ['GPP', 'TLAI', 'TOTECOSYSC', 'TOTECOSYSN', 'TOTSOMC', 'TOTVEGC', 'TWS'],
    'hist_vars_pft': [],

    'year_start': 1995,
    'month_start': 1,

    'year_end': 2118,
    'month_end': 12,

    'year_start_forcing': 1995,
    'month_start_forcing': 1,

    'year_end_forcing': 2018,
    'month_end_forcing': 12,
    
    'dir_domain_lnd': '/p/scratch/cjibg31/jibg3105/CESMDataRoot/InputData/share/domains/',
    'file_domain_lnd': 'domain.lnd.CLM5EU3_FATES_west.c200814.nc',

    'dir_domain_atm': '/p/scratch/cjibg31/jibg3105/CESMDataRoot/InputData/share/domains/',
    'file_domain_atm': 'domain.lnd.CLM5EU3_FATES_west.c200814.nc',

    'dir_surf': '/p/scratch/cjibg31/jibg3105/CESMDataRoot/InputData/lnd/clm2/surfdata_map/',
    'file_surf': 'surfdata_CLM5EU3_FATES_west_v3.nc',

    'dir_init': '/p/scratch/cjibg31/jibg3105/CESMDataRoot/InputData/lnd/clm2/initdata_map/CLM5EU3_split_ML/warmstart_ML/',
    'file_init': 'CLM5EU3_BGC_west_ML_warmstart_004.nc',

    'dir_forcing': '/p/scratch/cjibg31/jibg3105/CESMDataRoot/InputData/Forcings/CLM5EU3_west/',

    'vars_forcing' : {  'swdn': 'FSDS',
                        'precn': 'PRECTmms',
                        'tbot': 'TBOT',
                        'wind': 'WIND',
                        'pbot': 'PSRF',
                        'rh': 'RH'},

    'time_resolution_forcing_hours': 6,

    'mode_co2': None, 

    'type_co2': 'constant', 
    'ppmv_co2': 367.0, 
    
    'series_co2': None,

    'methane_model': False,

    'coldstart': False,

    'job_archive': False,

    'AD_spin_up': False,

    'continue_run': False

}

CLM5_BGC_EUR_0275_ML_east= {

    'dir_script': '/p/project/cjibg31/jibg3105/clm5.0/cime/scripts',
    'name': 'CLM5_BGC_EUR_0275_ML_east_0010_JW',
    'compset': 'I2000Clm50BgcCruGs',
    'n_cpu': 1024,
    'ncpl': 24,
    'wallclock': '24:00:00',
    'dir_output': '/p/scratch/cjibg31/jibg3105/CESMDataRoot/CaseOutputs',

    'months_per_wallclock': 60,
    
    'hist_frq_grid': -24,
    'hist_flt_grid': 365,
    'hist_frq_pft': -24,
    'hist_flt_pft': 365,
    'mode_datm': 'CLMCRUNCEPv7',
    'hist_vars_grid': ['GPP', 'TLAI', 'TOTECOSYSC', 'TOTECOSYSN', 'TOTSOMC', 'TOTVEGC', 'TWS'],
    'hist_vars_pft': [],

    'year_start': 2065,
    'month_start': 1,

    'year_end': 2118,
    'month_end': 12,

    'year_start_forcing': 1995,
    'month_start_forcing': 1,

    'year_end_forcing': 2018,
    'month_end_forcing': 12,
    
    'dir_domain_lnd': '/p/scratch/cjibg31/jibg3105/CESMDataRoot/InputData/share/domains/',
    'file_domain_lnd': 'domain.lnd.CLM5EU3_FATES_east.c200814.nc',

    'dir_domain_atm': '/p/scratch/cjibg31/jibg3105/CESMDataRoot/InputData/share/domains/',
    'file_domain_atm': 'domain.lnd.CLM5EU3_FATES_east.c200814.nc',

    'dir_surf': '/p/scratch/cjibg31/jibg3105/CESMDataRoot/InputData/lnd/clm2/surfdata_map/',
    'file_surf': 'surfdata_CLM5EU3_FATES_east_v3.nc',

    'dir_init': '/p/scratch/cjibg31/jibg3105/data/CLM5EUR0275/ML_spinup/not_coldstart/east/restart/',
    'file_init': 'CLM5_BGC_EUR_0275_ML_east_0010_JW.clm2.r.2065-01-01-00000.nc',

    'dir_forcing': '/p/scratch/cjibg31/jibg3105/CESMDataRoot/InputData/Forcings/CLM5EU3_east/',

    'vars_forcing' : {  'swdn': 'FSDS',
                        'precn': 'PRECTmms',
                        'tbot': 'TBOT',
                        'wind': 'WIND',
                        'pbot': 'PSRF',
                        'rh': 'RH'},

    'time_resolution_forcing_hours': 6,

    'mode_co2': None, 

    'type_co2': 'constant', 
    'ppmv_co2': 367.0, 
    
    'series_co2': None,

    'methane_model': False,

    'coldstart': False,

    'job_archive': False,

    'AD_spin_up': False,

    'continue_run': False

}
