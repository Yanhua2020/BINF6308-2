#!/usr/bin/env python3
# read_seq.py
from Bio import SeqIO
import re
for record in SeqIO.parse("/scratch/Drosophila/dmel-all-chromosome-r6.17.fasta", "fasta"):
        if re.match("^\d{1}\D*$", record.id):
                    seq = record.seq
                    print(record.id)
