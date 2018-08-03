#!/bin/bash
#SBATCH -N 1
#SBATCH -n 32
#SBATCH --exclusive
#SBATCH -p himem
#SBATCH -J job_pipeline_18p
start_time=`date +%s`
\time -o time_18p.txt blat /scratch-lustre/tisla003/Original_Data/summer2018/input/18p_Bait_RM_tandem.fasta /scratch-lustre/tisla003/Original_Data/longranger/longranger_output/barcoded_output/outs/nospace_modified_barcode_fasta_big.fasta /scratch-lustre/tisla003/Original_Data/summer2018/BLAT_output/18p/18p_blat.psl &&
grep -oP "E00489.\S*" 18p_blat.psl > header_18p.fastq &&  
grep -oP 'E00489.*-1' header_18p.fastq > name10X_barcode_18p.txt &&
sed 's/\_1_/_/g' name10X_barcode_18p.txt > modified10X_barcode_18p.txt &&
sed 's/\_2_/_/g' modified10X_barcode_18p.txt > new10X_barcode_18p.txt && 
sort -t_ -k2,2 new10X_barcode_18p.txt > sorted_10X_18p.txt &&
uniq sorted_10X_18p.txt > unq_seq_10X_18p.txt &&
awk -F '_' '{sub(/"".*$/, "", $2); print $2}' unq_seq_10X_18p.txt > unqseq_samebarcodes_18p.txt &&
sed -e 's/^/_/' unqseq_samebarcodes_18p.txt > unqseq_modified_samebarcodes_18p.txt &&
uniq -c unqseq_modified_samebarcodes_18p.txt | sort > unqseq_occur_samebarcodes_18p.txt &&
python extract_bc_range.py 3 70 &&
grep -f "range_bc_3_70.txt" 18p_blat.psl > blat_output_3_70.txt &&
cut -f21 blat_output_3_70.txt > start_position_3_70.txt &&
grep -o '\_B.*-1' blat_output_3_70.txt > extract_barcode_blat_output_3_70.txt &&
cut -f1 extract_barcode_blat_output_3_70.txt > barcode_blat_output_3_70.txt &&
python cluster_bc_multiple_3_70.py &&
grep -f "barcode_yes_3_70_less_than_100kb.txt" /scratch-lustre/tisla003/Original_Data/longranger/longranger_output/barcoded_output/outs/nospace_modified_barcode_fasta_big.fasta > ranged_common_part_bc_100kb_3_70.fastq &&
awk -F '_' '{sub(/"".*$/, "", $1); print $1}' ranged_common_part_bc_100kb_3_70.fastq > common_part_100kb_3_70.fastq &&
cut -c 2- common_part_100kb_3_70.fastq > new_common_part_100kb_3_70.fastq &&
awk -F ':' '{sub(/"".*$/, "", $4); if($4==1) print $0}' new_common_part_100kb_3_70.fastq > com_part_L001_100kb_3_70.fastq &&
awk -F ':' '{sub(/"".*$/, "", $4); if($4==2) print $0}' new_common_part_100kb_3_70.fastq > com_part_L002_100kb_3_70.fastq &&
sort com_part_L001_100kb_3_70.fastq | uniq > unq_com_part_L001_100kb_3_70.fastq &&
sort com_part_L002_100kb_3_70.fastq | uniq > unq_com_part_L002_100kb_3_70.fastq &&
mkdir split_L001 split_L002 &&
mv unq_com_part_L001_100kb_3_70.fastq file_match_3_70_L001.sh get_line_number_L001.py extract_I1_L001_3_70.py extract_R1_L001_3_70.py extract_R2_L001_3_70.py split_L001 &&
mv unq_com_part_L002_100kb_3_70.fastq file_match_3_70_L002.sh get_line_number_L002.py extract_I1_L002_3_70.py extract_R1_L002_3_70.py extract_R2_L002_3_70.py split_L002 &&
mkdir supernova_assembly_18p &&
wait
{
cd split_L001
split -l 2690 -a 3 unq_com_part_L001_100kb_3_70.fastq 
dos2unix file_match_3_70_L001.sh
chmod +x file_match_3_70_L001.sh
./file_match_3_70_L001.sh > illumina_bc_linenum_L001_big.fastq
python get_line_number_L001.py
{ 
python extract_I1_L001_3_70.py
mv print_L001_I1.fastq HG00353_S1_L001_I1_001.fastq
}&
{
python extract_R1_L001_3_70.py
mv print_L001_R1.fastq HG00353_S1_L001_R1_001.fastq
}
{
python extract_R2_L001_3_70.py
mv print_L001_R2.fastq HG00353_S1_L001_R2_001.fastq 
} 
} &
{
cd split_L002
split -l 2690 -a 3 unq_com_part_L002_100kb_3_70.fastq 
dos2unix file_match_3_70_L002.sh
chmod +x file_match_3_70_L002.sh
./file_match_3_70_L002.sh > illumina_bc_linenum_L002_big.fastq
python get_line_number_L002.py
{
python extract_I1_L002_3_70.py
mv print_L002_I1.fastq HG00353_S1_L002_I1_001.fastq 
} &
{
python extract_R1_L002_3_70.py
mv print_L002_R1.fastq HG00353_S1_L002_R1_001.fastq
} &
{
python extract_R2_L002_3_70.py
mv print_L002_R2.fastq HG00353_S1_L002_R2_001.fastq
} 
}
wait
cd ../ &&
cd split_L001 &&
mv HG00353_S1_L001_I1_001.fastq HG00353_S1_L001_R1_001.fastq HG00353_S1_L001_R2_001.fastq ../supernova_assembly_18p &&
cd ../ &&
cd split_L002 &&
mv HG00353_S1_L002_I1_001.fastq HG00353_S1_L002_R1_001.fastq HG00353_S1_L002_R2_001.fastq ../supernova_assembly_18p &&
cd ../ &&
cd supernova_assembly_18p &&
supernova run --id=supernova_output_18p \--fastqs=/scratch-lustre/tisla003/Original_Data/summer2018/BLAT_output/18p/supernova_assembly_18p &&
supernova mkoutput --asmdir=/scratch-lustre/tisla003/Original_Data/summer2018/BLAT_output/18p/supernova_assembly_18p/supernova_output_18p/outs/assembly  \--outprefix=/scratch-lustre/tisla003/Original_Data/summer2018/BLAT_output/18p/supernova_assembly_18p/18p_pseudohap2 \--style=pseudohap2 &&
gunzip 18p*
end_time=`date +%s`
echo execution time was `expr $end_time - $start_time` s.