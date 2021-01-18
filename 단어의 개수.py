sentence = input()

if sentence == '':
    print("0")
else:
    words = sentence.split(' ')
    while '' in words:
        words.remove('')
    print(len(words))