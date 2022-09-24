"""Solves https://www.hackerrank.com/challenges/nested-list/problem"""
if __name__ == '__main__':
    students = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        
    students.sort(key = lambda student: student[1])
    lowest_score = students[0][1]
    
    lowest_removed = list(filter(lambda student: student[1] > lowest_score, students))

    new_lowest_score = lowest_removed[0][1]
    
    second_lowest_scores = list(filter(lambda student: student[1] == new_lowest_score, lowest_removed))
    
    second_lowest_scores.sort(key = lambda student: student[0])
    
    for student in second_lowest_scores:
        print(student[0])
