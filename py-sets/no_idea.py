"""Solves https://www.hackerrank.com/challenges/no-idea/problem?isFullScreen=true"""
# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    a = set(map(int, input().split()))
    b = set(map(int, input().split()))
    
    happiness = 0
    
    seen = set()
    for i in arr:
        if i in a:
            happiness += 1
        elif i in b:
            happiness -= 1
    print(happiness)