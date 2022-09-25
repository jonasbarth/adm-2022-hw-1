"""Solves https://www.hackerrank.com/challenges/py-collections-deque?isFullScreen=true"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

if __name__ == '__main__':
    d = deque()
    method_calls = {}
    method_calls[d.append.__name__] = d.append
    method_calls[d.appendleft.__name__] = d.appendleft
    method_calls[d.pop.__name__] = d.pop
    method_calls[d.popleft.__name__] = d.popleft
    
    n_operations = int(input())
    
    for _ in range(n_operations):
        operation = list(input().split())
        if len(operation) > 1:
            argument = int(operation[-1])
            operation = operation[0]
            method_calls[operation](argument)
        
        else:
            method_calls[operation[0]]()
    
    print(' '.join(list(map(lambda item : str(item), d))))
