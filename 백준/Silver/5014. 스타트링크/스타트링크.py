def bfs(node):
    queue = []

    queue.append(node)
    visited[node] = 1

    while queue:

        node = queue.pop(0)

        if node == G:
            print(visited[node] - 1)
            return

        for next_node in graph[node]:
            if visited[next_node] == 0:
                queue.append(next_node)
                visited[next_node] = visited[node] + 1

    print('use the stairs')
    return

F, S, G, U, D = map(int, input().split())
graph = [[] for _ in range(F + 1)]


for i in range(1, F + 1):
    if i + U > F:
        continue
    graph[i].append(i + U)

for j in range(1, F + 1):
    if j - D <= 0:
        continue
    graph[j].append(j - D)

visited = [0] * (F + 1)

bfs(S)