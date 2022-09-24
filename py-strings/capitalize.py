"""Solves https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    result = []

    previous_char = ' '
    for char in list(s):
        if char.isalpha() and previous_char == ' ':
            result.append(f'{char.upper()}')
        else:
            result.append(char)
        
        previous_char = char
         
    return ''.join(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
