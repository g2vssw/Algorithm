def bfs(s):
    queue = [s]
    visited[s] = 1

    while queue:
        i = queue.pop()
        for n_i in graph[i]:
            if visited[n_i] == 0:
                visited[n_i] = i
                queue.append(n_i)

N = int(input())

graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
for _ in range(N-1):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

bfs(1)

for i in range(2, N + 1):
    print(visited[i])