def bfs(i, j):

    if arr[i][j] == 'W' or visited[i][j] == 1:
        return
    elif arr[i][j] == 'L' and visited[i][j] == 0:
        visited[i][j] = 1

    queue = [(i, j)]


    while queue:
        i, j = queue.pop(0)

        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if ni < 0 or ni >= L or nj < 0 or nj >= W:
                continue
            elif arr[ni][nj] == 'W' or visited[ni][nj] != 0:
                continue
            visited[ni][nj] = visited[i][j] + 1
            queue.append((ni, nj))

    return visited[i][j]

L, W = map(int, input().split())
arr = [list(input()) for _ in range(L)]
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
visited = [[0 for _ in range(W)] for _ in range(L)]
result = []
for i in range(L):
    for j in range(W):
        visited = [[0 for _ in range(W)] for _ in range(L)]
        bfs(i, j)
        max_value = 0
        for k in range(L):
            max_value = max(max(visited[k]) - 1, max_value)
        result.append(max_value)

print(max(result))