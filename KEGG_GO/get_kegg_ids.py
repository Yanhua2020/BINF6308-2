#!/usr/bin/env python3
# get_kegg_ids.py
import subprocess
# Open the BLAST output
blast_output = open('../BLAST/alignPreicted.txt')
# Open files for stdout and stderr
out = open('kegg.txt','w')
err = open('kegg.err','w')
# Iterate over lines of BLAST output
for blast_line in blast_output:
        # Remove line terminator
    blast_line = blast_line.rstrip()
      # Split line on whitespace
    fields = blast_line.split()
    sp = fields[1]
    evalue = fields[7]
    print(sp + "\t" + evalue)
   # Check for e-value less than 1e-180
    if float(fields[7]) < float("1e-180"):
   # Call the KEGG API
       result = subprocess.call("curl http://rest.kegg.jp/conv/genes/uniprot:" + sp, 
       stdout=out, stderr=err, shell=True)
