#!/usr/bin/env python
# get_all_kmers2.py
seq = 'GCCGGCCCTCAGACAGGAGTGGTCCTGGATG'
kmer_length = 6
# Calculate the stop before the loop to improve efficiency. 
stop = len(seq) - kmer_length + 1
for start in range(0, stop):
        kmer = seq[start:start + kmer_length]
        print(kmer)
