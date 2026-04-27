import sys
from collections import deque

input = sys.stdin.readline

# 1. N(가수의 수), M(보조 PD의 수) 입력
N, M = map(int, input().split())

# 2. 그래프와 진입 차수 배열 초기화
adj = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)

# PD들이 가져온 순서를 바탕으로 간선 정보 생성
for _ in range(M):
    # PD가 정한 순서 정보 입력 (첫 번째 값은 가수의 수이므로 슬라이싱으로 제외)
    data = list(map(int, input().split()))
    singers = data[1:]
    
    # 연속된 두 가수의 앞뒤 관계를 그래프에 기록
    for i in range(len(singers) - 1):
        u, v = singers[i], singers[i+1]
        adj[u].append(v)   # u번 가수 다음에 v번 가수가 출연해야 함
        indegree[v] += 1   # v번 가수의 진입 차수 증가

# 3. 위상 정렬을 위한 큐 초기화
# 진입 차수가 0인(선행 조건이 없는) 모든 가수를 큐에 삽입
queue = deque()
for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)

# 결과를 저장할 리스트
result = []

# 4. 큐가 빌 때까지 반복하며 정렬 수행
while queue:
    current = queue.popleft()
    result.append(current)
    
    # 현재 출연한 가수와 연결된 다음 가수들의 진입 차수 감소
    for next_singer in adj[current]:
        indegree[next_singer] -= 1
        
        # 선행 출연진이 모두 정해졌다면 큐에 삽입
        if indegree[next_singer] == 0:
            queue.append(next_singer)

# 5. 결과 검증 및 출력
# 결과 리스트의 크기가 N이면 모든 가수의 순서를 정한 것 (성공)
if len(result) == N:
    for singer in result:
        print(singer)
# 크기가 N보다 작으면 사이클이 발생하여 순서를 정할 수 없는 상태 (실패)
else:
    print(0)