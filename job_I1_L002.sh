#!/bin/bash --login
#SBATCH -N 1
#SBATCH -n 32
#SBATCH --exclusive
#SBATCH -p himem
#SBATCH -J job_run_I2
python extract_I1_L002_3_70.py