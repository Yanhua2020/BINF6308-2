#!/usr/bin/env python3

# get_path.py
import subprocess
# Open the  KO 
kegg = open('ko.txt')
kegg_pathway = {}
# Open files for stdout and stderr
out = open('koPathway.txt','w')
err = open('koPathway.err','w')
# Iterate over lines of KEGG pathway
for kegg_line in kegg:
        # Remove line terminator
            kegg_line = kegg_line.rstrip()
        # Split line on whitespace
            fields = kegg_line.split()
            if len(fields) > 1:
                 kegg = fields[1]
                 kegg_pathway[kegg] = 1
for kegg_pathway in kegg_pathway:
           
            result = subprocess.call("curl http://rest.kegg.jp/link/pathway/" + kegg_pathway, stdout=out, stderr=err, shell=True)
