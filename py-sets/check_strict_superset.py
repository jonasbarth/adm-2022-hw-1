"""Solves https://www.hackerrank.com/challenges/py-check-strict-superset/problem?isFullScreen=true"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    a = set(map(int, input().split()))
    n = int(input())
    
    result = True
    for _ in range(n):
        other_set = set(map(int, input().split()))
        is_strict_superset = a.issuperset(other_set) and len(a.difference(other_set)) > 0
        result = result and is_strict_superset
        
    print(result)