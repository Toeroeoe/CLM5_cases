
# Script to set up CLM5 cases
# With different arguments

# To do:
# - output from pft and column level
# - setting to adapt in existing case
# - Option to do monthly or other runs (not necessarly yearly)
# - what about the env script there
# - more transparent function input parameters



setup_CLM5_case(){

    # Don't change the function, change the variables
    # that are passed as arguments below
    
    local dir_user_config=$(pwd)/config_files
    local dir_work=$1
    local name_case=$2
    local year_start=$3
    local year_end=$4
    local stop_n=$5
    local compset=$6
    local dir_domain=$7
    local file_domain=$8
    local dir_surf=$9
    local file_surf=$10
    local dir_init=$11
    local file_init=$12
    local hist_vars=$13
    local hist_frq=$14
    local hist_flt=$15
    local dir_forcing=$16
    local mode_co2=$17
    local type_co2=$18
    local series_co2=$19
    local n_cpu=$20
    local ncpl=$21
    local coldstart=$22
    local env=$23
    local build=$24
    local flag_co2=$25
    local wallclock_time=$26
    local AC_spin_up=$27
    local type_case=$28

    cd $dir_work

    if [ -d $name_case ]; then

        echo "$name_case case directory already exists."
        exit 1

    fi

    local year_files=""

    for year in $(seq $year_start $year_end); do
        
        for month in $(seq -f %02g 01 12); do

            file="${year}-${month}.nc\n"

            if [ $year -eq $year_end ] && [ $month -eq 12 ]; then

                file=${file::-2}
            fi

            year_files+=$file

        done

    done

    # Please install config files accordingly
    # https://icg4geo.icg.kfa-juelich.de/ModelSystems/clm/CLM5.0_on_JSC_Machines
    # Load environment modules
    $env >/dev/null 2>&1

    # Create the case directory
    echo "Create case..."
    ./create_newcase --case $name_case --res CLM_USRDAT --compset $compset --run-unsupported

    # Enter case dir
    cd $name_case

    # domain file and path is the same for ATM and LND
    ./xmlchange ATM_DOMAIN_PATH="$dir_domain",LND_DOMAIN_PATH="$dir_domain"
    ./xmlchange ATM_DOMAIN_FILE="$file_domain",LND_DOMAIN_FILE="$file_domain"

    ./xmlchange NTASKS=$n_cpu
    ./xmlchange DATM_MODE=CLMCRUNCEPv7
   
    # Setup case
    ./case.setup

    # Copy the config files from repo to the case dir
    echo "Copy config files..."
    cp $dir_user_config/user_nl/* .
    cp $dir_user_config/user_datm/* .

    # Replace dummy variables in file with these settings
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
    
    # Copy user_datm_* to the Buildconf/datmconf;
    cp user_datm.streams* Buildconf/datmconf

    ## Align DATM to the beggining and end year of the available forcing
    ./xmlchange DATM_CLMNCEP_YR_ALIGN=$year_start,DATM_CLMNCEP_YR_START=$year_end,DATM_CLMNCEP_YR_END=$year_end

    ## Every Job will have STOP_N simulation years; starting from year_start.
    ./xmlchange STOP_OPTION=nyears,RUN_STARTDATE=$year_start-01-01,STOP_DATE=-1,STOP_N=$stop_n
    ./xmlchange JOB_WALLCLOCK_TIME=$wallclock_time

    # atmospheric CO2 options
    if [ $flag_co2 == "T" ]; then
        ./xmlchange CCSM_BGC=$mode_co2
        ./xmlchange CLM_CO2_TYPE=$type_co2
        ./xmlchange DATM_CO2_TSERIES=$series_co2
    fi

    # Accelerated decomposition mode for first part of spin up
    ./xmlchange CLM_ACCELERATED_SPINUP=$AC_spin_up
    
    # Resubmit times (How many times STOP_N should be simulated?)
    ./xmlchange RESUBMIT=$(( ($year_end-$year_start)/$stop_n ))

    # Use Coldstart or initial file (if available)?
    ./xmlchange CLM_FORCE_COLDSTART=$coldstart

    # CLM just supports half hourly (*_NCPL=48) and hourly time steps.
    ./xmlchange ATM_NCPL=$ncpl,LND_NCPL=$ncpl

    # Turn off annoying archive job
    ./xmlchange DOUT_S=FALSE

    # ready to build and submit !!!
    if [ $build == "T" ]; then
        ./case.build
    fi

} 


### User settings

# Case type (spin up or production)
type_case=spinup

# The script that loades the necessary CLM5 environment modules
env=$HOME/CLM5.0_on_JSC_Machines/clm50.jsc_generic.loadenvs

# Directories
# Work directory with create_newcase script
dir_work=/p/project/cjibg31/jibg3105/clm5.0/cime/scripts
dir_domain=/p/scratch/cjibg31/shared/TEST
dir_surf=/p/scratch/cjibg31/shared/TEST
dir_forcing=/p/scratch/cjibg31/shared/EUR-0275_forcings_ERA5
dir_init=none
file_init=none

# File names
file_domain=domain.lnd.EUR-0275_EUR-0275.230912.nc
file_surf=surfdata_EUR-0275_hist_16pfts_Irrig_CMIP6_simyr2000_c230216_GLC2000.nc

# Main case settings
name_case=CLM5EUR-0275_SP_ERA5_TEST_CARLS_1979
compset=2000_DATM%CRUv7_CLM50%SP_SICE_SOCN_MOSART_SGLC_SWAV
n_cpu=1024

# Start and end year of simulation
year_start=1979
year_end=2000
stop_n=6
wallclock_time="24:00:00"

# Frequency ouput and file arrangements
# https://escomp.github.io/ctsm-docs/versions/release-clm5.0/html/users_guide/setting-up-and-running-a-case/customizing-the-clm-namelist.html
hist_frq=-24
hist_flt=365

# Atmospheric carbon module
# To turn off set CCSM_BGC to none
# https://docs.cesm.ucar.edu/models/cesm2/settings/current/drv_input_cesm.html
# https://escomp.github.io/ctsm-docs/versions/master/html/users_guide/running-special-cases/Running-stand-alone-CLM-with-transient-historical-CO2-concentration.html
flag_co2="F" # "T"rue or "F"alse
mode_co2=CO2A 
type_co2=diagnostic
series_co2=20tr

# Number of time steps per day
# Either 24 or 48
NCPL=24

# History or output variables
# https://www2.cesm.ucar.edu/models/cesm1.2/clm/models/lnd/clm/doc/UsersGuide/history_fields_table_40.xhtml
hist_vars="'QFLX_EVAP_TOT','ALBD','TLAI'"

# 'DISPVEGC', 'DISPVEGN', 'DOWNREG', 'ER', 'GPP', 'GROSS_NMIN', 'LEAFC', 'LEAFN', 'LNC', 'NBP', 'NDEP_TO_SMINN', 'NEE', 
# 'NEP', 'NPP', 'PLANT_NDEMAND', 'STORVEGC', 'STORVEGN', 'TOTCOLN', 'TOTCOLC', 'TOTECOSYSC', 'TOTECOSYSN', 'TOTPFTC', 'TOTPFTN', 'TOTSOMC', 'TOTSOMN', 'TOTVEGC', 'TOTVEGN',
# 'FSM', 'Qle', 'Rnet', 'SWdown', 'TBOT','SWup','Qh','LWdown','LWup','Qstor','ALBD', 'ALBGRD', 'TSOI',
# 'FCEV', 'FCTR', 'FGEV', 'FGR', 'FSNO', 'QCHARGE', 'RAIN', 'QOVER', 'QIRRIG', 'QINFL', 'QINTR', 'QFLX_EVAP_VEG', 'QFLX_EVAP_GRND', 'QFLX_EVAP_TOT', 'QICE', 'H2OCAN', 'H2OCAN', 'QDRAI',
# 'H2OSNO', 'H2OSOI', 'RH', 'SNOW', 'SNOWDP', 'SNOWICE', 'SNOTTOPL', 'SNOWLIQ', 'TLAI', 'TSAI', 'TWS','ZWT','GSSHA','GSSUN' 
# 'VEGWP'
# 'FDRY'
# 'QROOTSINK'

# Which of these can be output from COLUMN or PFT level?

# Bool if you want the script to directly build your case
# "T"rue or "F"alse

# COLDSTART without interpolating from global init file
# on or off
coldstart=on

# Accelerated decomposition (as first part of spinup?)?
AC_spin_up=off

build="F" 


setup_CLM5_case #1 
                $dir_work \
                #2
                $name_case \ 
                #3
                $year_start \
                #4
                $year_end \
                #5
                $stop_n \
                #6
                $compset \
                #7
                $dir_domain \
                #8
                $file_domain \
                #9
                $dir_surf \
                #10
                $file_surf \
                #11
                $dir_init \ 
                #12
                $file_init \ 
                #13
                $hist_vars \ 
                #14
                $hist_frq \ 
                #15
                $hist_flt \ 
                #16
                $dir_forcing \ 
                #17
                $mode_co2 \ 
                #17
                $type_co2 \ 
                #19
                $series_co2 \ 
                #20
                $n_cpu \ 
                #21
                $NCPL \ 
                #22
                $coldstart \ 
                #23
                $env \ 
                #24
                $build \ 
                #25
                $flag_co2 \ 
                #26
                $wallclock_time \ 
                #27
                $AC_spin_up \ 
                #28
                $type_case


