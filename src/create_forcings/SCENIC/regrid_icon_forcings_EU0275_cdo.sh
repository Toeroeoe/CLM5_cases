#!/bin/bash -x

#SBATCH --job-name="prep_atm"
#SBATCH --nodes=1
#SBATCH --cpus-per-task=2
#SBATCH --time=6:00:00
#SBATCH --account=jibg31
#SBATCH --partition=dc-cpu
#SBATCH --error="log/prep_atm_%j.err"
#SBATCH --output="log/prep_atm_%j.out"

#Author: Bibi S. Naz, IBG3, b.naz@fz-juelich.de
#Date created: Sept 14 2023

ml Intel
ml ParaStationMPI
ml HDF
ml HDF5
ml NCO
ml CDO

outpath=/p/data1/jibg31/poppe1/FORCINGS/ICON_storylines/4K/
inpath=/p/data1/jibg31/AGRASIM/storyline_forcings/4K/eu011/

mkdir -p $outpath

for year in $(seq 2093 2098); do
    for mon in 01 02 03 04 05 06 07 08 09 10 11 12; do
        if [ ! -f ${outpath}/${year}-${mon}.nc ]; then
 		    cdo -O remap,EUR-0275_TSMP_FZJ-IBG3_1592x1544_LAND-LAKE-SEA-MASK_griddes.txt,weightfile_genbil.nc ${inpath}/${year}-${mon}.nc ${outpath}/${year}-${mon}.nc
        else
            echo "file ${outpath}/${year}-${mon}.nc already exists, skipping."
        fi
	done
done

