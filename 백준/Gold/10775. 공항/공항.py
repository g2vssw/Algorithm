import sys

# 재귀 한도 늘리기 (Union-Find의 깊이가 깊어질 수 있음)
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

# 부모 노드를 찾는 함수 (경로 압축 포함)
# 이 함수를 통해 현재 게이트에서 사용 가능한 가장 번호가 큰 게이트를 바로 찾음
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 게이트를 연결하는 함수
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 1. 입력 받기
G = int(input()) # 게이트의 수
P = int(input()) # 비행기의 수

# 2. 부모 테이블 초기화 (0번 게이트는 폐쇄를 의미하는 더미 게이트)
parent = [i for i in range(G + 1)]

# 도킹 성공한 비행기 수
count = 0

# 3. 비행기를 하나씩 도킹 시도
for _ in range(P):
    gi = int(input())
    
    # 현재 gi 이하의 게이트 중 도킹 가능한 가장 큰 번호의 게이트를 찾음
    available_gate = find_parent(parent, gi)
    
    # 4. 도킹 가능 여부 확인
    # 찾은 게이트가 0이면 더 이상 들어갈 자리가 없음
    if available_gate == 0:
        break
    
    # 도킹 성공: 해당 게이트를 바로 왼쪽(available_gate - 1) 게이트와 합침
    # 이제 누군가 이 게이트를 찾으러 오면 자동으로 왼쪽 빈칸으로 안내됨
    union_parent(parent, available_gate, available_gate - 1)
    count += 1

# 5. 결과 출력
print(count)