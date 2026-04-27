import sys
from collections import deque

input = sys.stdin.readline

# 1. 입력 받기
# N: 학생 수, M: 비교 횟수
N, M = map(int, input().split())

# 2. 그래프 및 진입 차수 배열 초기화
# adj: 인접 리스트 (A -> B 관계 저장)
# indegree: 각 노드로 들어오는 간선의 개수
adj = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)

for _ in range(M):
    A, B = map(int, input().split())
    adj[A].append(B) # A 다음에 B가 서야 함
    indegree[B] += 1 # B 입장에서는 앞에 서야 할 사람이 한 명 추가됨

# 3. 위상 정렬 수행을 위한 큐 초기화
# 진입 차수가 0인(내 앞에 아무도 없는) 노드를 모두 큐에 삽입
queue = deque()
for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)

# 결과를 담을 리스트
result = []

# 4. 큐가 빌 때까지 반복
while queue:
    # 큐에서 노드를 꺼내 결과 리스트에 추가 (줄 세우기)
    current = queue.popleft()
    result.append(current)
    
    # 해당 학생 뒤에 서야 하는 학생들을 확인
    for next_student in adj[current]:
        # 앞 사람이 줄을 섰으므로 진입 차수 1 감소
        indegree[next_student] -= 1
        
        # 이제 내 앞에 아무도 없다면(진입 차수 0) 큐에 삽입
        if indegree[next_student] == 0:
            queue.append(next_student)

# 5. 결과 출력 (공백으로 구분하여 한 줄에 출력)
print(*(result))