"""Solves https://www.hackerrank.com/challenges/py-collections-namedtuple?isFullScreen=true"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

if __name__ == '__main__':
    
    n_students = int(input())
    marks_index = list(input().split()).index('MARKS')
    
    all_marks = [int(list(input().split())[marks_index]) for _ in range(n_students)]
        
    print(sum(all_marks) / len(all_marks))
        
        
