"""Solves https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true"""
#!/bin/python3

import math
import os
import random
import re
import sys

        
def is_odd(n):
    return n % 2 == 1

def is_in_inclusive_range(start, end, n):
    return n in range(start, end + 1)



if __name__ == '__main__':
    n = int(input().strip())
    if is_odd(n):
        print("Weird")
        sys.exit()

    if is_in_inclusive_range(2, 5, n):
        print("Not Weird")
        
    if is_in_inclusive_range(6, 20, n):
        print("Weird")
        
    if n > 20:
        print("Not Weird")