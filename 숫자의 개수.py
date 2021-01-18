a = int(input())
b = int(input())
c = int(input())

k = a*b*c
k_list = list(str(k))

for i in range(0, 10):
    if str(i) in k_list:
        print(k_list.count(str(i)))
    else:
        print("0")