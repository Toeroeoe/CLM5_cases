
test = {

    'dir_script': '/p/project/cjibg31/jibg3105/clm5.0/cime/scripts',
    'name': 'CLM5-EUR0275-BGC_SCENIC_JR',
    'compset': '2000_DATM%CRUv7_CLM50%BGC-CROP_SICE_SOCN_MOSART_SGLC_SWAV',
    'partition': 'dc-cpu',
    'n_cpu': 1024,
    'ncpl': 24,
    'wallclock': '5:00:00',
    'months_per_wallclock': 1,
    'dir_output': '/p/scratch/cjibg31/jibg3105/CESMDataRoot/CaseOutputs/',
    
    'hist_frq_grid': -24,
    'hist_flt_grid': 365,
    'hist_frq_pft': -24,
    'hist_flt_pft': 365,
    'mode_datm': 'CLMCRUNCEPv7',
    'hist_vars_grid': [
                        ## Vegetation function
                        'TLAI', # Total leaf-area-index
                        
                        ## Evaporation
                        'Qle', # Total evaporation
                        ],

    'hist_vars_pft': [],
    'year_start': 2018,
    'month_start': 1,

    'year_end': 2018,
    'month_end': 1,

    'year_start_forcing': 2018,
    'month_start_forcing': 1,

    'year_end_forcing': 2018,
    'month_end_forcing': 1,
    
    'dir_domain_lnd': '/p/scratch/cjibg31/jibg3105/CESMDataRoot/InputData/share/domains/EUR-0275/domain/',
    'file_domain_lnd': 'domain.lnd.EUR-0275_final.nc',

    'dir_domain_atm': '/p/scratch/cjibg31/jibg3105/projects/SCENIC/forcing_domain/',
    'file_domain_atm': 'domain.lnd.EUR-11_focus_EUR-11_focus.241213_final.nc',

    'domain_atm_vars': {'time': 'time',
                        'xc': 'lon',
                        'yc': 'lat',
                        'area': 'area',
                        'mask': 'mask'},

    'dir_surf': '/p/scratch/cjibg31/jibg3105/CESMDataRoot/InputData/lnd/clm2/surfdata_map/EUR_0275/',
    'file_surf': 'surfdata_EUR-0275_hist_78pfts_Irrig_CMIP6_simyr2000_c230216_GLC2000.nc',

    'dir_init': '/p/scratch/cjibg31/jibg3105/data/CLM5EUR0275/restart/',
    'file_init': 'CLM5_EUR0275-BGC_0001_production_1989-01-01.nc',

    'dir_forcing': '/p/scratch/cjibg31/jibg3105/projects/SCENIC/forcing/',

    'vars_forcing' : {'swdn': 'FSDS',
                      'precn': 'PRECTmms',
                      'tbot': 'TBOT',
                      'wind': 'WIND',
                      'pbot': 'PSRF',
                      'lwdn': 'FLDS',
                      'shum': 'QBOT'},

    'time_resolution_forcing_hours': 1,

    'mode_co2': None, 

    'type_co2': 'constant', 
    'ppmv_co2': 379.0, 
    
    'series_co2': None,

    'coldstart': False,

    'job_archive': False,

    'AD_spin_up': False,

    'continue_run': False

}
