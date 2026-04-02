X = int(input())

N = int(input())

value = 0
for _ in range(N):
    a, b = map(int, input().split())
    value += (a * b)

if X == value:
    print("Yes")
else:
    print("No")