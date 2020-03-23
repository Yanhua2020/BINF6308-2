#!/usr/bin/env python3
# translate.py
# Import Seq
from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
dna = Seq("AGTACACTGGTA")
rna = dna.transcribe()
protein = rna.translate()
idname=protein
protein_record =SeqRecord(rna,id=str(idname), description ="rna seq used as seqreading")
SeqIO.write(protein_record, "protein.fasta", "fasta")
