"""Solves https://www.hackerrank.com/challenges/most-commons/problem?isFullScreen=true"""
#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import islice

if __name__ == '__main__':
    s = input()
    char_count = {}
    for char in s:
        try:
            char_count[char] += 1
        except KeyError:
            char_count[char] = 1
            
    sorted_char_count = {char: count for char, count in sorted(char_count.items(), key=lambda item: item[1], reverse=True)}
    top_three = dict(islice(sorted_char_count.items(), 3))
    
    chars_with_same_value = [char ]
    for char, count in top_three.items():
        print(char, count)
