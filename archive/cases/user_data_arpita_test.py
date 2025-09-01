
west = {

    'dir_script': '/p/project/cjibg31/jibg3105/clm5.0/cime/scripts',
    'name': 'CLM5_BGC_EUR_Arpita_check_west_JW',
    'compset': 'I2000Clm50BgcCruGs',
    'n_cpu': 384,
    'ncpl': 24,
    'wallclock': '24:00:00',
    'dir_output': '/p/scratch/cjibg31/jibg3105/CESMDataRoot/CaseOutputs',
    
    'months_per_wallclock': 180,
    
    'hist_frq_grid': -24,
    'hist_flt_grid': 365,
    'hist_frq_pft': -24,
    'hist_flt_pft': 365,
    'mode_datm': 'CLMCRUNCEPv7',
    'hist_vars_grid': ['DISPVEGC', 'ER', 'GPP', 'LEAFC', 'NBP', 'TSOI', 'EFLX_LH_TOT', 'NEE', 
                       'NPP', 'TOTCOLC', 'TOTECOSYSC', 'TOTPFTC', 'EFLX_GNET', 'TOTSOMC', 
                       'TOTVEGC', 'Qle', 'Rnet', 'SWdown', 'TBOT', 'SWup', 'Qh', 'LWdown', 
                       'LWup', 'QRUNOFF', 'QSOIL', 'QVEGE', 'QVEGT', 'FCEV', 'FCTR', 'FGEV', 
                       'FGR', 'FSNO', 'QCHARGE', 'RAIN', 'QOVER', 'QIRRIG', 'QINFL', 'QINTR', 
                       'QFLX_EVAP_VEG', 'QFLX_EVAP_GRND', 'QFLX_EVAP_TOT', 'H2OCAN', 'QDRAI', 
                       'H2OSNO', 'H2OSOI', 'RH', 'SNOW', 'SNOWDP', 'SNOWLIQ', 'TLAI', 'TSAI', 
                       'TWS', 'ZWT', 'GSSHA', 'GSSUN'],
    'hist_vars_pft': [],

    'year_start': 2008,
    'month_start': 1,

    'year_end': 2022,
    'month_end': 12,

    'year_start_forcing': 2008,
    'month_start_forcing': 1,

    'year_end_forcing': 2022,
    'month_end_forcing': 12,
    
    'dir_domain_lnd': '/p/scratch/cjibg31/jibg3105/CESMDataRoot/InputData/share/domains/',
    'file_domain_lnd': 'domain.lnd.CLM5EU3_FATES_west.c200814.nc',

    'dir_domain_atm': '/p/scratch/cjibg31/jibg3105/CESMDataRoot/InputData/share/domains/',
    'file_domain_atm': 'domain.lnd.CLM5EU3_FATES_west.c200814.nc',

    'dir_surf': '/p/scratch/cjibg31/jibg3105/CESMDataRoot/InputData/lnd/clm2/surfdata_map/',
    'file_surf': 'surfdata_CLM5EU3_FATES_west.nc',

    'dir_init': '/p/scratch/cjibg31/jibg3105/CESMDataRoot/InputData/lnd/clm2/initdata_map/FINAL/',
    'file_init': 'CLM5EU3_BGC_west_JR2.clm2.r.3204-01-01-00000.nc',

    'dir_forcing': '/p/scratch/cjibg36/bose1/CLM5_DATA/inputdata/atm/datm7/CLM5EU3_BGC_west_new/',

    'vars_forcing' : {  'swdn': 'FSDS',
                        'precn': 'PRECTmms',
                        'tbot': 'TBOT',
                        'wind': 'WIND',
                        'pbot': 'PSRF',
                        'lwdn': 'FLDS',
                        'shum': 'QBOT'},

    'time_resolution_forcing_hours': 3,

    'mode_co2': None, 

    'type_co2': 'constant', 
    'ppmv_co2': 379.0, 
    
    'series_co2': None,

    'methane_model': True,

    'coldstart': False,

    'job_archive': False,

    'AD_spin_up': False,

    'continue_run': False

}

