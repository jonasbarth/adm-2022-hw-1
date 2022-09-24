"""Solves https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true"""
def swap_case(s):
    new_string = []
    for char in s:
        if char.isupper():
            new_string.append(char.lower())
        elif char.islower():
            new_string.append(char.upper())
        else:
            new_string.append(char)
            
    return ''.join(new_string)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)