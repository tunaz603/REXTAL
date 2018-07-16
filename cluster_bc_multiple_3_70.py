# -*- coding: utf-8 -*-
"""
Created on Fri Jan 05 17:19:40 2018

@author: tislam
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Nov 08 10:45:21 2017

@author: tislam
"""

import re
import sys
import math
import time
import numpy

fi_1 = open('barcode_blat_output_3_70.txt','r')
fi_2 = open('start_position_3_70.txt','r')

fo_1 = open ('barcode_yes_3_70_less_than_50kb.txt','w')
fo_2 = open ('barcode_no_3_70_less_than_50kb.txt','w')

fo_3 = open ('barcode_yes_3_70_less_than_100kb.txt','w')
fo_4 = open ('barcode_no_3_70_less_than_100kb.txt','w')


num_lines = sum(1 for line in open('barcode_blat_output_3_70.txt'))
#print num_lines #ok

start_time = time.time()
array_barcode = []
array_st_position = []
array_comma_count = []
for i in range (0,num_lines):
    line_parts_barcode = fi_1.readline().replace('\n','')
    #array_barcode.append(line_parts_barcode)
    line_parts_position = fi_2.readline().replace('\n','').split(',')
    count_comma = len (line_parts_position)
    array_comma_count.append(count_comma)
   # print count_comma
        
    #array_st_position.append(int(line_parts_position[0]))
    if count_comma == 2:
        array_st_position.append(int(line_parts_position[0]))
        array_barcode.append(line_parts_barcode)
    if count_comma == 3:
        for i in range (0, count_comma-1):
            array_st_position.append(int(line_parts_position[i]))
            array_barcode.append(line_parts_barcode)
    if count_comma == 4:
        for i in range (0, count_comma-1):
            array_st_position.append(int(line_parts_position[i]))
            array_barcode.append(line_parts_barcode)
    if count_comma == 5:
        for i in range (0, count_comma-1):
            array_st_position.append(int(line_parts_position[i]))
            array_barcode.append(line_parts_barcode)
    if count_comma == 6:
        for i in range (0, count_comma-1):
            array_st_position.append(int(line_parts_position[i]))
            array_barcode.append(line_parts_barcode)
    if count_comma == 7:
        for i in range (0, count_comma-1):
            array_st_position.append(int(line_parts_position[i]))
            array_barcode.append(line_parts_barcode)
    if count_comma == 8:
        for i in range (0, count_comma-1):
            array_st_position.append(int(line_parts_position[i]))
            array_barcode.append(line_parts_barcode)
        
#print array_barcode #ok
#print array_st_position #ok
print max(array_comma_count) #if this value is greater than 8 please add more conditions like //if count_comma == 8: in previous line. 

array_break_pos =[]
for i in range (0, len(array_barcode)-1):
    if array_barcode[i] != array_barcode[i+1]:
        array_break_pos.append(i+1) #break point
#print array_break_pos #ok


array_position_cluster_all = []
array_barcode_cluster_all = []
k=0
for i in range (0, len (array_break_pos)+1):
    array_position_cluster = []
    array_barcode_cluster = []
    #1st block
    if i == 0:
        for j in range (i,array_break_pos[i]):
            array_position_cluster.append (array_st_position[j])
            array_barcode_cluster.append (array_barcode[j])
            k = j + 1
    #last block
    if i == len (array_break_pos) :
        for l in range  (int(array_break_pos[len (array_break_pos) -1 ]) , len (array_st_position)  ):
            array_position_cluster.append (array_st_position[l])
            array_barcode_cluster.append (array_barcode[l])
    #middle blocks
    else:
         for m in range (k,array_break_pos[i]):
            array_position_cluster.append (array_st_position[m])
            array_barcode_cluster.append (array_barcode[m])
            k = m+1
    #print (array_position_cluster)#ok
    array_position_cluster_all.append((array_position_cluster)) # keep barcode wise position cluster-wise 
    array_barcode_cluster_all.append((array_barcode_cluster))

#print array_position_cluster_all #ok
#print array_barcode_cluster_all #ok
#print len(array_position_cluster_all) #ok
#print array_position_cluster_all[1][2] #ok
array_new = []

val_max = []
val_min = []
for i in range (0, len (array_position_cluster_all)):
    val_max.append(max(array_position_cluster_all[i]))
    val_min.append(min(array_position_cluster_all[i]))
#print val_max #ok
#print val_min #ok
#fo_11.write(str(val_max) + '\n')
#fo_12.write(str(val_min) + '\n')

distance = []
for i in range (0, len (val_max)):
    distance.append(val_max[i]-val_min[i])
    
#print distance #ok

# 50kb calculation
barcode_yes_50kb = []
barcode_no_50kb = []
for i in range (0, len(distance)):
    if int(distance [i]) <= 50000:
        flag = i
        #print 'yes'
        barcode_yes_50kb.append(array_barcode_cluster_all[flag][0])
       
    else:
        flag1 = i
        #print 'No'
        barcode_no_50kb.append(array_barcode_cluster_all[flag1][0])
#print barcode_yes_50kb #ok
#print barcode_no_50kb #ok
for i in range (0, len(barcode_yes_50kb)):
    fo_1.write(str(barcode_yes_50kb[i]) + '\n')
for i in range (0, len(barcode_no_50kb)):
    fo_2.write(str(barcode_no_50kb[i]) + '\n')
    
# 100kb calculation
barcode_yes_100kb = []
barcode_no_100kb = []

for i in range (0, len(distance)):
    if int(distance [i]) <= 100000:
        flag = i
        #print 'yes'
        barcode_yes_100kb.append(array_barcode_cluster_all[flag][0])
       
		
        #print val_max[i]," ", val_min[i] #ok
        
       
    else:
        flag1 = i
        #print 'No'
        barcode_no_100kb.append(array_barcode_cluster_all[flag1][0])
#print barcode_yes_50kb #ok
#print barcode_no_50kb #ok
for i in range (0, len(barcode_yes_100kb)):
    fo_3.write(str(barcode_yes_100kb[i]) + '\n')
for i in range (0, len(barcode_no_100kb)):
    fo_4.write(str(barcode_no_100kb[i]) + '\n')
    
print("--- %s seconds ---" % (time.time() - start_time))

fi_1.close()
fi_2.close()

fo_1.close()
fo_2.close()
fo_3.close()
fo_4.close()