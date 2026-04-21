from collections import deque

def bfs(start):
    queue = deque(start)

    while queue:
        i, j, p = queue.popleft()

        if visited[i][j] == 0:
            visited[i][j] = 1

        if i == ei and j == ej:
            print(visited[ei][ej] - 1)
            break

        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if ni < 0 or ni >= R or nj < 0 or nj >= C:
                continue
            elif arr[ni][nj] == 'X' or visited[ni][nj] != 0:
                continue
            elif visited[ni][nj] == 0:
                if p == '*':
                    if arr[ni][nj] == 'D' or arr[ni][nj] == '*':
                        continue
                    elif arr[ni][nj] == '.' or arr[ni][nj] == 'S':
                        arr[ni][nj] = '*'
                        visited[ni][nj] = 1
                        queue.append((ni, nj, p))
                elif p == 'S':
                    if arr[ni][nj] == '*':
                        continue
                    elif arr[ni][nj] == '.' or arr[ni][nj] == 'D':
                        arr[ni][nj] = 'S'
                        visited[ni][nj] = visited[i][j] + 1
                        queue.append((ni, nj, p))

    if visited[ei][ej] == 0:
        return print("KAKTUS")
    else:
        return

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
visited = [[0 for _ in range(C)] for _ in range(R)]

start = deque()
for i in range(R):
    for j in range(C):
        if arr[i][j] == '*':
            start.append((i, j, '*'))

for i in range(R):
    for j in range(C):
        if arr[i][j] == 'D':
            ei, ej = i, j
        elif arr[i][j] == 'S':
            start.append((i, j, 'S'))

bfs(start)