east = {

    'dir_script': '/p/project/cjibg31/jibg3105/clm5.0/cime/scripts',
    'name': 'CLM5_BGC_EUR_Arpita_check_east_JW',
    'compset': 'I2000Clm50BgcCruGs',
    'n_cpu': 1024,
    'ncpl': 24,
    'wallclock': '24:00:00',
    'dir_output': '/p/scratch/cjibg31/jibg3105/CESMDataRoot/CaseOutputs',

    'months_per_wallclock': 36,
    
    'hist_frq_grid': -24,
    'hist_flt_grid': 365,
    'hist_frq_pft': -24,
    'hist_flt_pft': 365,
    'mode_datm': 'CLMCRUNCEPv7',

    'hist_vars_grid': ['DISPVEGC', 'ER', 'GPP', 'LEAFC', 'NBP', 'TSOI', 'EFLX_LH_TOT', 'NEE', 
                       'NPP', 'TOTCOLC', 'TOTECOSYSC', 'TOTPFTC', 'EFLX_GNET', 'TOTSOMC', 
                       'TOTVEGC', 'Qle', 'Rnet', 'SWdown', 'TBOT', 'SWup', 'Qh', 'LWdown', 
                       'LWup', 'QRUNOFF', 'QSOIL', 'QVEGE', 'QVEGT', 'FCEV', 'FCTR', 'FGEV', 
                       'FGR', 'FSNO', 'QCHARGE', 'RAIN', 'QOVER', 'QIRRIG', 'QINFL', 'QINTR', 
                       'QFLX_EVAP_VEG', 'QFLX_EVAP_GRND', 'QFLX_EVAP_TOT', 'H2OCAN', 'QDRAI', 
                       'H2OSNO', 'H2OSOI', 'RH', 'SNOW', 'SNOWDP', 'SNOWLIQ', 'TLAI', 'TSAI', 
                       'TWS', 'ZWT', 'GSSHA', 'GSSUN'],

    'hist_vars_pft': [],

    'year_start': 2014,
    'month_start': 1,

    'year_end': 2022,
    'month_end': 12,

    'year_start_forcing': 2014,
    'month_start_forcing': 1,

    'year_end_forcing': 2022,
    'month_end_forcing': 12,
    
    'dir_domain_lnd': '/p/scratch/cjibg31/jibg3105/CESMDataRoot/InputData/share/domains/',
    'file_domain_lnd': 'domain.lnd.CLM5EU3_FATES_east.c200814.nc',

    'dir_domain_atm': '/p/scratch/cjibg31/jibg3105/CESMDataRoot/InputData/share/domains/',
    'file_domain_atm': 'domain.lnd.CLM5EU3_FATES_east.c200814.nc',

    'dir_surf': '/p/scratch/cjibg31/jibg3105/CESMDataRoot/InputData/lnd/clm2/surfdata_map/',
    'file_surf': 'surfdata_CLM5EU3_FATES_east.nc',

    'dir_init': '/p/scratch/cjibg31/jibg3105/CESMDataRoot/CaseOutputs/CLM5_BGC_EUR_Arpita_check_east_JW/run/',
    'file_init': 'CLM5_BGC_EUR_Arpita_check_east_JW.clm2.r.2014-01-01-00000.nc',

    'dir_forcing': '/p/scratch/cjibg36/bose1/CLM5_DATA/inputdata/atm/datm7/CLM5EU3_BGC_east_new/',

    'vars_forcing' : {  'swdn': 'FSDS',
                        'precn': 'PRECTmms',
                        'tbot': 'TBOT',
                        'wind': 'WIND',
                        'pbot': 'PSRF',
                        'lwdn': 'FLDS',
                        'shum': 'QBOT'},

    'time_resolution_forcing_hours': 3,

    'mode_co2': None, 

    'type_co2': 'constant', 
    'ppmv_co2': 379.0, 
    
    'series_co2': None,

    'methane_model': True,

    'coldstart': False,

    'job_archive': False,

    'AD_spin_up': False,

    'continue_run': False

}
