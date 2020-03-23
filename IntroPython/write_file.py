#!/usr/bin/env python
# write_file.py
line_to_write = 'some text to write to the file'

# Open the file, and pass the 'w' parameter which means write to the file.
with open("out_file.txt", 'w') as  out:
        # Write the line of output
        out.write(line_to_write)

