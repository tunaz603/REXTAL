#!/bin/bash
#SBATCH -N 1
#SBATCH -n 32
#SBATCH --exclusive
#SBATCH -p himem
#SBATCH -J job_longranger_run
start_time=`date +%s`
cd /scratch-lustre/tisla003/Original_Data/longranger/longranger_output &&
longranger basic --id=barcoded_output \--fastqs=/scratch-lustre/tisla003/Original_Data/longranger/longranger_input/HG00353 &&
end_time=`date +%s`
echo execution time was `expr $end_time - $start_time` s.