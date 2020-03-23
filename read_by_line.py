#!/usr/bin/env python
# read_by_line.py
import re
import os


# Open a sample fastq file for reading
read_sample = open('/scratch/SampleDataFiles/Sample.R1.fastq', 'r')

# Initialize a variable to contain the lines
line = ' '

# While line is not empty
while line:
        # Read one line from the file using the readline() method
            line = read_sample.readline()
            line = line.rstrip(os.linesep)
            if re.match('^[ATGCN]+$', line):
            # Print the line
                print(line)

                    # Close the file using the close() method
