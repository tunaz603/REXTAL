# -*- coding: utf-8 -*-
"""
Spyder Editor

//written by Tunaz (tislam@cs.odu.edu)

"""
    
import textwrap
final = list()

with open("18p_Bait_RM.fasta.2.7.7.80.10.50.500.mask", 'r') as fh_in:
    for line in fh_in:
        line = line.strip()
        if not line.startswith(">"):
            final.append(line)

final2 = "".join(final)

with open("18p_Bait_RM_tandem.fasta", 'w') as fh_out:
    fh_out.write(">hg38_chr18:131694-231693")
    fh_out.write("\n")
    fh_out.write('\n'.join(textwrap.wrap(final2, 50)))
'''
final2 = "".join(final)
print '\n'.join(textwrap.wrap(final2, 50))
'''