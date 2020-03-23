#!/usr/bin/env python3
# format.py
num_bases = 50000
chrom = '2L'
another_variable = 'Joanna Lumley'
# Create the template
template = "Chromosome {} has {:,} bases. Put another variable here, like Chuck's favorite comic actress {}"
# Print the formatted output
print(template.format(chrom, num_bases, another_variable))
