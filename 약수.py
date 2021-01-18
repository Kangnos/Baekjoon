from math import gcd

number1, number2 = map(int, input().split())

def lcm(x,y):
    return x * y // gcd(x, y)

print(gcd(number1, number2))
print(lcm(number1, number2))

