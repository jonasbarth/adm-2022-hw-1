"""Solves https://www.hackerrank.com/challenges/the-minion-game/problem"""
from itertools import combinations
from functools import reduce

def minion_game(string):
    # your code goes here
    res = [string[i:j] for i, j in combinations(range(len(string) + 1), r = 2)]
    
    vowels = ['A', 'E', 'I', 'O', 'U']
    
    kevin_words = list(filter(lambda string: string[0] in vowels, res))
    kevin_count = {word : kevin_words.count(word) for word in kevin_words}
    kevin_total = reduce(lambda a, b : a + b, kevin_count.values())
    
    stuart_words = list(filter(lambda string: string[0] not in vowels, res))
    stuart_count = {word : stuart_words.count(word) for word in stuart_words}
    stuart_total = reduce(lambda a, b : a + b, stuart_count.values())
    
    if stuart_total > kevin_total:
        print(f"Stuart {stuart_total}")
    elif kevin_total < stuart_total:
        print(f"Kevin {kevin_total}")
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)   

