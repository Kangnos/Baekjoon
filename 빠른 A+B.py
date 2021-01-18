import sys

i = int(input())

for x in range(i):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)
