#!/usr/bin/env python
import re
dmel_genome_path = '/scratch/Drosophila/dmel-all-chromosome-r6.17.fasta'
headers_count = 0;
line_count = 0;
with open ("dmel_headers.txt", 'w') as out:
     with open(dmel_genome_path) as dmel_genome:
            for line in dmel_genome:
                line_count += 1
                if re.match('^>', line):
                    headers_count += 1
                    if headers_count <51:
                       out.write(line)


