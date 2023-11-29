

# Notes
# None and none and nones and default values correspond with here?
# Spinup functionality

from dataclasses import dataclass, field

@dataclass
class case:

    """
    I hope to be a generic class for most CLM5 user cases.

    Infos:
    https://www2.cesm.ucar.edu/models/ccsm4.0/clm/models/lnd/clm/doc/UsersGuide/x1327.html
    https://docs.cesm.ucar.edu/models/cesm2/settings/current/drv_input_cesm.html
    https://docs.cesm.ucar.edu/models/cesm2/settings/current/clm5_0_nml.html
    https://docs.cesm.ucar.edu/models/cesm2/settings/current/datm_input.html

    Maybe in future: different datm interpolation methods?
    https://escomp.github.io/ctsm-docs/versions/release-clm5.0/html/users_guide/setting-up-and-running-a-case/customizing-the-datm-namelist.html

    To do:
    - Custom forcings switch: consider the stated stream files in the user datm namelist

    """

    dir_script: str 
    name: str
    compset: str
    n_cpu: int
    year_start: int
    year_end: int
    year_start_forcing: int
    year_end_forcing: int
    dir_domain_lnd: str
    file_domain_lnd: str
    dir_surf: str
    file_surf: str
    months_per_wallclock: int
    time_resolution_forcing_hours: int

    ncpl: int                   = 24
    wallclock: str              = '24:00:00'
    
    mode_datm: str              = 'CLMCRUNCEPv7'
    hist_vars_grid: list        = field(default_factory = list)
    hist_vars_pft: list         = field(default_factory = list)
    hist_frq_grid: int          = -24
    hist_flt_grid: int          = 365
    hist_frq_pft: int           = -24
    hist_flt_pft: int           = 365

    month_start: int            = 1
    month_end: int              = 12

    month_start_forcing: int    = 1
    month_end_forcing: int      = 12

    custom_forcings: bool       = True


    dir_domain_atm: None | str  = None
    file_domain_atm: None | str = None

    dir_init: str | None        = None
    file_init: str | None       = None

    dir_forcing: str | None     = None

    vars_forcing: dict | None   = None

    mode_co2: None | str        = None 

    type_co2: str               = 'constant' 
    ppmv_co2: float             = 379.0
    
    series_co2: str             = None

    coldstart: bool             = False

    job_archive: bool           = False

    AD_spin_up: bool            = False

    continue_run: bool          = False


    def create(self):
        
        """
        To create a case directory.

        """
        import os
        import subprocess
        
        if os.path.isdir(f'{self.dir_script}/{self.name}'): 
            
            print('\nCase directory already exists. \n')

            return

        print('\nCreate case...\n')

        subprocess.call([f'{self.dir_script}/create_newcase', 
                         '--case', self.name, 
                         '--res', 'CLM_USRDAT' , 
                         '--compset', self.compset, 
                         '--run-unsupported'], cwd = self.dir_script)
        
        print('\nCase created.\n')
    

    def setup(self, clean: bool = False):
        
        """
        To setup the case and create respective generic namelist files.

        """

        import os
        import subprocess

        dir_setup           = f'{self.dir_script}/{self.name}'

        if clean: subprocess.call([f'{dir_setup}/case.setup', 
                                   '--clean'], cwd = dir_setup)
        
        if os.path.isdir(f'{dir_setup}/CaseDocs/'): 
            
            print('Case is already set-up. Clean?')
            
            return

        print('\nSet-up case ...\n')

        subprocess.call([f'{dir_setup}/xmlchange',
                         f'NTASKS={self.n_cpu}'], cwd = dir_setup)
        
        subprocess.call(f'{dir_setup}/case.setup', cwd = dir_setup)

        print('\nCase set-up.\n')
    
    
    
    def config(self):
     
        """
        Change the config files in the case directory.
        We use the xmlchange functionality.

        """

        print('\nAdjust case configuration...\n')

        import subprocess
        import numpy as np

        dir_setup           = f'{self.dir_script}/{self.name}'

        n_months            = 12 * (self.year_end - self.year_start) - (24 - (self.month_start + self.month_end))

        resubmit            = (np.ceil(n_months / self.months_per_wallclock) - 1).astype(int)

        keys_config         = { 'ATM_DOMAIN_PATH': self.dir_domain_atm,
                                'LND_DOMAIN_PATH': self.dir_domain_lnd,
                                'ATM_DOMAIN_FILE': self.file_domain_atm,
                                'LND_DOMAIN_FILE': self.file_domain_lnd,
                                'DATM_MODE': self.mode_datm,
                                'DATM_CLMNCEP_YR_ALIGN': self.year_start_forcing,
                                'DATM_CLMNCEP_YR_START': self.year_start_forcing,
                                'DATM_CLMNCEP_YR_END': self.year_end_forcing,
                                'RUN_STARTDATE': f'{self.year_start:04d}-{self.month_start:02d}-01',
                                'STOP_OPTION': 'nmonths',
                                'STOP_N': self.months_per_wallclock,
                                'STOP_DATE': -1,
                                'JOB_WALLCLOCK_TIME': self.wallclock,
                                'CLM_ACCELERATED_SPINUP': self.AD_spin_up,
                                'RESUBMIT': resubmit,
                                'CLM_FORCE_COLDSTART': self.coldstart,
                                'ATM_NCPL': self.ncpl,
                                'LND_NCPL': self.ncpl,
                                'DOUT_S': self.job_archive,
                                'CCSM_BGC': self.mode_co2,
                                'CLM_CO2_TYPE': self.type_co2,
                                'CCSM_CO2_PPMV': self.ppmv_co2,
                                'DATM_CO2_TSERIES': self.series_co2,
                                'CONTINUE_RUN': self.continue_run,
                                }
        
        for k, v in keys_config.items():
            
            print(f'Set {k}...')

            if v is None: v = 'none'
            if k in ('CLM_FORCE_COLDSTART', 'CLM_ACCELERATED_SPINUP') and v is False: v = 'off'
            if k in ('CLM_FORCE_COLDSTART', 'CLM_ACCELERATED_SPINUP') and v is True: v = 'on'
            if k in ('DOUT_S', 'CONTINUE_RUN') and v is False: v = 'FALSE'
            if k in ('DOUT_S', 'CONTINUE_RUN') and v is True: v = 'TRUE'

            subprocess.call([f'{dir_setup}/xmlchange',
                         f'{k}={v}'], cwd = dir_setup)
            
        print('\nCase configuration adjusted.\n')


    def namelists(self):

        """
        Change the user namelist files in the case directory.
        We use blueprint files from this repository, change them,
        and copy them to the case directory.

        """

        print('\nCreate case namelists...\n')

        dir_setup           = f'{self.dir_script}/{self.name}'
        
        file_init           = f"finidat = '{self.dir_init}/{self.file_init}'" if self.file_init is not None else ''

        hist_vars_grid      = "'" + "', '".join(self.hist_vars_grid) + "'"

        dt_limit            = (24 + self.time_resolution_forcing_hours) / self.time_resolution_forcing_hours

        if self.hist_vars_pft:

            hist_vars_pft_0 = f'hist_dov2xy(2) = .false.'
            hist_vars_pft_1 = f"hist_type1d_pertape(2) = 'PFTS'"
            hist_vars_pft_2 = f'hist_nhtfrq(2) = {self.hist_frq_pft}'
            hist_vars_pft_3 = f'nhist_mfilt(2) = {self.hist_flt_pft}'
            hist_vars_pft_4 = "'" + "', '".join(self.hist_vars_pft) + "'"

            hist_pft_str    = '\n'.join([hist_vars_pft_0, 
                                        hist_vars_pft_1,
                                        hist_vars_pft_2,
                                        hist_vars_pft_3,
                                        hist_vars_pft_4,])
        else:
            
            hist_pft_str    = ''


        keys_namelist_clm   = { 'file_surf': f"'{self.dir_surf}/{self.file_surf}'",
                                'file_init': file_init,
                                'hist_frq': self.hist_frq_grid,
                                'hist_flt': self.hist_flt_grid,
                                'hist_vars_grid': hist_vars_grid,
                                'hist_vars_pft': hist_pft_str,
                                }
        
        keys_namelist_datm  = { 'year_start': self.year_start_forcing,
                                'year_end': self.year_end_forcing,
                                'dt_limit': dt_limit,
                                }

        self.search_replace('config_files/user_nl/', 'user_nl_clm', keys_namelist_clm, dir_setup)
        self.search_replace('config_files/user_nl/', 'user_nl_datm', keys_namelist_datm, dir_setup)


        print('\nNamelists created and copied.\n')
    

    def search_replace(self, path_in, name_file, search_replace_dict, path_out):
        
        with open(f'{path_in}/{name_file}', 'r') as file:
        
            content         = file.read()

            for k, v in search_replace_dict.items():

                content     = content.replace(k, str(v))

        with open(f'{path_out}/{name_file}', 'w') as file:

            file.write(content)


    def streams(self):

        """
        Create and adjust the datm stream files files.
        This is to run CLM5 with your own forcings.
        We use the blueprint files in this repository, change them,
        and copy them to the case directory.

        """

        if not self.custom_forcings: print('\nNo stream files necessary.\n'); return
        
        print('\nCreate case stream files...\n')

        import subprocess

        dir_setup           = f'{self.dir_script}/{self.name}'

        year_files          = [f'{y}-{m:02d}.nc' for y in range(self.year_start_forcing, self.year_end_forcing + 1) for m in range(1,13)]

        keys_solar          = {k: v for k, v in self.vars_forcing.items() if k == 'swdn'}
        keys_precn          = {k: v for k, v in self.vars_forcing.items() if k == 'precn'}
        keys_tpqw           = {k: v for k, v in self.vars_forcing.items() if k not in ['swdn', 'precn']}

        str_solar           = '\n'.join([f'{v}\t{k}' for k, v in keys_solar.items()])
        str_precn           = '\n'.join([f'{v}\t{k}' for k, v in keys_precn.items()])
        str_tpqw            = '\n'.join([f'{v}\t{k}' for k, v in keys_tpqw.items()])

        keys_streams_solar  = { 'dir_domain': self.dir_domain_atm,
                                'file_domain': self.file_domain_atm, 
                                'dir_forcing': self.dir_forcing,
                                'year_files': '\n'.join(year_files),
                                'vars_solar': str_solar,
                               }
        
        keys_streams_precn  = { 'dir_domain': self.dir_domain_atm,
                                'file_domain': self.file_domain_atm, 
                                'dir_forcing': self.dir_forcing,
                                'year_files': '\n'.join(year_files),
                                'vars_precn': str_precn,
                               }
        
        keys_streams_tpqw   = { 'dir_domain': self.dir_domain_atm,
                                'file_domain': self.file_domain_atm, 
                                'dir_forcing': self.dir_forcing,
                                'year_files': '\n'.join(year_files),
                                'vars_tpqw': str_tpqw,
                               }
        
        self.search_replace('config_files/user_datm/', 'user_datm.streams.txt.CLMCRUNCEPv7.Precip', keys_streams_precn, dir_setup)
        self.search_replace('config_files/user_datm/', 'user_datm.streams.txt.CLMCRUNCEPv7.Solar', keys_streams_solar, dir_setup)
        self.search_replace('config_files/user_datm/', 'user_datm.streams.txt.CLMCRUNCEPv7.TPQW', keys_streams_tpqw, dir_setup)

        subprocess.call(f'{dir_setup}/preview_namelists', cwd = dir_setup)
        subprocess.call(f'cp user_datm.streams.* Buildconf/datmconf/', shell = True, cwd = dir_setup)

        print('\nCase stream files created.\n')

        if self.vars_forcing is None: return

        keys_solar          = {k: v for k, v in self.vars_forcing.items() if k == 'swdn'}
        keys_precn          = {k: v for k, v in self.vars_forcing.items() if k == 'precn'}
        keys_tpqw           = {k: v for k, v in self.vars_forcing.items() if k not in ['swdn', 'precn']}



    def build(self, clean: bool = False):

        """
        Build the model case with the case.build script.

        """

        import subprocess
        import mmap

        dir_setup           = f'{self.dir_script}/{self.name}'

        with open(f'{dir_setup}/CaseStatus', 'r') as file, \
            mmap.mmap(file.fileno(), 0, access = mmap.ACCESS_READ) as s:
            
            if s.find(b'case.build success') != -1:

                print('Case was already built. Clean?')
                
                return

        if clean:

            print('Cleaning case build...')

            subprocess.call([f'{dir_setup}/case.build', '--clean-all'], cwd = dir_setup)

            print('Case build cleaned.')

        print('Build case...')

        subprocess.call([f'{dir_setup}/case.build'], cwd = dir_setup)

        print('Case built.')


    def submit(self):

        """
        Submit your case for simulation with the case.submit script.
        
        """

        import subprocess

        dir_setup           = f'{self.dir_script}/{self.name}'

        print('\nCase submit...\n')

        subprocess.call([f'{dir_setup}/case.submit', '--resubmit-immediate'], cwd = dir_setup)

        print('\nCase submitted. All done!\n')

        