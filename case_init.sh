#### This script is to create a pan-European CLM5 case in 3 km spatial resolution.
#### Please not the specification of the case below and make changes accordingly.
####
#### The configuration files for the CLM5 case are available in this same repository.
####
#### A set of needed input data can be obtained from the author of this script:
####  - domain file (grid specifications),
####  - surface files (land surface characteristics),
####  - restart file (after BGC spinup, C pool equilibrium),
####  - atmospheric forcings (downscaled from COSMO-REA6).
####
#### Other required files are default global files from clm5 repositories;
#### and should be in the default $CESMROOT data directories.
####
#### Notes:
####  - Tested on jureca with 10 nodes (NTASKS setting),
####  - in hourly time steps (*_NCPL setting),
####  - when switching forcings, please change YR_ALIGN/START/END accordingly.
####  - monthly ouput (change it in user_nl_clm)
####  - The files can be found on jureca here /p/largedata/jibg36/CLM5EU3/full


### Directories
## Work directory with create_newcase script
dir_work=/p/project/cjibg31/jibg3105/clm5.0/cime/scripts
dir_user_config=$(pwd)/config_files

## Directories with input files
dir_domain=/p/scratch/cjibg31/shared/EUR-0275_domain
dir_surf=/p/scratch/cjibg31/shared/EUR-0275_surface
dir_forcing=/p/scratch/cjibg31/shared/EUR-0275_forcings_ERA5
#dir_forcing=/p/scratch/cjibg31/jibg3105/CESMDataRoot/InputData/Forcings/ERA5_EUR-0275/2021_test_2
#dir_init=/p/scratch/cjibg31/jibg3105/CESMDataRoot/InputData/lnd/clm2/initdata_map/CLM5EU3_BGC_000

### File names
file_domain=domain.lnd.EUR-0275.230303_cut.nc
#file_surf=surfdata_EUR-0275_hist_16pfts_Irrig_CMIP6_simyr2005_c230712_cut_pos.nc
file_surf=surfdata_EUR-0275_hist_16pfts_Irrig_CMIP6_simyr2000_c230216_GLC2000.nc
#file_surf=surfdata_EUR-0275_hist_78pfts_CMIP6_simyr2005_c230307_cut.nc
#file_init=CLM5EU3_BGC_r.nc

### Settings
name_case=CLM5EUR-0275_SP_ERA5_3_GLC2000
#compset=I2000Clm50BgcCruGs          # Other compsets are not tested
#compset=I2000Clm50BgcCropGs
#compset=2000_DATM%CRUv7_CLM50%BGC_SICE_SOCN_MOSART_SGLC_SWAV
compset=2000_DATM%CRUv7_CLM50%SP_SICE_SOCN_MOSART_SGLC_SWAV

## Start and end year of simulation; currently limited by forcing data availability
year_start=1979
year_end=1979
stop_n=1

## Frequency ouput and file arrangements
## https://escomp.github.io/ctsm-docs/versions/release-clm5.0/html/users_guide/setting-up-and-running-a-case/customizing-the-clm-namelist.html
hist_frq=-24
hist_flt=365

## History or output variables
#hist_vars="'GPP','QFLX_EVAP_TOT','ALBD','TLAI'"
hist_vars="'QFLX_EVAP_TOT','ALBD','TLAI'"

## How many resubmits
## Careful, not tested with other time periods
resubmit=$(( ($year_end-$year_start)/$stop_n ))




####################
####### Main #######
####################
### Changes in own risk

cd $dir_work

if [ -d $name_case ]; then
    
    echo "$name_case case directory already exists."
    exit 1

fi


year_files=""

for year in $(seq $year_start $year_end); do
    
    for month in $(seq -f %02g 01 12); do

        year_files+="${year}-${month}.nc\n"

    done
done


## Please install config files accordingly
## https://icg4geo.icg.kfa-juelich.de/ModelSystems/clm/CLM5.0_on_JSC_Machines
source ~/CLM5.0_on_JSC_Machines/clm50.jsc_generic.loadenvs >/dev/null 2>&1
## Create the case directory
echo "Create case..."
./create_newcase --case $name_case --res CLM_USRDAT --compset $compset --run-unsupported

