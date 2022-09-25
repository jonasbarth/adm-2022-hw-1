"""Solves https://www.hackerrank.com/challenges/word-order?isFullScreen=true"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

if __name__ == '__main__':
    n_words = int(input())
    
    distinct_word_count = OrderedDict()
    for _ in range(n_words):
        word = input().rstrip('\n')
        try:
            distinct_word_count[word] += 1
        except KeyError:
            distinct_word_count[word] = 1
            
    print(len(distinct_word_count))
    
    print(' '.join(list(map(lambda word_count : str(word_count[1]), distinct_word_count.items()))))
