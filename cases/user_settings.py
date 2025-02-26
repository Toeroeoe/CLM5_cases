

CLM5_BGC_EUR_0275_spinup_test_JR = {

    'dir_script': '/p/project/cjibg31/jibg3105/clm5.0/cime/scripts',
    'name': 'CLM5-EUR0275-BGC_spinup_0001_JR',
    'compset': '2000_DATM%CRUv7_CLM50%BGC-CROP_SICE_SOCN_MOSART_SGLC_SWAV',
    'n_cpu': 1024,
    'ncpl': 24,
    'wallclock': '20:00:00',
    'months_per_wallclock': 72,
    'dir_output': '/p/scratch/cjibg31/jibg3105/CESMDataRoot/CaseOutputs/',
    
    'hist_frq_grid': 0,
    'hist_flt_grid': 12,
    'hist_frq_pft': -24,
    'hist_flt_pft': 365,
    'mode_datm': 'CLMCRUNCEPv7',
    'hist_vars_grid': ['GPP', 'TLAI', 'TOTECOSYSC', 'TOTECOSYSN', 'TOTSOMC', 'TOTVEGC', 'TWS'],
    'hist_vars_pft': [],

    'year_start': 546,
    'month_start': 1,

    'year_end': 605,
    'month_end': 12,

    'year_start_forcing': 1950,
    'month_start_forcing': 1,

    'year_end_forcing': 1959,
    'month_end_forcing': 12,
    
    'dir_domain_lnd': '/p/scratch/cjibg31/jibg3105/CESMDataRoot/InputData/share/domains/EUR-0275/domain/',
    'file_domain_lnd': 'domain.lnd.EUR-0275_final.nc',

    'dir_domain_atm': '/p/scratch/cjibg31/jibg3105/CESMDataRoot/InputData/share/domains/EUR-0275/domain',
    'file_domain_atm': 'domain.lnd.EUR-0275_final.nc',

    'dir_surf': '/p/scratch/cjibg31/jibg3105/CESMDataRoot/InputData/lnd/clm2/surfdata_map/EUR_0275/',
    'file_surf': 'surfdata_EUR-0275_hist_78pfts_Irrig_CMIP6_simyr2000_c230216_GLC2000.nc',

    'dir_init': '/p/scratch/cjibg31/jibg3105/data/CLM5EUR0275/spinup/restart/',
    'file_init': 'CLM5-EUR0275-BGC_spinup_0001_JW.clm2.r.0546-01-01-00000.nc',

    'dir_forcing': '/p/scratch/cjibg31/jibg3105/CESMDataRoot/InputData/Forcings/ERA5_EUR-0275/spinup/',

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
    'ppmv_co2': 315.98, 
    
    'series_co2': None,

    'coldstart': False,

    'job_archive': False,

    'AD_spin_up': False,

    'continue_run': False

}



CLM5_BGC_EUR_0275_spinup = {

    'dir_script': '/p/project/cjibg31/jibg3105/clm5.0/cime/scripts',
    'name': 'CLM5-EUR0275-BGC_spinup_0001_JW',
    'compset': '2000_DATM%CRUv7_CLM50%BGC-CROP_SICE_SOCN_MOSART_SGLC_SWAV',
    'n_cpu': 1024,
    'ncpl': 24,
    'wallclock': '20:00:00',
    'months_per_wallclock': 72,
    'dir_output': '/p/scratch/cjibg31/jibg3105/CESMDataRoot/CaseOutputs/',
    
    'hist_frq_grid': 0,
    'hist_flt_grid': 12,
    'hist_frq_pft': -24,
    'hist_flt_pft': 365,
    'mode_datm': 'CLMCRUNCEPv7',
    'hist_vars_grid': ['GPP', 'TLAI', 'TOTECOSYSC', 'TOTECOSYSN', 'TOTSOMC', 'TOTVEGC', 'TWS'],
    'hist_vars_pft': [],

    'year_start': 894,
    'month_start': 1,

    'year_end': 753,
    'month_end': 12,

    'year_start_forcing': 1950,
    'month_start_forcing': 1,

    'year_end_forcing': 1959,
    'month_end_forcing': 12,
    
    'dir_domain_lnd': '/p/scratch/cjibg31/jibg3105/CESMDataRoot/InputData/share/domains/EUR-0275/domain/',
    'file_domain_lnd': 'domain.lnd.EUR-0275_final.nc',

    'dir_domain_atm': '/p/scratch/cjibg31/jibg3105/CESMDataRoot/InputData/share/domains/EUR-0275/domain',
    'file_domain_atm': 'domain.lnd.EUR-0275_final.nc',

    'dir_surf': '/p/scratch/cjibg31/jibg3105/CESMDataRoot/InputData/lnd/clm2/surfdata_map/EUR_0275/',
    'file_surf': 'surfdata_EUR-0275_hist_78pfts_Irrig_CMIP6_simyr2000_c230216_GLC2000.nc',

    'dir_init': '/p/scratch/cjibg31/jibg3105/data/CLM5EUR0275/spinup/restart/',
    'file_init': 'CLM5-EUR0275-BGC_spinup_0001_JW.clm2.r.0894-01-01-00000.nc',

    'dir_forcing': '/p/scratch/cjibg31/jibg3105/CESMDataRoot/InputData/Forcings/ERA5_EUR-0275/spinup/',

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
    'ppmv_co2': 315.98, 
    
    'series_co2': None,

    'coldstart': False,

    'job_archive': False,

    'AD_spin_up': False,

    'continue_run': False

}


CLM5_BGC_EUR_0275_ML_west = {

    'dir_script': '/p/project/cjibg31/jibg3105/clm5.0/cime/scripts',
    'name': 'CLM5_BGC_EUR_0275_ML_west_0000_JW',
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

    'year_start': 2019,
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
    'file_surf': 'surfdata_CLM5EU3_FATES_west.nc',

    'dir_init': '/p/scratch/cjibg31/jibg3105/data/CLM5EUR0275/ML_spinup/not_coldstart/restart/west',
    'file_init': 'CLM5_BGC_EUR_0275_ML_west_0000.clm2.r.2019-01-01-00000.nc',

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
    'ppmv_co2': 379.0, 
    
    'series_co2': None,

    'methane_model': False,

    'coldstart': False,

    'job_archive': False,

    'AD_spin_up': False,

    'continue_run': False

}

CLM5_BGC_EUR_0275_ML_east= {

    'dir_script': '/p/project/cjibg31/jibg3105/clm5.0/cime/scripts',
    'name': 'CLM5_BGC_EUR_0275_ML_east_0000_JW',
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

    'year_start': 2019,
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
    'file_surf': 'surfdata_CLM5EU3_FATES_east.nc',

    'dir_init': '/p/scratch/cjibg31/jibg3105/data/CLM5EUR0275/ML_spinup/not_coldstart/restart/east/',
    'file_init': 'CLM5_BGC_EUR_0275_ML_east_0000.clm2.r.2019-01-01-00000.nc',

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
    'ppmv_co2': 379.0, 
    
    'series_co2': None,

    'methane_model': False,

    'coldstart': False,

    'job_archive': False,

    'AD_spin_up': False,

    'continue_run': False

}
