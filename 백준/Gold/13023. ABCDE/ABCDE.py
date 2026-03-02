import sys

input = sys.stdin.readline

def dfs():

    visited = [False] * N

    def backtrack(node, depth):
        
        if depth == 4:
            return 1
        
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                value = backtrack(next_node, depth + 1)
                visited[next_node] = False

                if value:
                    return 1

    for i in range(N):
        visited[i] = True
        result = backtrack(i, 0)
        visited[i] = False
    
        if result:
            return 1
    
    return 0


N, M = map(int, input().split())

graph = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = dfs()

print(result)