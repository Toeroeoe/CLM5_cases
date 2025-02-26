#!/bin/bash -x
#SBATCH --job-name=post_py
#SBATCH --account=jibg31
#SBATCH --ntasks=1
#SBATCH --mem 1024000
#SBATCH --time=24:00:00

source /p/scratch/cjibg31/jibg3105/projects/venvs/2024_03/activate.sh

srun -n 1 python post_process.py


