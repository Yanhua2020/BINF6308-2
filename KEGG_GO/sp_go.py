#!/usr/bin/env python3
# sp_go.py
# Open the output file for writing
subset = open("sp_go.txt", "w")
# Open the UniProt to GO Mapping file
sp = open("/scratch/SampleDataFiles/goa_uniprot_all.gaf")
# Iterate over lines
for line in sp:
        # Split on tabs
    fields = line.split("\t")
        # Check for 6 columns
    if len(fields) > 4:
       # Write columns 2 and 5
       subset.write(fields[1] + "\t" + fields[4] + "\n")
