# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n_elements_s = int(input())
    
    s = set(map(int, input().split()))
    
    n_commands = int(input())
    
    for _ in range(n_commands):
        command_input = input().split()
        command = command_input[0]
        if command == 'pop':
            try:
                s.pop()
            except KeyError:
                continue
        elif command == 'remove':
            try:
                s.remove(int(command_input[1]))
            except KeyError:
                continue
        elif command == 'discard':
            s.discard(int(command_input[1]))

    print(sum(s))