def bfs(i, j):
    global cnt
    if visited[i][j] == 1:
        return
    elif visited[i][j] == 0:
        queue = [(i, j)]
        visited[i][j] = 1
        cnt += 1


    Q = arr[i][j]
    while queue:
        i, j = queue.pop(0)

        for k in range(4):
            ni, nj = i + di[k], j + dj[k]

            if ni < 0 or ni >= N or nj < 0 or nj >= N:
                continue
            elif arr[ni][nj] != Q or visited[ni][nj] == 1:
                continue
            elif arr[ni][nj] == Q or visited[ni][nj] == 0:
                visited[ni][nj] = 1
                queue.append((ni, nj))

def bfs2(i, j):
    global cnt
    if visited[i][j] == 1:
        return
    elif visited[i][j] == 0:
        queue = [(i, j)]
        visited[i][j] = 1
        cnt += 1

    Q = arr[i][j]
    while queue:
        i, j = queue.pop(0)

        for k in range(4):
            ni, nj = i + di[k], j + dj[k]

            if ni < 0 or ni >= N or nj < 0 or nj >= N:
                continue
            elif arr[ni][nj] != Q or visited[ni][nj] == 1:
                if Q == "R" and arr[ni][nj] == "G" and visited[ni][nj] == 0:
                    visited[ni][nj] = 1
                    queue.append((ni, nj))
                elif Q == "G" and arr[ni][nj] == "R" and visited[ni][nj] == 0:
                    visited[ni][nj] = 1
                    queue.append((ni, nj))
                else:
                    continue
            elif arr[ni][nj] == Q or visited[ni][nj] == 0:
                visited[ni][nj] = 1
                queue.append((ni, nj))

N = int(input())
arr = [list(input()) for _ in range(N)]
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
queue = []
result = []

# 색맹X ------------------------

visited = [list(0 for _ in range(N)) for _ in range(N)]

cnt = 0

for i in range(N):
    for j in range(N):
        bfs(i, j)

result.append(cnt)

# 색맹O ------------------------

visited = [list(0 for _ in range(N)) for _ in range(N)]

cnt = 0

for i in range(N):
    for j in range(N):
        bfs2(i, j)

result.append(cnt)

print(*result)