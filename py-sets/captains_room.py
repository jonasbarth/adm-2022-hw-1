"""Solves https://www.hackerrank.com/challenges/py-the-captains-room/problem?isFullScreen=true"""
# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    group_size = int(input())
    room_numbers = list(map(int, input().split()))
    
    number_of_groups = (len(room_numbers) - 1) / group_size
    
    counts = {}
    
    for room_number in room_numbers:
        try:
            counts[room_number] += 1
        except KeyError:
            counts[room_number] = 1
            
    captain = list(filter(lambda elem: elem[1] == 1, counts.items()))
    
    print(captain[0][0])