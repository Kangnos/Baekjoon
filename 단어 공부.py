words = input().upper()
t = []
for i in set(words):
    t.append(words.count(i))

idx = [i for i, x in enumerate(t) if x == max(t)]

if len(idx) > 1:
    print("?")
else:
    print(list(set(words))[t.index(max(t))])