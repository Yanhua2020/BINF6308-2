#!/usr/bin/env python3
# readFastq.py
# Import Seq, SeqRecord, and SeqIO
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
# Import itertools to take a slice of list
import itertools
sequenceleft=[]
sequenceright=[]
readsequence=open("interleave.fasta",'w')
read_sampleleft = SeqIO.parse("/scratch/AiptasiaMiSeq/fastq/Aip02.R1.fastq", "fastq")
read_sampleright= SeqIO.parse("/scratch/AiptasiaMiSeq/fastq/Aip02.R2.fastq","fastq")
for sequence in read_sampleleft:
    sequenceleft.append(sequence.id)
    sequenceleft.append(sequence.seq)
for sequence in read_sampleright:
    sequenceright.append(sequence.id)
    sequenceright.append(sequence.seq)
for sequence in zip (sequenceleft,sequenceright):
    readsequence.write(str(sequence))



