#!/usr/bin/env python3
# read_print.py
# Create a file object named read_sample
read_sample = open('/scratch/SampleDataFiles/Sample.R1.fastq', 'r')
# Call the .readline() method to get one line from the file
line = read_sample.readline()
print(line)
