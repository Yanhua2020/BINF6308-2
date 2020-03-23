#!/usr/bin/env pythoni3
# get_path.py
import subprocess
# Open the KEGG to KO mappings
kegg = open('kegg.txt')
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
            print(kegg_pathway)
            result = subprocess.call("curl http://rest.kegg.jp/link/pathway/ko:K04524" + kegg_pathway, stdout=out, stderr=err, shell=True)
