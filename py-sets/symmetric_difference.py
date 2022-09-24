"""Solves https://www.hackerrank.com/challenges/symmetric-difference/problem?isFullScreen=true"""
# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    n1 = int(input())
    arr1 = set(map(int, input().split()))
    
    n2 = int(input())
    arr2 = set(map(int, input().split()))
    
    for n in sorted(arr1.difference(arr2).union(arr2.difference(arr1))):
        print(n)