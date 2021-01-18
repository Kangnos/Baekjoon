students_line = int(input())

for _ in range(students_line):
    count = 0
    students_score = list(map(int, input().split()))
    avg = sum(students_score[1:]) / students_score[0]
    for i in range(1,len(students_score)):
        if students_score[i] > avg:
            count += 1

    print(str('%.3f' % round(count / students_score[0] * 100, 3)) + "%")