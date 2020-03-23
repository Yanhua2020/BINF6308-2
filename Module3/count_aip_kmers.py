#!/usr/bin/env python
#count_aip_kmers.py
import re
import os
kmer_length =6
kmer_dictionary = {}
read_sample = open('/scratch/AiptasiaMiSeq/fastq/Aip02.R1.fastq','r')

line = ' '

# While line is not empty
while line:
        # Read one line from the file
            line = read_sample.readline()
                # Remove end-of-line character
            line = line.rstrip(os.linesep)
            if re.match('^[ATGCN]+$', line):
                stop = len(line) - kmer_length + 1  
                for start in range(0, stop):
                    kmer =line[start:start + kmer_length]
# see if it's in the dictionary
                    if kmer in kmer_dictionary:
# Add one to the count
                         kmer_dictionary[kmer] += 1
                    else:
# It's not in the dictionary so add with a count of 1
                         kmer_dictionary[kmer] = 1

# Save a tab character to print output as tab-separated
t = "\t"

# Iterate over the k-mers in the dictionary
for kmer in kmer_dictionary:
# Get the count of how many times observed
                   count = kmer_dictionary[kmer]
# Convert the count to a string and make a tuple of the kmer and count
                   out = (kmer, str(count))
 
                   A= t.join(out)
                   
                   with open("aip_kmers.txt",'a') as out:
                       out.write(A)
                       
