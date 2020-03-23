#!/usr/bin/env python
# get_all_kmers.py
seq = 'GCCGGCCCTCAGACAGGAGTGGTCCTGGATG'
kmer_length = 7
stop = len(seq) - kmer_length + 1
for start in range(0, stop):
          kmer = seq[start:start + kmer_length]
          print(kmer)
