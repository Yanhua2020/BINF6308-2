#!/usr/bin/env python
# if_else.py

# Iterate over a range of values
for num in range(1,10):
        # Use the modulo operator to get the remainder after division
        # If the remainder after dividing by 2 is zero, the number is even
        if num % 2 == 0:
            print(num)
            print('is even')
        else:
            print(num)
            print('is odd')
