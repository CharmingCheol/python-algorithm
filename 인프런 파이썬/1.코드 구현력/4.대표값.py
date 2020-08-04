from sys import stdin

students = int(stdin.readline())
scores = list(map(int, stdin.readline().split()))
average = round(sum(scores) / students)

student_score = scores[0]
student_index = 0
for (index, value) in enumerate(scores):
    if abs(average - student_score) > abs(average - value):
        student_score = value
        student_index = index
    if abs(average - student_score) >= abs(average - value) and student_score < value:
        student_score = value
        student_index = index
print(average, student_index + 1)