import sys
from collections import deque
input = sys.stdin.readline

C, R = map(int, input().split())
K = int(input())
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

arr = [[0] * R for _ in range(C)]
arr[0][0] = 1
queue = deque([(0, 0)])

if C * R < K:
    print(0)
else:
    k = 0
    while queue:
        i, j = queue.popleft()

        if arr[i][j] == K:
            print(i + 1, j + 1)
            break
    
        ni, nj = i + di[k], j + dj[k]

        if ni < 0 or ni >= C or nj < 0 or nj >= R:
            k = (k + 1) % 4
            queue.append((i, j))
            continue

        elif arr[ni][nj] != 0:
            k = (k + 1) % 4
            queue.append((i, j))
            continue

        if arr[ni][nj] == 0:
            arr[ni][nj] = arr[i][j] + 1
            queue.append((ni, nj))