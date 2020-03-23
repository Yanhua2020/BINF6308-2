#!/usr/bin/env python
# format.py

# Iterate over a range of values
for num in range(1,10):
        # Use the modulo operator to get the remainder after division
        # If the remainder after dividing by 2 is zero, the number is even
        if num % 2 == 0:
            print("{} is even".format(num))
        else:
            print("{} is odd".format(num))
