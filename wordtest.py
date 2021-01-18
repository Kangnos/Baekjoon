import time

wordsnumbers = int(input())

english_voca_list = []

for i in range(wordsnumbers):
    engword = str(input())
    english_voca_list.append(engword)
    Koreanmeaning = str(input())
    english_voca_list.append(Koreanmeaning)

print(english_voca_list)

time.sleep(1)

print("\n단어 테스트 시작!")

