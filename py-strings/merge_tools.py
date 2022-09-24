"""Solves https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true"""
def merge_the_tools(string, k):
    # your code goes here
    substrings = [string[i:i+k] for i in range(0, len(string), k)]
    substrings = [set(list(s)) for s in substrings]
    
    for substring in substrings:
        print(''.join(substring))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)