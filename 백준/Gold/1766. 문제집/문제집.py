import sys
import heapq # 우선순위 큐(최소 힙)를 위해 사용

input = sys.stdin.readline

# 1. N(문제의 수), M(선후 관계 정보의 수) 입력
N, M = map(int, input().split())

# 2. 그래프와 진입 차수 배열 초기화
# adj: 특정 문제를 풀고 나서 풀 수 있는 다음 문제들의 리스트
# indegree: 특정 문제를 풀기 위해 먼저 풀어야 하는 문제의 개수
adj = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)

for _ in range(M):
    # A번 문제는 B번 문제보다 먼저 풀어야 함 (A -> B)
    A, B = map(int, input().split())
    adj[A].append(B)
    indegree[B] += 1

# 3. 위상 정렬을 위한 우선순위 큐(최소 힙) 초기화
# 진입 차수가 0인(지금 바로 풀 수 있는) 모든 문제를 힙에 삽입
# heapq는 기본적으로 최소 힙이므로 번호가 작은 문제가 먼저 나옴
pq = []
for i in range(1, N + 1):
    if indegree[i] == 0:
        heapq.heappush(pq, i)

# 결과를 저장할 리스트
result = []

# 4. 힙이 빌 때까지 반복하며 정렬 수행
while pq:
    # 현재 풀 수 있는 문제 중 번호가 가장 작은 것을 꺼냄
    current = heapq.heappop(pq)
    result.append(current)
    
    # 해당 문제를 풀었으므로, 이 문제와 연결된 다음 문제들을 확인
    for next_problem in adj[current]:
        # 선행 문제 조건이 하나 해결되었으므로 진입 차수 감소
        indegree[next_problem] -= 1
        
        # 이제 선행 문제를 모두 풀었다면(진입 차수 0) 힙에 삽입
        if indegree[next_problem] == 0:
            heapq.heappush(pq, next_problem)

# 5. 결과 출력 (공백으로 구분하여 한 줄에 출력)
print(*(result))