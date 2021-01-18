# a = int(input())

# if a == 1:
#     print("*")

# for _ in range(a):
#     if a % 2 == 0:
#         print("* " * (a // 2))
#         print(" *" * (a // 2))
#     else:
#         print("* " * (a // 2) + "*")
#         print(" *" * (a // 2))


N = int(input())

odd = N - N//2  
even = N//2

for i in range(N):
    print("* " * odd)
    print(" *" * even)