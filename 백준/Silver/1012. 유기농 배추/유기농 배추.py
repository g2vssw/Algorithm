def bfs(i, j):
    global cnt

    if visited[i][j] == 1 or arr[i][j] == 0:
        return
    elif arr[i][j] == 1 and visited[i][j] == 0:
        visited[i][j] = 1
        cnt += 1

    queue = [(i, j)]

    while queue:
        i, j = queue.pop()

        for k in range(4):
            ni, nj = i + di[k], j + dj[k]

            if ni < 0 or ni >= N or nj < 0 or nj >= M:
                continue
            elif arr[ni][nj] == 0 or visited[ni][nj] == 1:
                continue
            visited[ni][nj] = 1
            queue.append((ni, nj))

T = int(input())

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

for _ in range(T):
    M, N, K = map(int, input().split())
    arr = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        arr[y][x] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            bfs(i, j)

    print(cnt)