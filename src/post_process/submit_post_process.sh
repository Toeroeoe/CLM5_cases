#!/bin/bash -x
#SBATCH --job-name=post_py
#SBATCH --account=jibg31
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=32
#SBATCH --mem 1024000
#SBATCH --time=24:00:00

source /p/scratch/cjibg31/jibg3105/projects/model_setups/CLM5_cases/src/post_process/venv/activate.sh

srun -n 1 -c 32 \
    python make_yearly_resample.py \
    --inpath /p/data1/jibg31/CLM5_EU3_DETECT/BGC_outputs/history \
    --file CLM5-EUR0275-BGC_0001_JR.clm2.h0.*.nc \
    --outpath /p/scratch/cjibg31/jibg3105/data/CLM5EU3_DETECT/BGC/8daily \
    --tres 8D \
    --method mean \
    --tres_clm 1D \
    --vars ER \
            GPP \
            NEE \
            NPP \
            TOTECOSYSC \
            LEAFC \
            LEAFN \
            TOTSOMC \
            TOTSOMN \
            TOTVEGC \
            TOTVEGC \
            TLAI \
            BTRANMN \
            ALBD \
            QOVER \
            QIRRIG \
            QFLX_EVAP_TOT \
            QFLX_EVAP_GRND \
            QFLX_EVAP_VEG \
            H2OSOI \
            TWS \
            ZWT \
            GSSHA \
            GSSUN \
    --year_start 1960 \
    --year_end 2024 \


