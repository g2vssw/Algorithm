import sys

input = sys.stdin.readline

# Union-Find

# 부모 노드를 찾는 함수 (경로 압축)
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 집합을 합치는 함수
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# N: 집의 개수, M: 도로의 개수
N, M = map(int, input().split())

# 모든 간선 정보를 담을 리스트
edges = []
for _ in range(M):
    u, v, cost = map(int, input().split())
    edges.append((cost, u, v))

# 1. 간선을 비용 순으로 오름차순 정렬 (크루스칼의 핵심)
edges.sort()

# 2. 부모 테이블 초기화 (자기 자신을 부모로)
parent = [i for i in range(N + 1)]

# 결과값과 MST에 포함된 간선 중 가장 큰 비용을 저장할 변수
total_cost = 0
last_edge_cost = 0

# 3. 간선을 하나씩 확인하며 MST 구축
for cost, u, v in edges:
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, u) != find_parent(parent, v):
        union_parent(parent, u, v)
        total_cost += cost
        # 비용 순으로 정렬되어 있으므로 마지막에 더해지는 값이 가장 큰 값임
        last_edge_cost = cost

# 4. 결과 출력
# 전체 MST 유지비에서 가장 비싼 간선 하나를 제거하여 마을을 두 개로 분리함
print(total_cost - last_edge_cost)