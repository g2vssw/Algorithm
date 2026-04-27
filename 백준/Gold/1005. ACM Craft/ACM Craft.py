import sys
from collections import deque

input = sys.stdin.readline

def solve():
    # 1. 입력 받기
    # N: 건물의 개수, K: 건설 순서 규칙의 개수
    N, K = map(int, input().split())
    
    # 각 건물당 건설에 걸리는 시간 (인덱스 조절을 위해 앞에 0 추가)
    build_time = [0] + list(map(int, input().split()))
    
    # 그래프 및 진입 차수 배열 초기화
    adj = [[] for _ in range(N + 1)]
    indegree = [0] * (N + 1)
    
    for _ in range(K):
        u, v = map(int, input().split())
        adj[u].append(v) # u를 지어야 v를 지을 수 있음
        indegree[v] += 1
        
    # 승리하기 위해 건설해야 할 건물 번호
    target = int(input())

    # 2. DP 테이블 및 위상 정렬 초기화
    # dp[i]는 i번 건물을 완공하기까지 걸리는 총 최소 시간
    dp = [0] * (N + 1)
    queue = deque()

    # 진입 차수가 0인(선행 건물이 없는) 건물들을 큐에 삽입
    for i in range(1, N + 1):
        if indegree[i] == 0:
            queue.append(i)
            dp[i] = build_time[i] # 해당 건물의 건설 시간 자체가 초기값

    # 3. 위상 정렬 수행하며 DP 값 갱신
    while queue:
        current = queue.popleft()
        
        # 목표 건물을 이미 처리했다면 더 돌 필요는 없으나, 
        # 위상 정렬 흐름상 전체를 훑어도 무방함
        if current == target:
            break
            
        for next_node in adj[current]:
            # 핵심 로직: 다음 건물의 완공 시간은 
            # (현재까지 계산된 다음 건물의 시간)과 (현재 건물 완공 + 다음 건물 소요 시간) 중 최댓값
            dp[next_node] = max(dp[next_node], dp[current] + build_time[next_node])
            indegree[next_node] -= 1
            
            # 모든 선행 건물이 지어졌다면 큐에 삽입
            if indegree[next_node] == 0:
                queue.append(next_node)

    # 4. 결과 출력
    print(dp[target])

# 테스트 케이스 개수만큼 실행
T = int(input())
for _ in range(T):
    solve()