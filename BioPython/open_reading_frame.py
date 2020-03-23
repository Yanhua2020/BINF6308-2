#!/usr/bin/env python3
#find open reading frame
import re
# Initialize an RNA sequence to test the regular expression
rna = 'GGUCCGGGAUGCCUGAAUGGUACACUGGUAAGUACACUGUAAGUAAAAAAAA'
# Search for AUG followed by any character one or more times.
result = re.search('AUG([AUGC]{3})+?(UAA|UAG|UGA)', rna)
# Use the type function to see what re.search() returns.
print(type(result))
# Use the group() method of the match object to get the matching string
orf = result.group()
# Print the matching string
print(orf)
