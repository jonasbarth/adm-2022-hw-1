"""Solves https://www.hackerrank.com/challenges/collections-counter?isFullScreen=true"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

if __name__ == '__main__':
    n_shoes = int(input())
    shoe_sizes = Counter(list(map(int, input().split())))
    
    n_customers = int(input())

    money_earned = 0
    for _ in range(n_customers):
        wanted_size, price = list(map(int, input().split()))
        if shoe_sizes[wanted_size] > 0:
            money_earned += price
            shoe_sizes[wanted_size] -= 1
            
    print(money_earned)
