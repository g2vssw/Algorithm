import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def dfs(node):
    
    if len(graph[node]) == 0:
        return
    
    for next_node in graph[node]:
        path.append(next_node)
        dfs(next_node)

T = int(input())

for _ in range(T):
    N = int(input())
    graph = [[] for _ in range(N + 1)]

    for _ in range(N - 1):
        A, B = map(int, input().split())
        graph[B].append(A)

    N1, N2 = map(int, input().split())

    path = [N1]
    dfs(N1)
    result1 = path
    path = [N2]
    dfs(N2)
    result2 = path

    result = 0
    for r1 in result1:
        for r2 in result2:
            if r1 == r2:
                result = r1
                break
        if result:
            break

    print(result)