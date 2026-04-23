import sys
input = sys.stdin.readline
from collections import deque

C, R = map(int, input().split())
K = int(input())
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

k = 0
t = 0
b = 0
r = 0
l = 0
queue = deque([(0, 0, 1)])

if C * R < K:
    print(0)
else:
    k = 0
    c = 0
    r = 0
    while queue:
        i, j, v = queue.popleft()

        if v == K:
            print(i + 1, j + 1)
            break

        ni, nj = i + di[k], j + dj[k]

        if ni < 0 + t or ni >= C - b or nj < 0 + l or nj >= R - r:
            if k == 0:
                t += 1
            elif k == 1:
                r += 1
            elif k == 2:
                b += 1
            elif k == 3:
                l += 1
            k = (k + 1) % 4
            queue.append((i, j, v))
            continue

        else:
            v = v + 1
            queue.append((ni, nj, v))