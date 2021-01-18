alphabet = "abcdefghijklnmopqrstuvwxyz"
word = str(input())
position = []

print(len(word))

for i in range(len(word)):
    if word[i] in alphabet:
        position.append(word.count(word[i]))
    else: 
        position.append("-1")

print(position)

print(len(alphabet))