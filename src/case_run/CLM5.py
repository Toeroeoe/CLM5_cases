

# Notes
# None and none and nones and default values correspond with here?
# Spinup functionality

from dataclasses import dataclass, field
from pathlib import Path
import os
import subprocess
import shutil
import numpy as np
import pandas as pd
import mmap


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
    - Test / adapt for cases with default forcings (no stream files)
    - Test / adapt for single-point cases
    -
    """
    computer: str
    partition: str
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
    dir_output: str

    ncpl: int = 24
    wallclock: str = '24:00:00'
    
    mode_datm: str = 'CLMCRUNCEPv7'
    hist_vars_grid: list = field(default_factory = list)
    hist_vars_pft: list = field(default_factory = list)
    hist_frq_grid: int = -24
    hist_flt_grid: int = 365
    hist_frq_pft: int = -24
    hist_flt_pft: int = 365

    month_start: int = 1
    day_start: int = 1
    month_end: int = 12
    day_end: int = 31

    month_start_forcing: int = 1
    month_end_forcing: int = 12

    dtlimit: float | None = None

    custom_forcings: bool = True

    dir_domain_atm: None | str = None
    file_domain_atm: None | str = None

    domain_atm_vars: None | dict[str, str] = None

    dir_domain_co2: None | str = None
    file_domain_co2: None | str = None

    domain_co2_vars: None | dict[str, str] = None

    dir_init: str | None = None
    file_init: str | None = None

    init_interpolation: bool = False

    dir_forcing: str | None = None

    vars_forcing: dict | None = None

    mode_co2: None | str = None 
    
    dir_co2: None | str = None
    file_co2: None | str = None

    vars_co2: None | dict[str, str] = None

    type_co2: str = 'constant' 
    ppmv_co2: float = 379.0

    methane_model: bool = True
    
    series_co2: str | None = None

    coldstart: bool = False

    job_archive: bool = False

    AD_spin_up: bool = False

    continue_run: bool = False


    def create(self, delete: bool = False):
        
        """
        To create a case directory.

        """

        if delete: 

            print(f'\nDelete {self.name} existing case and output directory. \n')

            shutil.rmtree(f'{self.dir_script}/{self.name}/', ignore_errors = True)
            shutil.rmtree(f'{self.dir_output}/{self.name}/', ignore_errors = True)

        
        if os.path.isdir(f'{self.dir_script}/{self.name}'): 
            
            print(f'\n{self.name} case directory already exists. \n')

            return

        print('\nCreate case...\n')

        print('Create case command:',
              f'{self.dir_script}/create_newcase', 
              '--case', f'{self.name}_{self.computer}', 
              '--res', 'CLM_USRDAT' , 
              '--compset', self.compset, 
              '--run-unsupported',
              '\n')

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

        dir_setup = f'{self.dir_script}/{self.name}'

        if os.path.isdir(f'{dir_setup}/CaseDocs/'): 
            
            print('Case is already set-up. Clean?')
            
            if not clean: return


        if clean: print('Clean...'); subprocess.call([f'{dir_setup}/case.setup', 
                                   '--clean'], cwd = dir_setup)


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

        dir_setup = f'{self.dir_script}/{self.name}'



        n_months = (np.datetime64(f'{self.year_end}-{self.month_end:>02}')- \
                    np.datetime64(f'{self.year_start}-{self.month_start:>02}')) / np.timedelta64(1, 'M')
        
        print(f'Number of months to simulate: {n_months:.0f}')

        resubmit = (np.ceil(n_months / self.months_per_wallclock) - 1).astype(int)

        keys_config = {'ATM_DOMAIN_PATH': self.dir_domain_lnd,
                       'LND_DOMAIN_PATH': self.dir_domain_lnd,
                       'ATM_DOMAIN_FILE': self.file_domain_lnd,
                       'LND_DOMAIN_FILE': self.file_domain_lnd,
                       'DATM_MODE': self.mode_datm,
                       'DATM_CLMNCEP_YR_ALIGN': self.year_start_forcing,
                       'DATM_CLMNCEP_YR_START': self.year_start_forcing,
                       'DATM_CLMNCEP_YR_END': self.year_end_forcing,
                       'RUN_STARTDATE': f'{self.year_start:04d}-{self.month_start:02d}-{self.day_start:02d}',
                       'STOP_DATE': -1,
                       'STOP_OPTION': 'nmonths',
                       'STOP_N': self.months_per_wallclock,
                       'STOP_DATE': f'{self.year_end:04d}{self.month_end:02d}{self.day_end:02d}',
                       'REST_OPTION': 'nmonths',
                       'REST_N': 12,
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
                       'JOB_QUEUE': self.partition,}
        
        for k, v in keys_config.items():
            

            if v is None: v = 'none'
            if k in ('CLM_FORCE_COLDSTART', 'CLM_ACCELERATED_SPINUP') and v is False: v = 'off'
            if k in ('CLM_FORCE_COLDSTART', 'CLM_ACCELERATED_SPINUP') and v is True: v = 'on'
            if k in ('DOUT_S', 'CONTINUE_RUN') and v is False: v = 'FALSE'
            if k in ('DOUT_S', 'CONTINUE_RUN') and v is True: v = 'TRUE'

            print(f'Set {k} to: {v}...')

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

        dir_setup = f'{self.dir_script}/{self.name}'
        
        file_init = f"finidat = '{self.dir_init}/{self.file_init}'" if self.file_init is not None else ''

        hist_vars_grid = "'" + "', '".join(self.hist_vars_grid) + "'"

        dt_limit = self.dtlimit if self.dtlimit is not None else ((self.ncpl + self.time_resolution_forcing_hours) / self.time_resolution_forcing_hours) + 1

        if self.hist_vars_pft:
            hist_vars_pft_0 = "'" + "', '".join(self.hist_vars_pft) + "'"
            hist_vars_pft_1 = f'hist_dov2xy(2) = .false.'
            hist_vars_pft_2 = f"hist_type1d_pertape(2) = 'PFTS'"
            hist_vars_pft_3 = f'hist_nhtfrq(2) = {self.hist_frq_pft}'
            hist_vars_pft_4 = f'hist_mfilt(2) = {self.hist_flt_pft}'

            hist_pft_str = 'hist_fincl2 = ' + \
                                '\n'.join([hist_vars_pft_0, 
                                           hist_vars_pft_1,
                                           hist_vars_pft_2,
                                           hist_vars_pft_3,
                                           hist_vars_pft_4,])
        else:
            
            hist_pft_str = ''
                    
        methane_str = '' if self.methane_model else 'use_lch4 = .false.'

        init_interpolation_str = 'use_init_interp = .true.' if self.init_interpolation else ''

        keys_namelist_clm = {'file_surf': f"'{self.dir_surf}/{self.file_surf}'",
                             'file_init': file_init,
                             'hist_frq': self.hist_frq_grid,
                             'hist_flt': self.hist_flt_grid,
                             'hist_vars_grid': hist_vars_grid,
                             'hist_vars_pft': hist_pft_str,
                             'methane_model': methane_str,
                             'init_interpolation': init_interpolation_str}
        
        keys_namelist_datm  = {'year_start': self.year_start_forcing,
                               'year_end': self.year_end_forcing,
                               'dt_limit': dt_limit}

        self.search_replace(f'{Path(__file__).resolve().parent}/config_files/user_nl/', 
                            'user_nl_clm', 
                            keys_namelist_clm, 
                            dir_setup)

        self.search_replace(f'{Path(__file__).resolve().parent}/config_files/user_nl/', 
                            'user_nl_datm', 
                            keys_namelist_datm, 
                            dir_setup)
        
        subprocess.call(f'cp user_nl_cpl {dir_setup}', 
                        shell = True, 
                        cwd = f'{Path(__file__).resolve().parent}/config_files/user_nl/')
        
        subprocess.call(f'cp user_nl_mosart {dir_setup}', 
                        shell = True, 
                        cwd = f'{Path(__file__).resolve().parent}/config_files/user_nl/')


        print('\nNamelists created and copied.\n')
    

    def search_replace(self, path_in, name_file, search_replace_dict, path_out):
        
        with open(f'{path_in}/{name_file}', 'r') as file:
        
            content = file.read()

            for k, v in search_replace_dict.items():

                content = content.replace(k, str(v))

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

        dir_setup = f'{self.dir_script}/{self.name}'

        year_files = []
        
        for iy, y in enumerate(range(self.year_start_forcing, self.year_end_forcing + 1)):

            m0 = self.month_start if iy == 0 else 1
            m1 = self.month_end + 1 if y == self.year_end_forcing else 13  

            for m in range (m0, m1):

                year_files.append(f'\t\t{y}-{m:02d}.nc')

        if self.dir_co2 is None: self.dir_co2 = '/p/scratch/cjibg31/jibg3105/CESMDataRoot/InputData/atm/datm7/CO2/'
        if self.dir_domain_co2 is None: self.dir_domain_co2 = '/p/scratch/cjibg31/jibg3105/CESMDataRoot/InputData/atm/datm7/CO2/'
        if self.file_domain_co2 is None: self.file_domain_co2 = 'fco2_datm_global_simyr_1750-2014_CMIP6_c180929.nc'
        if self.file_co2 is None: self.file_co2 = 'fco2_datm_global_simyr_1750-2014_CMIP6_c180929.nc'

        if self.vars_forcing is None: self.vars_forcing = {}
        if self.domain_atm_vars is None : self.domain_atm_vars = {}
        if self.domain_co2_vars is None : self.domain_co2_vars = {'time': 'time',
                                                                  'lon': 'lonc',
                                                                  'lat': 'latc',
                                                                  'area': 'area',
                                                                  'mask': 'mask'}
        if self.vars_co2 is None: self.vars_co2 = {'co2diag': 'CO2'}

        keys_solar = {k: v for k, v in self.vars_forcing.items() if k == 'swdn'}
        keys_precn = {k: v for k, v in self.vars_forcing.items() if k == 'precn'}
        keys_tpqw = {k: v for k, v in self.vars_forcing.items() if k not in ['swdn', 'precn']}

        str_solar = '\n'.join([f'\t\t{v: <10}{k}' for k, v in keys_solar.items()])
        str_precn = '\n'.join([f'\t\t{v: <10}{k}' for k, v in keys_precn.items()])
        str_tpqw = '\n'.join([f'\t\t{v: <10}{k}' for k, v in keys_tpqw.items()])
        str_co2 = '\n'.join([f'\t\t{v: <10}{k}' for k, v in self.vars_co2.items()])

        str_atm_domain_vars = '\n'.join([f'\t\t{v: <10}{k}' for k, v in self.domain_atm_vars.items()])
        str_co2_domain_vars = '\n'.join([f'\t\t{v: <10}{k}' for k, v in self.domain_co2_vars.items()])

        keys_streams_solar = {'atm_domain_vars': str_atm_domain_vars,
                              'dir_domain': self.dir_domain_atm,
                              'file_domain': self.file_domain_atm, 
                              'dir_forcing': self.dir_forcing,
                              'year_files': '\n'.join(year_files),
                              'vars_solar': str_solar}
        
        keys_streams_precn = {'atm_domain_vars': str_atm_domain_vars,
                              'dir_domain': self.dir_domain_atm,
                              'file_domain': self.file_domain_atm, 
                              'dir_forcing': self.dir_forcing,
                              'year_files': '\n'.join(year_files),
                              'vars_precn': str_precn}
        
        keys_streams_tpqw = {'atm_domain_vars': str_atm_domain_vars,
                             'dir_domain': self.dir_domain_atm,
                             'file_domain': self.file_domain_atm, 
                             'dir_forcing': self.dir_forcing,
                             'year_files': '\n'.join(year_files),
                             'vars_tpqw': str_tpqw}

        keys_streams_co2 = {'co2_domain_vars': str_co2_domain_vars,
                             'dir_domain': self.dir_domain_co2,
                             'file_domain': self.file_domain_co2, 
                             'dir_co2': self.dir_co2,
                             'file_co2': self.file_co2,
                             'vars_co2': str_co2}

        self.search_replace(f'{Path(__file__).resolve().parent}/config_files/user_datm/', 
                            'user_datm.streams.txt.CLMCRUNCEPv7.Precip', 
                            keys_streams_precn, 
                            dir_setup)

        self.search_replace(f'{Path(__file__).resolve().parent}/config_files/user_datm/', 
                            'user_datm.streams.txt.CLMCRUNCEPv7.Solar', 
                            keys_streams_solar, 
                            dir_setup)

        self.search_replace(f'{Path(__file__).resolve().parent}/config_files/user_datm/', 
                            'user_datm.streams.txt.CLMCRUNCEPv7.TPQW', 
                            keys_streams_tpqw, 
                            dir_setup)

        self.search_replace(f'{Path(__file__).resolve().parent}/config_files/user_datm/', 
                            'user_datm.streams.txt.co2tseries.20tr', 
                            keys_streams_co2, 
                            dir_setup)
        
        subprocess.call(f'{dir_setup}/preview_namelists', cwd = dir_setup)
        subprocess.call(f'cp user_datm.streams.txt.* Buildconf/datmconf/', shell = True, cwd = dir_setup)

        print('\nCase stream files created.\n')


    def build(self, clean: bool = False):

        """
        Build the model case with the case.build script.

        """

        dir_setup = f'{self.dir_script}/{self.name}'

        with open(f'{dir_setup}/CaseStatus', 'r') as file, \
            mmap.mmap(file.fileno(), 0, access = mmap.ACCESS_READ) as s:
            
            if s.find(b'case.build success') != -1:

                print('Case was already built. Clean?')
                
                if not clean: return

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

        dir_setup = f'{self.dir_script}/{self.name}'

        print('\nCase submit...\n')

        subprocess.call([f'{dir_setup}/case.submit', '--resubmit-immediate'], cwd = dir_setup)

        print('\nCase submitted. All done!\n')

        