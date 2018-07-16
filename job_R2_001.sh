#!/bin/bash --login
#SBATCH -N 1
#SBATCH -n 32
#SBATCH --exclusive
#SBATCH -p himem
#SBATCH -J job_run_R2
python extract_R2_L001_3_70.py