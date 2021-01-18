datacase = int(input()) # 문제 풀때 데이터 케이스의 10의 아홉은 int type임.

words = []

for i in range(datacase):
    word = str(input())
    word_count = len(word)
    words.append((word, word_count))

words = list(set(words))

words.sort(key= lambda word: (word[1], word[0]))


for word in words:
    print(word[0])