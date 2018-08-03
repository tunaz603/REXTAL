import re
import sys
import math
import time
import numpy

fi_ln = open('/scratch-lustre/tisla003/Original_Data/summer2018/BLAT_output/18p/split_L002/illumina_bc_linenum_L002_big.fastq','r')

fo_line_number = open ('output_line_number_L002_3_70.txt','w')



line_count_bc = sum(1 for line in open('illumina_bc_linenum_L002_big.fastq'))
#print line_count_bc

start_time = time.time()
for i in range (0,line_count_bc):
    line_parts = fi_ln.readline().replace('\n','').split(":")
    #print line_parts[0], line_parts[1], line_parts[4] #ok
    fo_line_number.write(line_parts[0]+'\n')

print("--- %s seconds ---" % (time.time() - start_time))
fi_ln.close()


fo_line_number.close()
