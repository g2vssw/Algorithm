def dfs(node):
    ans_dfs.append(node)                  # 방문 노드 추가
    visited[node] = 1                     # 방문 표시

    for next_node in graph[node]:
        if visited[next_node] == 0:       # == if not visited[next_node]: / 방문하지 않은 노드인 경우
            dfs(next_node)


def bfs(node):
    queue = []                            # 필요한 queue, visited, 변수 생성

    queue.append(node)                    # queue에 초기 데이터(들) 삽입
    ans_bfs.append(node)
    visited[node] = 1

    while queue:
        node = queue.pop(0)
        for next_node in graph[node]:
            if visited[next_node] == 0:     # 방문하지 않은 노드 -> 큐 삽입
                queue.append(next_node)
                ans_bfs.append(next_node)
                visited[next_node] = 1

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)  # 양방향

# 오름차순 정렬
for i in range(1, N + 1):
    graph[i].sort()

visited = [0] * (N + 1)
ans_dfs = []
dfs(V)

visited = [0] * (N + 1)
ans_bfs = []
bfs(V)

print(*ans_dfs)
print(*ans_bfs)