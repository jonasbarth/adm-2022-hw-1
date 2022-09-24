"""Solves https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=true"""
def print_formatted(number):
    bin_len = len(format(number, "b"))
    for i in range(1, number + 1):
        # your code goes here
        dec = format(i, "d")
        octal = format(i, "o")
        hexa = format(i, "X")
        binary = format(i, "b")
      
        print(f'{dec.rjust(bin_len)} {octal.rjust(bin_len)} {hexa.rjust(bin_len)} {binary.rjust(bin_len)}')

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)