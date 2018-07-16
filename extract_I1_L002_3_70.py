import re
import sys
import math
import time
import numpy

fp = open('/scratch-lustre/tisla003/Original_Data/longranger/longranger_input/HG00353/HG00353_S1_L002_I1_001.fastq', 'r')
fi_ln = open('/scratch-lustre/tisla003/Original_Data/summer2018/BLAT_output/18p/split_L002/output_line_number_L002_3_70.txt','r')
fo = open('print_L002_I1.fastq', 'w')
line_count = 1481146588  # line count in HG00353_S1_L002_I1_001.fastq file = 1481146588
arr_head = []
arr_seq = []
arr_qs = []
start_time = time.time()
for i in range(0, line_count / 4):
    line1 = fp.readline().replace('\n', '')
    line2 = fp.readline().replace('\n', '')
    line3 = fp.readline().replace('\n', '')
    line4 = fp.readline().replace('\n', '')
    arr_head.append(line1)
    arr_seq.append(line2)
    arr_qs.append(line4)
#print len(arr_head)
lc_align_sorted_count = sum(1 for line in open('output_line_number_L002_3_70.txt'))
for i in range(0, lc_align_sorted_count):
    line_parts = fi_ln.readline().replace('\n', '')
    #for i in range(0, len(arr_head)):
    fo.write(arr_head[(int(line_parts)-1)/4] + '\n')
    fo.write(arr_seq[(int(line_parts)-1)/4] + '\n')
    fo.write('+' + '\n')
    fo.write(arr_qs[(int(line_parts)-1)/4] + '\n')
print("--- %s seconds ---" % (time.time() - start_time))
fp.close()
fi_ln.close()
fo.close()

