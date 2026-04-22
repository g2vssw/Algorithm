def dfs(node):
    for next_node in range(N):
        if arr[node][next_node] == 1 and visited[next_node] == 0:
            visited[next_node] = 1
            dfs(next_node)

N = int(input())

arr = [list(map(int, input().split())) for i in range(N)]

result = []
for i in range(N):
    visited = [0] * N
    dfs(i)
    result.append(visited)

for r in result:
    print(*r)