import sys
from collections import deque

input = sys.stdin.readline

di_q = [-1, -1, 0, 1, 1, 1, 0, -1]
dj_q = [0, 1, 1, 1, 0, -1, -1, -1]

di_k = [-2, -1, 1, 2, 2, 1, -1, -2]
dj_k = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs(si, sj):

    C = arr[si][sj]

    if C == 1:
        for k in range(8):
            cnt = 1
            while True:
                ni, nj = si + di_q[k] * cnt, sj + dj_q[k] * cnt
                if ni < 0 or ni >= N or nj < 0 or nj >= M or arr[ni][nj] in [1, 2, 3]:
                    break
                arr[ni][nj] = -1
                cnt += 1
    else:
        for k in range(8):
            ni, nj = si + di_k[k], sj + dj_k[k]
            if ni < 0 or ni >= N or nj < 0 or nj >= M or arr[ni][nj] != 0:
                continue
            arr[ni][nj] = -1

N, M = map(int, input().split())
Queen = list(map(int, input().split()))
Knight = list(map(int, input().split()))
Pawn = list(map(int, input().split()))

arr = [[0] * M for _ in range(N)]
chess = [Queen, Knight, Pawn]


for i in range(3):
    if chess[i][0] == 0:
        continue
    for k in range(1, len(chess[i]), 2):
        ni, nj = chess[i][k] - 1, chess[i][k + 1] - 1
        arr[ni][nj] = i + 1

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0 or arr[i][j] == -1 or arr[i][j] == 3:
            continue
        bfs(i, j)

result = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            result += 1

print(result)