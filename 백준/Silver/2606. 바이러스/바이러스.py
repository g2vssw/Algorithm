def bfs(node):
    queue = [node]

    while queue:
        node = queue.pop()

        for next_node in graph[node]:
            if visited[next_node] == 1:
                continue
            visited[next_node] = 1
            queue.append(next_node)

N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)


for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N + 1):
    graph[i].sort()

visited[1] = 1
bfs(1)

cnt = 0
for i in range(N + 1):
    if visited[i] == 1:
        cnt += 1

print(cnt - 1)