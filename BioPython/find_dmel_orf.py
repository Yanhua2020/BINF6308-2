#!/usr/bin/env python3
# find_dmel_orf.py
from Bio import SeqIO
import re
from Bio.Seq import Seq

for record in SeqIO.parse("/scratch/Drosophila/dmel-all-chromosome-r6.17.fasta", "fasta"):
        if re.match("^\d{1}\D*$", record.id):
             dna = record.seq
             rna = dna. transcribe()
             result = re.search('AUG([AUGC]{3})+?(UAA|UAG|UGA)', str(rna))
             orf = result.group()
             protein = Seq(orf).translate()
             print (protein)
