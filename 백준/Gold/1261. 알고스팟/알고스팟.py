import sys
from collections import deque

input = sys.stdin.readline

# 1. 입력 받기
# 주의: M이 가로(열), N이 세로(행)로 주어집니다.
M, N = map(int, input().split())

# 미로 정보 입력
board = [list(map(int, input().strip())) for _ in range(N)]

# 2. 방문 및 비용 저장 배열 초기화 (-1은 아직 방문하지 않음을 의미)
dist = [[-1] * M for _ in range(N)]

# 3. 0-1 BFS 수행
def bfs():
    # 시작점 (0, 0) 설정
    queue = deque([(0, 0)])
    dist[0][0] = 0
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    while queue:
        r, c = queue.popleft()
        
        # 목표 지점 (N-1, M-1)에 도달하면 부순 벽의 수 반환
        if r == N - 1 and c == M - 1:
            return dist[r][c]
            
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            
            # 격자 범위 내에 있고 아직 방문하지 않은 경우
            if 0 <= nr < N and 0 <= nc < M and dist[nr][nc] == -1:
                
                # 빈 방(0)인 경우: 벽을 부수지 않으므로 비용 0 추가
                if board[nr][nc] == 0:
                    dist[nr][nc] = dist[r][c]
                    # 비용이 0이므로 우선순위를 높여 덱의 앞에 삽입
                    queue.appendleft((nr, nc))
                
                # 벽(1)인 경우: 벽을 부수므로 비용 1 추가
                else:
                    dist[nr][nc] = dist[r][c] + 1
                    # 비용이 발생하므로 덱의 뒤에 삽입
                    queue.append((nr, nc))

# 4. 결과 출력
# N=1, M=1인 경우 루프를 타지 않을 수 있으므로 초기값 처리 주의
if N == 1 and M == 1:
    print(0)
else:
    print(bfs())