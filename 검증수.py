Computer_code = list(map(int, input().split()))


Z_Computer_code = []

for i in range(0, len(Computer_code)):
    Z_Computer_code.append(Computer_code[i] ** 2)

print(sum(Z_Computer_code)% 10)
