# Problem: Grading Students - https://www.hackerrank.com/challenges/grading/problem

def gradingStudents(grades):
    result = []
    for grade in grades:
        next_multiple_of_five = ((grade//5) + 1)* 5
        if grade < 38:
            result.append(grade)
        elif next_multiple_of_five - grade < 3:
            result.append(next_multiple_of_five)
        else:
            result.append(grade)
    return result
        
            