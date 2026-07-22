
T_ET = {
    'computer': 'JURECA',
    'dir_script': '/p/project1/cjibg31/jibg3105/clm5.0/cime/scripts',
    'name': '1PT_Aurade_T_ET',
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
    'hist_vars_grid': [
                        ### Carbon and nitrogen
                        #'DISPVEGC', # displayed veg carbon, excluding storage and cpool
                        #'DISPVEGN', # displayed vegetation nitrogen
                        #'DOWNREG',  # fractional reduction in GPP due to N limitation
                        'ER', # Ecosystem respiration
                        'GPP', # Gross primary production
                        #'GROSS_NMIN', # gross rate of N mineralization
                        #'LEAFC', # leaf carbon
                        #'LEAFN', # leaf nitrogen
                        #'LNC', # leaf N concentration
                        #'NBP', # net biome production, includes fire, landuse, and harvest flux, positive for sink	
                        #'NDEP_TO_SMINN', # atmospheric N deposition to soil mineral N
                        'NEE', # net ecosystem exchange
			            #'NEP', # Net ecosystem production
                        'NPP', # Net Primary Production
                        #'PLANT_NDEMAND', # N flux required to support initial GPP	
                        #'STORVEGC', # stored vegetation carbon, excluding cpool	
                        #'STORVEGN', # stored vegetation nitrogen, excluding cpool	
                        #'TOTCOLN', # total column nitrogen
                        #'TOTCOLC', # total column carbon
                        #'TOTECOSYSC', # total ecosystem carbon (veg + soil)
                        #'TOTECOSYSN', # total ecosystem nitrogen (veg + soil)
                        #'TOTPFTC', # total PFT level carbon
                        #'TOTPFTN', # total PFT level nitrogen
                        'TOTSOMC', # Total soil organic matter carbon
                        #'TOTSOMN', # Total soil organic matter nitrogen
                        'TOTVEGC', # total vegetation carbon
                        #'TOTVEGN', # Total vegetaiton nitrogen

                        ## Vegetation function
                        'TLAI', # Total leaf-area-index
                        #'TSAI', # total stem-area-index
                        #'BTRAN', # beta factor transpiration down regulation
                        'BTRANMN', # daily minimum beta transpiration factor
                        #'GSSHA', # stomatal conductance (shaded leaf)
                        #'GSSUN', # stomatal conductance (sunlit leaf)
                        
                        ## Radiation
			            'FSM', # Snow melt heat flux
                        'Rnet', # net radiation
                        'SWdown', # Shortwave radiation downwards incoming
                        'TBOT', # atmospheric air temperature
                        #'SWup', #Shortwave radiation upwards outgoing
                        'Qh', # Sensible heat
                        'TSOI', # Soil temperature
                        'LWdown', # Longwave radiation downwards incoming
                        #'LWup', # Longwave radiation upwards outgoing
                        #'Qstor', # storage heat flux (incl. snowmelt)
                        'ALBD', # Surface albedo (visible and near infra red bands)
                        'ALBGRD',  # Ground albedo
                        'ALBI', # Surface albido (indirect)
                        'ALBGRI', # Ground albido (indirect)
                        'FGR', # heat flux into soil
                        
                        ## Evaporation
                        #'Qle', # Total evaporation
			            #'FCEV', # Canopy evaporation
                        #'FCTR', # Canopy transpiration
                        #'FGEV', # Canopy evaporation

                        ## Snow
                        #'FSNO', # fraction snow cover
                        #'SNOWDP', # snow height
                        #'SNOWICE', # snow ice
                        #'SNOTTOPL', # snow temperature top layer
                        #'SNOWLIQ', # snow liquid water
                        #'QICE', # Ice growth, melt


                        ## Water balance
                        #'QCHARGE', #Aquifer recharge
                        'SNOW',  # atmospheric snow
                        'RAIN', # atmospheric rain
                        'QOVER', # Surface runoff
                        'QIRRIG', # Irrigation
                        'QINFL', # Infiltration
                        'QINTR', # Interception
                        'QFLX_EVAP_VEG', # Vegetation evaporation
                        'QFLX_EVAP_GRND', # Ground surface evaporation
                        'QFLX_EVAP_TOT', # Evapo transpiration
                        'H2OCAN', # Intercepted water
                        'QDRAI', # subsurface drainage
			            'H2OSNO', # snow depth (liq. water)
                        'H2OSOI', # volumentric soil water
                        'RH', # relative humidity
                        #'VPD', # Vapour pressure deficit
                        'TWS', # total water storage
                        'ZWT', # table water depth
                        'SOILPSI', # soil water potential
                        'VEGWP', # vegetation water potential
                        'watfc', # water field capacity
                        'SMP', # soil matric potential
                        ],

    'hist_vars_pft': [],
    'year_start': 1,
    'month_start': 1,
    'day_start': 1,

    'year_end': 2022,
    'month_end': 12,
    'day_end': 31,

    'year_start_forcing': 2022,
    'month_start_forcing': 1,

    'year_end_forcing': 2022,
    'month_end_forcing': 12,

    'dtlimit': None,
    
    'dir_domain_lnd': '/p/scratch/cjibg31/jibg3105/CESMDataRoot/InputData/share/domains/FR-Aur/',
    'file_domain_lnd': 'domain.lnd.Aurade_Aurade.251212.nc',

    'dir_domain_atm': '/p/scratch/cjibg31/jibg3105/CESMDataRoot/InputData/share/domains/FR-Aur/',
    'file_domain_atm': 'domain.lnd.Aurade_Aurade.251212.nc',

    'domain_atm_vars': {'time': 'time',
                        'lon': 'xc',
                        'lat': 'yc',
                        'area': 'area',
                        'mask': 'mask'},

    'dir_surf': '/p/scratch/cjibg31/jibg3105/CESMDataRoot/InputData/lnd/clm2/surfdata_map/1PT/FR-Aur/',
    'file_surf': 'surfdata_Aurade_hist_78pfts_CMIP6_simyr2000_c251212_adj_2.nc',

    #'dir_init': '/p/scratch/cjibg31/jibg3105/CESMDataRoot/CaseOutputs/1PT_Aurade_T_ET/run/',
    #'file_init': '1PT_Aurade_T_ET.clm2.r.2022-01-01-00000.nc',

    'dir_forcing': '/p/scratch/cjibg31/jibg3105/CESMDataRoot/InputData/Forcings/DETECT/1PT/FR-Aur/',

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
