import sys
from collections import deque

input = sys.stdin.readline

def bfs(start_node):

    if len(graph[start_node]) == 0:
        return 1
    
    visited = [0] * (N + 1)
    visited[start_node] = 1
    queue = deque([start_node])

    cnt = 1
    while queue:
        node = queue.popleft()

        for next_node in graph[node]:
            if visited[next_node]:
                continue
            visited[next_node] = 1
            cnt += 1
            queue.append(next_node)
    
    return cnt

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[B].append(A)

result = []
max_hacking = 1
for i in range(1, N + 1):
    value = bfs(i)
    if max_hacking < value:
        max_hacking = value
        result = [i]
    elif max_hacking == value:
        result.append(i)

print(" ".join(map(str, result)))