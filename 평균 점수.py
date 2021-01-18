s = 0
n = int(input("과목의 갯수를 입력하세요>> "))

for _ in range(1, n+1):
    score = float(input("%d번째 과목의 점수를 입력하세요" % (n)))
    s += score
print("총점수는 %d점입니다." % (s))
print("평균점수는 %d점입니다." % (s / n))
    