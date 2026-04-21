import sys
input = sys.stdin.readline
import copy
from collections import deque


def bfs():
    global result
    queue = deque()
    defense_arr = copy.deepcopy(arr)

    for i in range(N):
        for j in range(M):
            if defense_arr[i][j] == 2:
                queue.append((i, j))

    while queue:
        i, j = queue.popleft()

        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if ni < 0 or ni >= N or nj < 0 or nj >= M:
                continue
            if defense_arr[ni][nj] != 0:
                continue
            defense_arr[ni][nj] = 2
            queue.append((ni, nj))

    cnt = 0
    for q in range(N):
        for w in range(M):
            if defense_arr[q][w] == 0:
                cnt += 1

    result = max(result, cnt)


def defense(cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                arr[i][j] = 1
                defense(cnt + 1)
                arr[i][j] = 0

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

result = 0
defense(0)

print(result)