cd $name_case
echo "Enter case directory..."
## domain file and path is the same for ATM and LND
./xmlchange ATM_DOMAIN_PATH="$dir_domain",LND_DOMAIN_PATH="$dir_domain"
./xmlchange ATM_DOMAIN_FILE="$file_domain",LND_DOMAIN_FILE="$file_domain"
## On jureca, with 10 nodes = 1280 CPUs
./xmlchange NTASKS=1024
./xmlchange DATM_MODE=CLMCRUNCEPv7
## Setup case
./case.setup

## Copy the config files from repo to the case dir
echo "Copy config files..."
cp $dir_user_config/user_nl/* .
cp $dir_user_config/user_datm/* .

## Replace dummy variables in file with these settings
echo "Adjust settings in config namelist files..."
sed -i "s#file_surf#'$dir_surf/$file_surf'#" user_nl_clm
sed -i "s#file_init#'$dir_init/$file_init'#" user_nl_clm
sed -i "s#hist_vars#$hist_vars#" user_nl_clm
sed -i "s#hist_frq#$hist_frq#" user_nl_clm
sed -i "s#hist_flt#$hist_flt#" user_nl_clm

sed -i "s#year_start#$year_start#g" user_nl_datm
sed -i "s#year_end#$year_end#" user_nl_datm

echo "Adjust settings in config datm stream files..."
sed -i "s#dir_domain#$dir_domain#" user_datm.streams.txt.CLMCRUNCEPv7.Precip
sed -i "s#file_domain#$file_domain#" user_datm.streams.txt.CLMCRUNCEPv7.Precip
sed -i "s#dir_forcing#$dir_forcing#" user_datm.streams.txt.CLMCRUNCEPv7.Precip
sed -i "s#year_files#$year_files#" user_datm.streams.txt.CLMCRUNCEPv7.Precip

sed -i "s#dir_domain#$dir_domain#" user_datm.streams.txt.CLMCRUNCEPv7.Solar
sed -i "s#file_domain#$file_domain#" user_datm.streams.txt.CLMCRUNCEPv7.Solar
sed -i "s#dir_forcing#$dir_forcing#" user_datm.streams.txt.CLMCRUNCEPv7.Solar
sed -i "s#year_files#$year_files#" user_datm.streams.txt.CLMCRUNCEPv7.Solar

sed -i "s#dir_domain#$dir_domain#" user_datm.streams.txt.CLMCRUNCEPv7.TPQW
sed -i "s#file_domain#$file_domain#" user_datm.streams.txt.CLMCRUNCEPv7.TPQW
sed -i "s#dir_forcing#$dir_forcing#" user_datm.streams.txt.CLMCRUNCEPv7.TPQW
sed -i "s#year_files#$year_files#" user_datm.streams.txt.CLMCRUNCEPv7.TPQW


./preview_namelists
echo "Copy files to Buildconf/datmconf"
## Copy user_datm_* to the Buildconf/datmconf;
## It does not happen automatically sometimes;
## And else it leads to an error.
cp user_datm.streams* Buildconf/datmconf

## Align DATM to the beggining and end year of the available forcing
./xmlchange DATM_CLMNCEP_YR_ALIGN=$year_start,DATM_CLMNCEP_YR_START=$year_start,DATM_CLMNCEP_YR_END=$year_end

## Every Job will have STOP_N simulation years; starting from year_start.
## With JURECA and using 1280 CPUs, the model runs ca. 6 years per 20 hours (please check)
./xmlchange STOP_OPTION=nyears,RUN_STARTDATE=$year_start-01-01,STOP_DATE=-1,STOP_N=$stop_n

## CO2 constant (für I2000 compsets CO2 concentration = start year concentration)
## CO2A is transient concentration diagnostic
# ./xmlchange CCSM_BGC=none
#./xmlchange CCSM_BGC=CO2A
#./xmlchange CLM_CO2_TYPE=diagnostic
#./xmlchange DATM_CO2_TSERIES=SSP3-7.0

## Resubmit times (How many times STOP_N should be simulated?)
./xmlchange RESUBMIT=$resubmit

## Use Coldstart or initial file (if available)?
#./xmlchange CLM_FORCE_COLDSTART=on
#./xmlchange CLM_ACCELERATED_SPINUP=off

## Hourly time step, to make the continental model faster.
## CLM just supports half hourly (*_NCPL=48) and hourly time steps.
./xmlchange ATM_NCPL=24,LND_NCPL=24

## Turn off annoying archive job
./xmlchange DOUT_S=FALSE

## ready to build and submit !!!
./case.build
#./case.submit