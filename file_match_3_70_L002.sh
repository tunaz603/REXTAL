for f in /scratch-lustre/tisla003/Original_Data/summer2018/BLAT_output/18p/split_L002/x???; do
  grep -n -w -f "$f" /scratch-lustre/tisla003/Original_Data/longranger/longranger_input/HG00353/HG00353_S1_L002_I1_001.fastq 
done
