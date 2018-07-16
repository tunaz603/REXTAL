#!/bin/bash --login
#SBATCH -N 1
#SBATCH -n 32
#SBATCH --exclusive
#SBATCH -p himem
#SBATCH -J BLAT_18p

\time -o time_18p.txt blat /scratch-lustre/tisla003/Original_Data/summer2018/input/18p_Bait_RM_tandem.fasta /scratch-lustre/tisla003/Original_Data/longranger/longranger_output/barcoded_output/outs/nospace_modified_barcode_fasta_big.fasta /scratch-lustre/tisla003/Original_Data/summer2018/BLAT_output/18p/18p_blat.psl 

