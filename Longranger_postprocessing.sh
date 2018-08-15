#!/bin/bash
#SBATCH -N 1
#SBATCH -n 32
#SBATCH --exclusive
#SBATCH -p himem
#SBATCH -J job_longranger_postprcessing
start_time=`date +%s`
cd /scratch-lustre/tisla003/Original_Data/longranger/longranger_output/barcoded_output/outs/ &&
seqtk seq -a barcoded.fastq > barcoded_fasta_big.fasta &&
gawk '{if ($0 ~/^>/) {h[$1]++; $1=$1 "_" h[$1]} print}' /scratch-lustre/tisla003/Original_Data/longranger/longranger_output/barcoded_output/outs/barcoded_fasta_big.fasta >/scratch-lustre/tisla003/Original_Data/longranger/longranger_output/barcoded_output/outs/modified_barcode_fasta_big.fasta &&
tr ' ' '_' </scratch-lustre/tisla003/Original_Data/longranger/longranger_output/barcoded_output/outs/modified_barcode_fasta_big.fasta >/scratch-lustre/tisla003/Original_Data/longranger/longranger_output/barcoded_output/outs/nospace_modified_barcode_fasta_big.fasta &&
end_time=`date +%s`
echo execution time was `expr $end_time - $start_time` s.
