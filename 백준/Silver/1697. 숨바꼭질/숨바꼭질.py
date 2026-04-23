N, K = map(int, input().split())
visited = [0] * 100001
queue = [N]

while queue:
    N = queue.pop(0)

    if N == K:
        print(visited[N])
        break

    for j in [N - 1, N + 1, 2 * N]:
        if j > 100000 or j < 0:
            continue
        elif visited[j] == 0:
            visited[j] = visited[N] + 1
            queue.append(j)