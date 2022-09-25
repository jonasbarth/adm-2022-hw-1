"""Solves https://www.hackerrank.com/challenges/py-collections-ordereddict?isFullScreen=true"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

if __name__ == '__main__':
    n_items = int(input())
    
    items_to_prices = OrderedDict()
    
    for _ in range(n_items):
        item_and_price = list(input().split())
        item = ' '.join(item_and_price[:-1])
        price = int(item_and_price[-1])
        
        try:
            items_to_prices[item] += price
        except KeyError:
            items_to_prices[item] = price
            
    for item_price in items_to_prices:
        print(item_price, items_to_prices[item_price])
