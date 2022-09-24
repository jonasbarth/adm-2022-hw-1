# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    n_english = int(input())
    roll_english = set(map(int, input().split()))
    
    n_french = int(input())
    roll_french = set(map(int, input().split()))
    
    print(len(roll_english.symmetric_difference(roll_french)))