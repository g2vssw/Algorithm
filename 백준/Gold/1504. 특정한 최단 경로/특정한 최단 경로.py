import sys
import heapq # 최단 경로 탐색을 위한 우선순위 큐

input = sys.stdin.readline

INF = float('inf')

# 1. 입력 받기
N, E = map(int, input().split()) # 정점 개수, 간선 개수

adj = [[] for _ in range(N + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    # 양방향 그래프
    adj[u].append((v, w))
    adj[v].append((u, w))

# 반드시 거쳐야 하는 두 정점
v1, v2 = map(int, input().split())

# 2. 다익스트라 함수 정의
def dijkstra(start):
    distances = [INF] * (N + 1)
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        dist, current = heapq.heappop(pq)
        
        if distances[current] < dist:
            continue
            
        for next_node, weight in adj[current]:
            cost = dist + weight
            if cost < distances[next_node]:
                distances[next_node] = cost
                heapq.heappush(pq, (cost, next_node))
                
    return distances

# 3. 각 시작점으로부터의 최단 거리 계산
# 1번에서 출발하는 모든 최단 거리
dist_from_1 = dijkstra(1)
# v1에서 출발하는 모든 최단 거리
dist_from_v1 = dijkstra(v1)
# v2에서 출발하는 모든 최단 거리
dist_from_v2 = dijkstra(v2)

# 4. 두 가지 가능한 경로 합산
# path1: 1 -> v1 -> v2 -> N
path1 = dist_from_1[v1] + dist_from_v1[v2] + dist_from_v2[N]
# path2: 1 -> v2 -> v1 -> N
path2 = dist_from_1[v2] + dist_from_v2[v1] + dist_from_v1[N]

# 5. 결과 도출
result = min(path1, path2)

# 경로가 없는 경우 (INF보다 크거나 같을 때) -1 출력
if result >= INF:
    print(-1)
else:
    print(result)