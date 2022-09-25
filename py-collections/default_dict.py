"""Solves https://www.hackerrank.com/challenges/defaultdict-tutorial?isFullScreen=true"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

def create_word_index_map(length):
    word_index_map = {}
    for i in range(length):
        word = input()
        try:
            word_index_map[word].append(i + 1)
        except KeyError:
            word_index_map[word] = [i + 1]

    return word_index_map

if __name__ == '__main__':
    n, m = tuple(map(int, input().split()))
   
    words_a_map = create_word_index_map(n)
    
    for _ in range(m):
        word_b = input()
        try:
            print(' '.join(list(map(str, words_a_map[word_b]))))
            
        except KeyError:
            print(-1)