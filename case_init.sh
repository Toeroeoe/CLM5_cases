
# Script to set up CLM5 cases
# With different arguments

# To do:
# - 



setup_CLM5_case(){

    # Don't change the function, change the variables
    # that are passed as arguments below
    
    local dir_user_config=$(pwd)/config_files

    cd $1

    if [ -d $2 ]; then

        echo "$2 case directory already exists."
        exit 1

    fi

    resubmit=$(( ($4-$3)/$5 ))

    local year_files=""

    for year in $(seq $3 $4); do

        for month in $(seq -f %02g 01 12); do

            file="${year}-${month}.nc"

            if [ $3 -eq $4 ] && [ $month -ne 12 ]; then

                file+="\n"
            
            elif [ $year -ne $4 ] && [ $month -ne 12 ]; then
                
                file+="\n"
                
            fi
            
            year_files+=$file

        done
    done

    # Please install config files accordingly
    # https://icg4geo.icg.kfa-juelich.de/ModelSystems/clm/CLM5.0_on_JSC_Machines
    # Load environment modules
    ${23} >/dev/null 2>&1
    module load Python

    # Create the case directory
    echo "Create case..."
    ./create_newcase --case $2 --res CLM_USRDAT --compset $6 --run-unsupported

    # Enter case dir
    cd $2

    # domain file and path is the same for ATM and LND
    ./xmlchange ATM_DOMAIN_PATH="$7",LND_DOMAIN_PATH="$7"
    ./xmlchange ATM_DOMAIN_FILE="$8",LND_DOMAIN_FILE="$8"

    ./xmlchange NTASKS=${20}
    ./xmlchange DATM_MODE=CLMCRUNCEPv7
   
    # Setup case
    ./case.setup

    # Copy the config files from repo to the case dir
    echo "Copy config files..."
    cp $dir_user_config/user_nl/* .
    cp $dir_user_config/user_datm/* .

    # Replace dummy variables in file with these settings
    echo "Adjust settings in config namelist files..."
    sed -i "s#file_surf#'$9/${10}'#" user_nl_clm
    sed -i "s#file_init#'${11}/${12}'#" user_nl_clm
    sed -i "s#hist_vars#${13}#" user_nl_clm
    sed -i "s#hist_frq#${14}#" user_nl_clm
    sed -i "s#hist_flt#${15}#" user_nl_clm

    sed -i "s#year_start#$3#g" user_nl_datm
    sed -i "s#year_end#$4#" user_nl_datm

    echo "Adjust settings in config datm stream files..."
    sed -i "s#dir_domain#$7#" user_datm.streams.txt.CLMCRUNCEPv7.Precip
    sed -i "s#file_domain#$8#" user_datm.streams.txt.CLMCRUNCEPv7.Precip
    sed -i "s#dir_forcing#${16}#" user_datm.streams.txt.CLMCRUNCEPv7.Precip
    sed -i "s#year_files#$year_files#" user_datm.streams.txt.CLMCRUNCEPv7.Precip

    sed -i "s#dir_domain#$7#" user_datm.streams.txt.CLMCRUNCEPv7.Solar
    sed -i "s#file_domain#$8#" user_datm.streams.txt.CLMCRUNCEPv7.Solar
    sed -i "s#dir_forcing#${16}#" user_datm.streams.txt.CLMCRUNCEPv7.Solar
    sed -i "s#year_files#$year_files#" user_datm.streams.txt.CLMCRUNCEPv7.Solar

    sed -i "s#dir_domain#$7#" user_datm.streams.txt.CLMCRUNCEPv7.TPQW
    sed -i "s#file_domain#$8#" user_datm.streams.txt.CLMCRUNCEPv7.TPQW
    sed -i "s#dir_forcing#${16}#" user_datm.streams.txt.CLMCRUNCEPv7.TPQW
    sed -i "s#year_files#$year_files#" user_datm.streams.txt.CLMCRUNCEPv7.TPQW

    ./preview_namelists
    
    # Copy user_datm_* to the Buildconf/datmconf;
    cp user_datm.streams* Buildconf/datmconf

    ## Align DATM to the beggining and end year of the available forcing
    ./xmlchange DATM_CLMNCEP_YR_ALIGN=$3,DATM_CLMNCEP_YR_START=$3,DATM_CLMNCEP_YR_END=$4

    ## Every Job will have STOP_N simulation years; starting from year_start.
    ./xmlchange STOP_OPTION=nyears,RUN_STARTDATE=$3-01-01,STOP_DATE=-1,STOP_N=$5

    # atmospheric CO2 options
    ./xmlchange CCSM_BGC=${17}
    ./xmlchange CLM_CO2_TYPE=${18}
    ./xmlchange DATM_CO2_TSERIES=${19}

    # Resubmit times (How many times STOP_N should be simulated?)
    ./xmlchange RESUBMIT=$resubmit

    # Use Coldstart or initial file (if available)?
    ./xmlchange CLM_FORCE_COLDSTART=${22}

    # CLM just supports half hourly (*_NCPL=48) and hourly time steps.
    ./xmlchange ATM_NCPL=${21},LND_NCPL=${21}

    # Turn off annoying archive job
    ./xmlchange DOUT_S=FALSE

    # ready to build and submit !!!
    if ${24}; then
        ./case.build
    fi

} 


### User settings
# The script that loades the necessary CLM5 environment modules
env=/p/home/jusers/poppe1/jureca/CLM5.0_on_JSC_Machines/clm50.jsc_generic.loadenvs

# Directories
# Work directory with create_newcase script
dir_work=/p/project/cjibg31/jibg3105/clm5.0/cime/scripts
dir_domain=/p/scratch/cjibg31/shared/EUR-0275_domain
dir_surf=/p/scratch/cjibg31/shared/EUR-0275_surface
dir_forcing=/p/scratch/cjibg31/shared/EUR-0275_forcings_ERA5
dir_init=none
file_init=none

# File names
file_domain=domain.lnd.EUR-0275.230303_cut.nc
file_surf=surfdata_EUR-0275_hist_16pfts_Irrig_CMIP6_simyr2000_c230216_GLC2000.nc

# Main case settings
name_case=CLM5EUR-0275_SP_ERA5_3_GLC2000_test
compset=2000_DATM%CRUv7_CLM50%SP_SICE_SOCN_MOSART_SGLC_SWAV
NTASKS=1024

# Start and end year of simulation
year_start=1979
year_end=1979
stop_n=1

# Frequency ouput and file arrangements
# https://escomp.github.io/ctsm-docs/versions/release-clm5.0/html/users_guide/setting-up-and-running-a-case/customizing-the-clm-namelist.html
hist_frq=-24
hist_flt=365

# Atmospheric carbon module
# To turn off set CCSM_BGC to none
# https://docs.cesm.ucar.edu/models/cesm2/settings/current/drv_input_cesm.html
CCSM_BGC=none 
CLM_CO2_TYPE=diagnostic
DATM_CO2_TSERIES=SSP3-7.0

# Number of time steps per day
# Either 24 or 48
NCPL=24

# COLDSTART without interpolating from global init file
# on or off
COLDSTART=on

# History or output variables
# https://www2.cesm.ucar.edu/models/cesm1.2/clm/models/lnd/clm/doc/UsersGuide/history_fields_table_40.xhtml
hist_vars="'QFLX_EVAP_TOT','ALBD','TLAI'"

# Bool if you want the script to directly build your case
build=false


setup_CLM5_case $dir_work $name_case $year_start $year_end $stop_n $compset \
        $dir_domain $file_domain $dir_surf $file_surf $dir_init $file_init \
        $hist_vars $hist_frq $hist_flt $dir_forcing $CCSM_BGC $CLM_CO2_TYPE \
        $DATM_CO2_TSERIES $NTASKS $NCPL $COLDSTART $env $build

