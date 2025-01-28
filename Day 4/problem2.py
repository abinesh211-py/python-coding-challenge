#Given the names and grades for each student in a class of  students,
#  store them in a nested list and print the name(s) of any student(s) having the second lowest grade.


if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        
        name = input()
        score = float(input())
        students.append([name, score])
    grades = sorted(set([score for name, score in students]))
    second_lowest_grade = grades[1]
    second_lowest_students = [name for name, score in students if score == second_lowest_grade]
    second_lowest_students.sort()
    for name in second_lowest_students:
     print(name)
