# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    n_elements_a = int(input())
    a = set(map(int, input().split()))
    
    n_other_sets = int(input())
    
    operations = {a.update.__name__: a.update, a.intersection_update.__name__: a.intersection_update, a.difference_update.__name__: a.difference_update, a.symmetric_difference_update.__name__: a.symmetric_difference_update}
    
    for _ in range(n_other_sets):
        op_name, set_length = input().split()
        other_set = set(map(int, input().split()))
        
        operations[op_name](other_set)    
        
    print(sum(a))