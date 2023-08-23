### 국영수
import sys

input = sys.stdin.readline

# 도현이네 반의 학생 수 N
n = int(input().rstrip())

# 학생의 이름, 국어, 영어, 수학 점수
students = []
for _ in range(n):
    students.append(input().split())

# 선택 정렬 - 가장 작은 것을 선택해서 앞쪽에 둔다
# 국어 정렬
idx = 0
counted_student = []
current_min_student = []
sorted_students = []
for s in students:

for i in len(students):
    for j in len(students):
        if students[j] not in counted_student:
            if students[i][1] < students[j][1]:
                current_min_student = students[i]
            elif
        sorted_students.append(current_min_student)
        counted_student.append(current_min_student)


"""
입력값
12
Junkyu 50 60 100
Sangkeun 80 60 50
Sunyoung 80 70 100
Soong 50 60 90
Haebin 50 60 100
Kangsoo 60 80 100
Donghyuk 80 60 100
Sei 70 70 70
Wonseob 70 70 90
Sanghyun 70 70 80
nsj 80 80 80
Taewhan 50 60 90
"""