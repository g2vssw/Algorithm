import sys

input = sys.stdin.readline

result1 = 0
result2 = 0
for i in range(3):
    num = int(input())
    if i == 0:
        result1 += num
        result2 += num
    elif i == 1:
        result1 += num
        result2 = int(str(result2) + str(num))
    else:
        result1 -= num
        result2 -= num

print(result1)
print(result2)