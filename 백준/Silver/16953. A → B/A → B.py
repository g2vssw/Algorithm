import sys
from collections import deque

input = sys.stdin.readline

A, B = map(int, input().split())

cnt = 1
while True:
    if B == A:
        break
    elif B < A:
        cnt = -1
        break

    if B % 2 == 0:
        B = B // 2
        cnt += 1
    else:
        if str(B)[-1] == "1":
            B = int(str(B)[:-1])
            cnt += 1
        else:
            cnt = -1
            break
print(cnt)