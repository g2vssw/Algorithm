def dfs(node):
    if node == b:
        return

    for next_node in graph[node]:
        if visited[next_node] == 0:
            visited[next_node] = visited[node] + 1
            dfs(next_node)

n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

for s in range(1, n + 1):
    graph[s].sort()

visited = [0] * (n + 1)
cnt = 0
visited[a] = 1
dfs(a)

print(visited[b]-1)