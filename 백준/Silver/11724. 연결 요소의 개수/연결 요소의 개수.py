import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(node):
    visited[node] = 1

    for next_node in graph[node]:
        if visited[next_node] == 0:
            dfs(next_node)

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
cnt = 0

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N + 1):
    graph[i].sort()

for i in range(1, N + 1):
    if visited[i] == 0:
        dfs(i)
        cnt += 1
    else:
        continue

print(cnt)