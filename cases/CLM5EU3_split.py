CLM5EU3_BGC_007_west = {

    'dir_script': '/p/project/cjibg31/jibg3105/clm5.0/cime/scripts',
    'name': 'CLM5EU3_BGC_west_0007_JW',
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
    'hist_vars_grid':   [
                        ### Carbon and nitrogen
                            'DISPVEGC', # displayed veg carbon, excluding storage and cpool
                            'DISPVEGN', # displayed vegetation nitrogen
                            'DOWNREG',  # fractional reduction in GPP due to N limitation
                            'ER', # Ecosystem respiration
                            'GPP', # Gross primary production
                            'GROSS_NMIN', # gross rate of N mineralization
                            'LEAFC', # leaf carbon
                            'LEAFN', # leaf nitrogen
                            'LNC', # leaf N concentration
                            'NBP', # net biome production, includes fire, landuse, and harvest flux, positive for sink	
                            'NDEP_TO_SMINN', # atmospheric N deposition to soil mineral N
                            'NEE', # net ecosystem exchange
			                'NEP', # Net ecosystem production
                            'NPP', # Net Primary Production
                            'PLANT_NDEMAND', # N flux required to support initial GPP	
                            'STORVEGC', # stored vegetation carbon, excluding cpool	
                            'STORVEGN', # stored vegetation nitrogen, excluding cpool	
                            #'TOTCOLN', # total column nitrogen
                            #'TOTCOLC', # total column carbon
                            'TOTECOSYSC', # total ecosystem carbon (veg + soil)
                            'TOTECOSYSN', # total ecosystem nitrogen (veg + soil)
                            #'TOTPFTC', # total PFT level carbon
                            #'TOTPFTN', # total PFT level nitrogen
                            'TOTSOMC', # Total soil organic matter carbon
                            'TOTSOMN', # Total soil organic matter nitrogen
                            'TOTVEGC', # total vegetation carbon
                            'TOTVEGN', # Total vegetaiton nitrogen

                        ## Vegetation function
                            'TLAI', # Total leaf-area-index
                            'TSAI', # total stem-area-index
                            #'BTRAN', # beta factor transpiration down regulation
                            'BTRANMN', # daily minimum beta transpiration factor
                            'GSSHA', # stomatal conductance (shaded leaf)
                            'GSSUN', # stomatal conductance (sunlit leaf)
                        
                        ## Radiation
			                'FSM', # Snow melt heat flux
                            'Rnet', # net radiation
                            'SWdown', # Shortwave radiation downwards incoming
                            'TBOT', # atmospheric air temperature
                            'SWup', #Shortwave radiation upwards outgoing
                            'Qh', # Sensible heat
                            'LWdown', # Longwave radiation downwards incoming
                            'LWup', # Longwave radiation upwards outgoing
                            'Qstor', # storage heat flux (incl. snowmelt)
                            'ALBD', # Surface albedo (visible and near infra red bands)
                            'ALBGRD',  # Ground albedo
                            'ALBI', # Surface albido (indirect)
                            'ALBGRI', # Ground albido (indirect)
                            'FGR', # heat flux into soil
                            
                        
                        ## Evaporation
                            'Qle', # Total evaporation
			                'FCEV', # Canopy evaporation
                            'FCTR', # Canopy transpiration
                            'FGEV', # Canopy evaporation


                        ## Snow
                            'FSNO', # fraction snow cover
                            'SNOWDP', # snow height
                            'SNOWICE', # snow ice
                            'SNOTTOPL', # snow temperature top layer
                            'SNOWLIQ', # snow liquid water
                            'QICE', # Ice growth, melt


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
                            'VPD', # Vapour pressure deficit
                            'TWS', # total water storage
                            'ZWT', # table water depth
                            'SOILPSI', # soil water potential
                            'VEGWP', # vegetation water potential
                            'watfc', # water field capacity
                            'SMP', # soil matric potential

                        ],
    'hist_vars_pft': [
                        ### Carbon and nitrogen
                            #'DISPVEGC', # displayed veg carbon, excluding storage and cpool
                            #'DISPVEGN', # displayed vegetation nitrogen
                            #'DOWNREG',  # fractional reduction in GPP due to N limitation
                            #'ER', # Ecosystem respiration
                            'GPP', # Gross primary production
                            #'GROSS_NMIN', # gross rate of N mineralization
                            #'LEAFC', # leaf carbon
                            #'LEAFN', # leaf nitrogen
                            #'LNC', # leaf N concentration
                            #'NBP', # net biome production, includes fire, landuse, and harvest flux, positive for sink	
                            #'NDEP_TO_SMINN',  # atmospheric N deposition to soil mineral N
                            #'NEE', # net ecosystem exchange
			                #'NEP', # Net ecosystem production
                            #'NPP', # Net Primary Production
                            #'PLANT_NDEMAND', # N flux required to support initial GPP	
                            #'STORVEGC', # stored vegetation carbon, excluding cpool	
                            #'STORVEGN', # stored vegetation nitrogen, excluding cpool	
                            #'TOTCOLN', # total column nitrogen
                            #'TOTCOLC', # total column carbon
                            #'TOTECOSYSC', # total ecosystem carbon (veg + soil)
                            #'TOTECOSYSN', # total ecosystem nitrogen (veg + soil)
                            #'TOTPFTC', # total PFT level carbon
                            #'TOTPFTN', # total PFT level nitrogen
                            #'TOTSOMC', # Total soil organic matter carbon
                            #'TOTSOMN', # Total soil organic matter nitrogen
                            #'TOTVEGC', # total vegetation carbon
                            #'TOTVEGN', # Total vegetaiton nitrogen

                        ## Vegetation function
                            #'LAISHA', # Shaded leaf leaf-area-index
                            #'LAISUN', # Sunlit leaf leaf-area-index
                            #'SAISHA', # shaded leaf leaf-area-index
                            #'SAISUN', # sunlit leaf leaf-area-index
                            #'BTRAN', # beta factor transpiration down regulation
                            'BTRANMN', # daily minimum beta transpiration factor
                            'GSSHA', # stomatal conductance (shaded leaf)
                            'GSSUN', # stomatal conductance (sunlit leaf)
                        
                        ## Radiation
			                #'FSM', # Snow melt heat flux
                            #'Rnet', # net radiation
                            #'SWdown', # Shortwave radiation downwards incoming
                            #'TBOT', # atmospheric air temperature
                            #'SWup', #Shortwave radiation upwards outgoing
                            #'Qh', # Sensible heat
                            #'LWdown', # Longwave radiation downwards incoming
                            #'LWup', # Longwave radiation upwards outgoing
                            #'Qstor', # storage heat flux (incl. snowmelt)
                            #'ALBD', # Surface albedo (visible and near infra red bands)
                            #'ALBGRD',  # Ground albedo
                            #'ALBI', # Surface albido (indirect)
                            #'ALBGRI', # Ground albido (indirect)
                            #'FGR', # heat flux into soil
                            
                        
                        ## Evaporation
                            'Qle', # Total evaporation
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
                            #'SNOW',  # atmospheric snow
                            #'RAIN', # atmospheric rain
                            #'QOVER', # Surface runoff
                            #'QIRRIG', # Irrigation
                            #'QINFL', # Infiltration
                            #'QINTR', # Interception
                            #'QFLX_EVAP_VEG', # Vegetation evaporation
                            #'QFLX_EVAP_GRND', # Ground surface evaporation
                            #'QFLX_EVAP_TOT', # Evapo transpiration
                            #'H2OCAN', # Intercepted water
                            #'QDRAI', # subsurface drainage
			                #'H2OSNO', # snow depth (liq. water)
                            #'H2OSOI', # volumentric soil water
                            #'RH', # relative humidity
                            #'TWS', # total water storage
                            #'ZWT', # table water depth
                            #'SOILPSI', # soil water potential
                            #'VEGWP', # vegetation water potential
                            #'watfc', # water field capacity
                            #'SMP', # soil matric potential
                    ],

    'year_start': 1995,
    'month_start': 1,

    'year_end': 2018,
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

    'dir_init': '/p/scratch/cjibg31/jibg3105/CESMDataRoot/InputData/lnd/clm2/initdata_map/FINAL/',
    'file_init': 'CLM5EU3_BGC_west_JR2.clm2.r.3204-01-01-00000.nc',

    'dir_forcing': '/p/scratch/cjibg31/jibg3105/CESMDataRoot/InputData/Forcings/CLM5EU3_west/',

    'vars_forcing' :    {  
                            'swdn': 'FSDS',
                            'precn': 'PRECTmms',
                            'tbot': 'TBOT',
                            'wind': 'WIND',
                            'pbot': 'PSRF',
                            'rh': 'RH'
                        },

    'time_resolution_forcing_hours': 6,

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

CLM5EU3_BGC_007_east = {

    'dir_script': '/p/project/cjibg31/jibg3105/clm5.0/cime/scripts',
    'name': 'CLM5EU3_BGC_east_0007_JW',
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
    'hist_vars_grid':   [
                        ### Carbon and nitrogen
                            'DISPVEGC', # displayed veg carbon, excluding storage and cpool
                            'DISPVEGN', # displayed vegetation nitrogen
                            'DOWNREG',  # fractional reduction in GPP due to N limitation
                            'ER', # Ecosystem respiration
                            'GPP', # Gross primary production
                            'GROSS_NMIN', # gross rate of N mineralization
                            'LEAFC', # leaf carbon
                            'LEAFN', # leaf nitrogen
                            'LNC', # leaf N concentration
                            'NBP', # net biome production, includes fire, landuse, and harvest flux, positive for sink	
                            'NDEP_TO_SMINN', # atmospheric N deposition to soil mineral N
                            'NEE', # net ecosystem exchange
			                'NEP', # Net ecosystem production
                            'NPP', # Net Primary Production
                            'PLANT_NDEMAND', # N flux required to support initial GPP	
                            'STORVEGC', # stored vegetation carbon, excluding cpool	
                            'STORVEGN', # stored vegetation nitrogen, excluding cpool	
                            #'TOTCOLN', # total column nitrogen
                            #'TOTCOLC', # total column carbon
                            'TOTECOSYSC', # total ecosystem carbon (veg + soil)
                            'TOTECOSYSN', # total ecosystem nitrogen (veg + soil)
                            #'TOTPFTC', # total PFT level carbon
                            #'TOTPFTN', # total PFT level nitrogen
                            'TOTSOMC', # Total soil organic matter carbon
                            'TOTSOMN', # Total soil organic matter nitrogen
                            'TOTVEGC', # total vegetation carbon
                            'TOTVEGN', # Total vegetaiton nitrogen

                        ## Vegetation function
                            'TLAI', # Total leaf-area-index
                            'TSAI', # total stem-area-index
                            #'BTRAN', # beta factor transpiration down regulation
                            'BTRANMN', # daily minimum beta transpiration factor
                            'GSSHA', # stomatal conductance (shaded leaf)
                            'GSSUN', # stomatal conductance (sunlit leaf)
                        
                        ## Radiation
			                'FSM', # Snow melt heat flux
                            'Rnet', # net radiation
                            'SWdown', # Shortwave radiation downwards incoming
                            'TBOT', # atmospheric air temperature
                            'SWup', #Shortwave radiation upwards outgoing
                            'Qh', # Sensible heat
                            'LWdown', # Longwave radiation downwards incoming
                            'LWup', # Longwave radiation upwards outgoing
                            'Qstor', # storage heat flux (incl. snowmelt)
                            'ALBD', # Surface albedo (visible and near infra red bands)
                            'ALBGRD',  # Ground albedo
                            'ALBI', # Surface albido (indirect)
                            'ALBGRI', # Ground albido (indirect)
                            'FGR', # heat flux into soil
                            
                        
                        ## Evaporation
                            'Qle', # Total evaporation
			                'FCEV', # Canopy evaporation
                            'FCTR', # Canopy transpiration
                            'FGEV', # Canopy evaporation


                        ## Snow
                            'FSNO', # fraction snow cover
                            'SNOWDP', # snow height
                            'SNOWICE', # snow ice
                            'SNOTTOPL', # snow temperature top layer
                            'SNOWLIQ', # snow liquid water
                            'QICE', # Ice growth, melt


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
                            'VPD', # Vapour pressure deficit
                            'TWS', # total water storage
                            'ZWT', # table water depth
                            'SOILPSI', # soil water potential
                            'VEGWP', # vegetation water potential
                            'watfc', # water field capacity
                            'SMP', # soil matric potential

                        ],
    'hist_vars_pft': [
                        ### Carbon and nitrogen
                            #'DISPVEGC', # displayed veg carbon, excluding storage and cpool
                            #'DISPVEGN', # displayed vegetation nitrogen
                            #'DOWNREG',  # fractional reduction in GPP due to N limitation
                            #'ER', # Ecosystem respiration
                            'GPP', # Gross primary production
                            #'GROSS_NMIN', # gross rate of N mineralization
                            #'LEAFC', # leaf carbon
                            #'LEAFN', # leaf nitrogen
                            #'LNC', # leaf N concentration
                            #'NBP', # net biome production, includes fire, landuse, and harvest flux, positive for sink	
                            #'NDEP_TO_SMINN',  # atmospheric N deposition to soil mineral N
                            #'NEE', # net ecosystem exchange
			                #'NEP', # Net ecosystem production
                            #'NPP', # Net Primary Production
                            #'PLANT_NDEMAND', # N flux required to support initial GPP	
                            #'STORVEGC', # stored vegetation carbon, excluding cpool	
                            #'STORVEGN', # stored vegetation nitrogen, excluding cpool	
                            #'TOTCOLN', # total column nitrogen
                            #'TOTCOLC', # total column carbon
                            #'TOTECOSYSC', # total ecosystem carbon (veg + soil)
                            #'TOTECOSYSN', # total ecosystem nitrogen (veg + soil)
                            #'TOTPFTC', # total PFT level carbon
                            #'TOTPFTN', # total PFT level nitrogen
                            #'TOTSOMC', # Total soil organic matter carbon
                            #'TOTSOMN', # Total soil organic matter nitrogen
                            #'TOTVEGC', # total vegetation carbon
                            #'TOTVEGN', # Total vegetaiton nitrogen

                        ## Vegetation function
                            #'LAISHA', # Shaded leaf leaf-area-index
                            #'LAISUN', # Sunlit leaf leaf-area-index
                            #'SAISHA', # shaded leaf leaf-area-index
                            #'SAISUN', # sunlit leaf leaf-area-index
                            #'BTRAN', # beta factor transpiration down regulation
                            'BTRANMN', # daily minimum beta transpiration factor
                            'GSSHA', # stomatal conductance (shaded leaf)
                            'GSSUN', # stomatal conductance (sunlit leaf)
                        
                        ## Radiation
			                #'FSM', # Snow melt heat flux
                            #'Rnet', # net radiation
                            #'SWdown', # Shortwave radiation downwards incoming
                            #'TBOT', # atmospheric air temperature
                            #'SWup', #Shortwave radiation upwards outgoing
                            #'Qh', # Sensible heat
                            #'LWdown', # Longwave radiation downwards incoming
                            #'LWup', # Longwave radiation upwards outgoing
                            #'Qstor', # storage heat flux (incl. snowmelt)
                            #'ALBD', # Surface albedo (visible and near infra red bands)
                            #'ALBGRD',  # Ground albedo
                            #'ALBI', # Surface albido (indirect)
                            #'ALBGRI', # Ground albido (indirect)
                            #'FGR', # heat flux into soil
                            
                        
                        ## Evaporation
                            'Qle', # Total evaporation
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
                            #'SNOW',  # atmospheric snow
                            #'RAIN', # atmospheric rain
                            #'QOVER', # Surface runoff
                            #'QIRRIG', # Irrigation
                            #'QINFL', # Infiltration
                            #'QINTR', # Interception
                            #'QFLX_EVAP_VEG', # Vegetation evaporation
                            #'QFLX_EVAP_GRND', # Ground surface evaporation
                            #'QFLX_EVAP_TOT', # Evapo transpiration
                            #'H2OCAN', # Intercepted water
                            #'QDRAI', # subsurface drainage
			                #'H2OSNO', # snow depth (liq. water)
                            #'H2OSOI', # volumentric soil water
                            #'RH', # relative humidity
                            #'TWS', # total water storage
                            #'ZWT', # table water depth
                            #'SOILPSI', # soil water potential
                            #'VEGWP', # vegetation water potential
                            #'watfc', # water field capacity
                            #'SMP', # soil matric potential
                    ],

    'year_start': 1995,
    'month_start': 1,

    'year_end': 2018,
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

    'dir_init': '/p/scratch/cjibg31/jibg3105/CESMDataRoot/InputData/lnd/clm2/initdata_map/FINAL/',
    'file_init': 'CLM5EU3_BGC_east_JR4.clm2.r.3618-01-01-00000.nc',

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

    'methane_model': True,

    'coldstart': False,

    'job_archive': False,

    'AD_spin_up': False,

    'continue_run': False

}