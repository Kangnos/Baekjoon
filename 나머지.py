numbers = [int(input()) for i in range(10)]
else_numbers = []


for i in range(len(numbers)):
    else_numbers.append(numbers[i] % 42)

print(len(set(else_numbers)))