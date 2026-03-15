import sys

input = sys.stdin.readline

coordinate = []
for _ in range(2):
    num = int(input())
    coordinate.append(num)

if coordinate[0] * coordinate[1] > 0:
    if coordinate[0] > 0:
        print(1)
    else:
        print(3)
else:
    if coordinate[0] > 0:
        print(4)
    else:
        print(2)