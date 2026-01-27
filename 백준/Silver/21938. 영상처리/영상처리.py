import sys
from collections import deque

input = sys.stdin.readline

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

N, M = map(int, input().split())

raw_arr = [list(map(int, input().split())) for _ in range(N)]

T = int(input())

arr = [[0] * M for _ in range(N)]

for i in range(N):
     for j in range(M):
        mean =  (raw_arr[i][j * 3] + raw_arr[i][j * 3 + 1] + raw_arr[i][j * 3 + 2]) / 3
        if mean >= T:
            arr[i][j] = 255
        else:
            arr[i][j] = 0

cnt = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 255:
            cnt += 1
            arr[i][j] = 0
            queue = deque([(i, j)])
            while queue:
                ci, cj = queue.popleft()

                for k in range(4):
                    ni, nj = ci + di[k], cj + dj[k]
                    if ni < 0 or ni >= N or nj < 0 or nj >= M or arr[ni][nj] != 255:
                        continue
                    arr[ni][nj] = 0
                    queue.append((ni, nj))

print(cnt)