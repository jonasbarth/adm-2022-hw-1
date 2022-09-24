"""Solves https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true"""
        
def has_alnum(string):
    return True in [char.isalnum() for char in string]

def has_alpha(string):
    return True in [char.isalpha() for char in string]
        
def has_digit(string):
    return True in [char.isdigit() for char in string]

def has_lower(string):
    return True in [char.islower() for char in string]
        
def has_upper(string):
    return True in [char.isupper() for char in string]
        

if __name__ == '__main__':
    s = input()
    
    results = [has_alnum(s), has_alpha(s), has_digit(s), has_lower(s), has_upper(s)]
    
    for result in results:
        print(result)