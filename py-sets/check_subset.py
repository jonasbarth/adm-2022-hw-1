"""Solves https://www.hackerrank.com/challenges/py-check-subset/problem?isFullScreen=true"""
# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    n_test_cases = int(input())
    
    for _ in range(n_test_cases):
        n_elements_a = int(input())
        a = set(map(int, input().split()))
        n_elements_b = int(input())
        b = set(map(int, input().split()))
        
        print(a.issubset(b))