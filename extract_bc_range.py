#written by Tunaz (tislam@cs.odu.edu)
import re
import sys
import math
import time
import numpy

fp = open('/scratch-lustre/tisla003/Original_Data/summer2018/BLAT_output/18p/unqseq_occur_samebarcodes_18p.txt', 'r')
low_range = sys.argv[1]
high_range = sys.argv[2]
line_count = sum(1 for line in open('/scratch-lustre/tisla003/Original_Data/summer2018/BLAT_output/18p/unqseq_occur_samebarcodes_18p.txt'))   # line count in input.txt file
arr_head = []
arr_seq = []
arr_qs = []
fo = open('range_bc_'+low_range+'_'+high_range+'.txt', 'w')
start_time = time.time()
for i in range(0, line_count):
    line = fp.readline().replace('\n', '').split('_')
    #print line[0]
    if int(low_range) <= int(line[0]) <= int(high_range):
        fo.write(line[1]+'\n')
		
print("--- %s seconds ---" % (time.time() - start_time))
fp.close()
fo.close()

