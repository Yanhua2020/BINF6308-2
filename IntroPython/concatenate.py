#!/usr/bin/env python
# concatenate.py

# Iterate over a range of values
for num in range(1,10):
        # Use the modulo operator to get the remainder after division
            # If the remainder after dividing by 2 is zero, the number is even
                if num % 2 == 0:
                            print(str(num) + ' is even')
                else:
                            print(str(num) + ' is odd')
