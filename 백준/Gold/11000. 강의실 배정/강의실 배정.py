import sys
import heapq # 강의실 종료 시간을 관리하기 위한 우선순위 큐

input = sys.stdin.readline

# 1. N(수업의 개수) 입력
N = int(input())

# 2. 수업 시간 정보 입력 및 시작 시간 기준 정렬
# (시작 시간, 종료 시간) 순으로 리스트에 저장
lectures = []
for _ in range(N):
    lectures.append(list(map(int, input().split())))

# 시작 시간 기준으로 정렬해야 순차적으로 강의실 배정이 가능함
lectures.sort()

# 3. 우선순위 큐(최소 힙) 초기화
# 첫 번째 수업이 끝나는 시간을 힙에 넣으며 시작
# pq는 현재 사용 중인 강의실들의 '종료 시간'을 담고 있음
pq = []
heapq.heappush(pq, lectures[0][1])

# 4. 두 번째 수업부터 하나씩 확인
for i in range(1, N):
    start, end = lectures[i]
    
    # 만약 현재 수업의 시작 시간이 가장 빨리 끝나는 강의실의 종료 시간보다 크거나 같다면
    # 해당 강의실을 이어서 쓸 수 있음 (재사용)
    if start >= pq[0]:
        heapq.heappop(pq) # 기존 종료 시간을 제거
        
    # 새로운 종료 시간을 힙에 추가
    # (재사용했다면 시간 갱신, 아니면 강의실 하나 추가되는 효과)
    heapq.heappush(pq, end)

# 5. 우선순위 큐에 남아있는 원소의 개수가 곧 필요한 강의실의 최소 개수
print(len(pq))