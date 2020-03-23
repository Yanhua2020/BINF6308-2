#!/usr/bin/env python3
# transcribe.py
# Import Seq
from Bio.Seq import Seq
dna = Seq("AGTACACTGGTA")
rna = dna.transcribe()
print(rna)
