"""Solves https://www.hackerrank.com/challenges/designer-door-mat/problem?isFullScreen=true"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    height, width = input().split()
    height = int(height)
    width = int(width)
    
    n_rows = (height - 1) // 2
    
    rows = []
    for i in range(n_rows):
        middle = i * 2 * '..|'
        rows.append(f'.|{middle}.'.center(width, '-'))        
    
    for row in rows:
        print(row)
    print('WELCOME'.center(width, '-'))
    
    for row in rows[::-1]:
        print(row)