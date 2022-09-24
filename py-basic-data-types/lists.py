"""Solves https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true"""
if __name__ == '__main__':
    N = int(input())

    arr = []
    for _ in range(N):
        command_input = input().split()
        command_name = command_input[0]
        
        if command_name == 'insert':
            arr.insert(int(command_input[1]), int(command_input[2]))
        elif command_name == 'print':
            print(arr)
        elif command_name == 'remove':
            arr.remove(int(command_input[1]))
        elif command_name == 'append':
            arr.append(int(command_input[1]))
        elif command_name == 'sort':
            arr.sort()
        elif command_name == 'pop':
            arr.pop()
        elif command_name == 'reverse':
            arr.reverse()