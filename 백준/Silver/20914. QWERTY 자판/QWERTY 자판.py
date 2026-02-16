import sys
from collections import deque

input = sys.stdin.readline

di = [-1, -1, 0, 1, 1, 0]
dj = [0, 1, 1, 0, -1, -1]

QWERTY = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]

def bfs(si, sj):

    st_i, st_j = si, sj
    time = 0
    for n in range(1, len(word)):
        visited = [[False] * 10 for _ in range(3)]
        visited[st_i][st_j] = True
        queue = deque([(st_i, st_j, 0)])
        s = word[n]
        while queue:
            ci, cj, m = queue.popleft()

            if arr[ci][cj] == s:
                time += m
                queue = deque([])
                st_i, st_j = ci, cj
                break

            for k in range(6):
                ni, nj = ci + di[k], cj + dj[k]
                if ni < 0 or ni >= 3 or nj < 0 or nj >= 10 or visited[ni][nj] == True:
                    continue
                visited[ni][nj] = True
                queue.append((ni, nj, m + 1))

    time *= 2
    time += len(word)

    return time

arr = []
for i in range(3):
    row = []
    for j in range(10):
        if len(QWERTY[i]) > j:
            row.append(QWERTY[i][j])
        else:
            row.append(0)
    arr.append(row)

T = int(input())

for _ in range(T):
    word = input().strip()
    result = 0
    for i in range(3):
        for j in range(10):
            if arr[i][j] == word[0]:
                result = bfs(i, j)
                break
        if result:
            break

    print(result)