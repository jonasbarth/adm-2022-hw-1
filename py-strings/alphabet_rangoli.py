"""Solves https://www.hackerrank.com/challenges/alphabet-rangoli/problem?isFullScreen=true"""
import string

def print_rangoli(size):
    # your code goes here
    alphabet = string.ascii_lowercase
    n_rows = size
  
    
    rows = []
    for n in range(1, n_rows + 1):
        before = alphabet[size - 1:size - n:-1]
        after = before[::-1]
        
        start_char = alphabet[size - n]
        full = before + start_char + after
        
        rows.append('-'.join(list(full)).center(size * 4 - 3, '-'))
        
        
    for row in rows:
        print(row)
        
    for row in rows[::-1][1:]:
        print(row)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)