
test = {

    'dir_script': '/p/project/cjibg31/jibg3105/clm5.0/cime/scripts',
    'name': 'CLM5-EUR0275-BGC_0001_JR_spinup_AD',
    'compset': '2000_DATM%CRUv7_CLM50%BGC-CROP_SICE_SOCN_MOSART_SGLC_SWAV',
    'partition': 'dc-cpu',
    'n_cpu': 1024,
    'ncpl': 24,
    'wallclock': '24:00:00',
    'months_per_wallclock': 84,
    'dir_output': '/p/scratch/cjibg31/jibg3105/CESMDataRoot/CaseOutputs/',
    
    'hist_frq_grid': 0,
    'hist_flt_grid': 12,
    'hist_frq_pft': -24,
    'hist_flt_pft': 365,
    'mode_datm': 'CLMCRUNCEPv7',
       'hist_vars_grid': ['GPP', 'TLAI', 'TOTECOSYSC', 'TOTECOSYSN', 'TOTSOMC', 'TOTVEGC', 'TWS'],
    'hist_vars_pft': [],

    'year_start': 1,
    'month_start': 1,

    'year_end': 1500,
    'month_end': 12,

    'year_start_forcing': 1950,
    'month_start_forcing': 1,

    'year_end_forcing': 1959,
    'month_end_forcing': 12,

    'dir_domain_lnd': '/p/scratch/cjibg31/jibg3105/CESMDataRoot/InputData/share/domains/EUR-0275/domain/',
    'file_domain_lnd': 'domain.lnd.EUR-0275_final.nc',

    'dir_domain_atm': '/p/scratch/cjibg31/jibg3105/CESMDataRoot/InputData/share/domains/EUR-0275/domain/',
    'file_domain_atm': 'domain.lnd.EUR-0275_final.nc',

    'domain_atm_vars': {'time': 'time',
                        'lon': 'xc',
                        'lat': 'yc',
                        'area': 'area',
                        'mask': 'mask'},

    'dir_surf': '/p/scratch/cjibg31/jibg3105/CESMDataRoot/InputData/lnd/clm2/surfdata_map/EUR_0275/',
    'file_surf': 'surfdata_EUR-0275_hist_78pfts_Irrig_CMIP6_simyr2000_c230216_GLC2000_corrected_3.nc',

    'dir_init': None,
    'file_init': None,

    'init_interpolation': False,

    'dir_forcing': '/p/data1/jibg31/poppe1/FORCINGS/ERA5/spinup/',

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

    'coldstart': True,

    'job_archive': False,

    'AD_spin_up': True,

    'continue_run': False

}
