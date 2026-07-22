
YG_test = {
    'computer': 'JURECA',
    'dir_script': '/p/project1/cjibg31/jibg3105/clm5.0/cime/scripts',
    'name': 'CLM5_1PT_ID-Pag',
    'compset': '2000_DATM%CRUv7_CLM50%BGC-CROP_SICE_SOCN_MOSART_SGLC_SWAV',
    'partition': 'dc-cpu',
    'n_cpu': 1,
    'ncpl': 48,
    'wallclock': '24:00:00',
    'months_per_wallclock': 12000,
    'dir_output': '/p/scratch/cjibg31/jibg3105/CESMDataRoot/CaseOutputs/',

    'hist_frq_grid': -24,
    'hist_flt_grid': 365,
    'hist_frq_pft': -24,
    'hist_flt_pft': 365,
    'mode_datm': 'CLMCRUNCEPv7',
    'hist_vars_grid': ['GPP',
                       'TOTECOSYSC',
                       'TOTSOMC',
                       'TOTVEGC',
                       'TLAI',
                       'TWS',
                    ],

    'hist_vars_pft': [],
    'year_start': 1,
    'month_start': 1,
    'day_start': 1,

    'year_end': 2000,
    'month_end': 12,
    'day_end': 31,

    'year_start_forcing': 2004,
    'month_start_forcing': 1,

    'year_end_forcing': 2019,
    'month_end_forcing': 12,

    'dtlimit': None,

    'dir_domain_lnd': '/p/scratch/cjibg31/ginting1/BORNEO/sites/inputdata/ID-Pag/domain/',
    'file_domain_lnd': 'domain.lnd.ID-Pag.c251213.nc',

    'dir_domain_atm': '/p/scratch/cjibg31/ginting1/BORNEO/sites/inputdata/ID-Pag/domain/',
    'file_domain_atm': 'domain.lnd.ID-Pag.c251213.nc',

    'domain_atm_vars': {'time': 'time',
                        'lon': 'xc',
                        'lat': 'yc',
                        'area': 'area',
                        'mask': 'mask'},

    'dir_surf': '/p/scratch/cjibg31/ginting1/BORNEO/sites/inputdata/ID-Pag/surfdata/',
    'file_surf': 'surfdata_ID-Pag_hist_78pfts_CMIP6_simyr2000_c251216.nc',

    #'dir_init': '/p/scratch/cjibg31/jibg3105/CESMDataRoot/CaseOutputs/1PT_Aurade_T_ET/run/',
    #'file_init': '1PT_Aurade_T_ET.clm2.r.2022-01-01-00000.nc',

    'dir_forcing': '/p/scratch/cjibg31/ginting1/BORNEO/sites/inputdata/ID-Pag/CLM1PT_JAPANFLUX_ERA5/',

    'vars_forcing' : {'swdn': 'FSDS',
                      'precn': 'PRECTmms',
                      'tbot': 'TBOT',
                      'wind': 'WIND',
                      'pbot': 'PSRF',
                      'lwdn': 'FLDS',
                      'rh': 'RH'},

    'time_resolution_forcing_hours': 1,

    #'mode_co2': 'CO2A',

    #'type_co2': 'constant',
    #'ppmv_co2': ,

    #'series_co2': '20tr',

    #'file_domain_co2': 'greenhouse_ssp370_adjusted.nc',
    #'file_co2': 'greenhouse_ssp370_adjusted.nc',

    'coldstart': True,

    'job_archive': False,

    'AD_spin_up': False,

    'continue_run': False

}
