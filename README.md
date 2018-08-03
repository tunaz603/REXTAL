# REXTAL
To run REXTAL for 18p:
The key input data is 10X Genomics linked-reads from individual human genomes, in our case from the genome of a publically available cell line GM19440. Our dataset has approximately 1.49 billion 10X Genomics linked-reads in paired-end format, with each read about 150 bp.
1) Preprocessing:
  1) We processed the raw 10X Genomics data using Long Ranger Basic software developed by 10X Genomics (and freely available to any researcher)     to generate barcode-filtered 10XG linked-reads. The Long Ranger basic pipe-line performs basic read and barcode processing including read       trimming, barcode error correction, barcode whitelisting, and attaching barcodes to reads.
  2) extract 18p 1-copy, bait, segmental duplication from UC genome browser
  3) Use online RepeatMasker (RM)
  4) Use tandem repeat finder
  5) python code for wrapping the line (if needed) (text_wrap_affter_tandem_repeat_finder.py)
  
  
 2) Run REXTAL pipeline
    1) We have input fasta file (barcode-filtered 10XG linked-reads file, size: almost 600 GB) in a folder named /scratch-lustre/tisla003/Original_Data/longranger/longranger_output/barcoded_output/outs/nospace_modified_barcode_fasta_big.fasta. I used the directoy where I kept, you can rename it according to yours.
    2) We have another input fasta file (Hg38 extracted from UC genome browser ) in a folder named /scratch-lustre/tisla003/Original_Data/summer2018/input/18p_Bait_RM_tandem.fasta. I used the directoy where I kept, you can rename it according to yours.
    3) Keep the files pipeline_18p.sh (main REXTAL pipeline file), extract_bc_range.py, cluster_bc_multiple_3_70.py, file_match_3_70_L001.sh, file_match_3_70_L002.sh, get_line_number_L001.py, get_line_number_L002.py, extract_I1_L001_3_70.py, extract_R1_L001_3_70.py, extract_R2_L001_3_70.py, extract_I1_L002_3_70.py,  extract_R1_L002_3_70.py,  extract_R2_L002_3_70.py in a directory i.e. 18p.
    4) In SSH type:
      dos2unix pipeline_18p.sh
      chmod +x pipeline_18p.sh
    5) Run the job script:
      sbatch pipeline_18p.sh
 
 3) Output: 
 You will find output of REXTAL in ../18p/supernova_assembly_18/ here named as 18p_pseudohap2.1.fasta and 18p_pseudohap2.2.fasta.
      
Dependency:
To run REXTAL you have to install Longranger Basic, BLAT, 10X Genomics Supernova (assembler) in your server.
  

