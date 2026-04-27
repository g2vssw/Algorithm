import sys
from collections import deque

input = sys.stdin.readline

# 1. N(세로), M(가로) 입력
N, M = map(int, input().split())

# 격자 정보 입력
board = [list(map(int, input().strip())) for _ in range(N)]

# 2. 3차원 방문 배열 초기화: visited[r][c][wall_broken]
# wall_broken: 0이면 안 부순 상태, 1이면 부순 상태
# 값은 시작점으로부터의 이동 거리(최단 경로)를 저장함
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]

# 3. BFS 수행
# 큐 저장 형태: (r, c, wall_broken)
queue = deque([(0, 0, 0)])
visited[0][0][0] = 1 # 시작점 거리 1부터 시작

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

ans = -1

while queue:
    r, c, broken = queue.popleft()
    
    # 목표 지점에 도달하면 결과 저장 후 종료 (BFS이므로 처음 도달이 최단거리 보장)
    if r == N - 1 and c == M - 1:
        ans = visited[r][c][broken]
        break
        
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        
        # 격자 범위 내에 있는지 확인
        if 0 <= nr < N and 0 <= nc < M:
            # 다음 칸이 이동 가능한 길(0)이고, 해당 상태(broken)로 방문한 적이 없는 경우
            if board[nr][nc] == 0 and visited[nr][nc][broken] == 0:
                visited[nr][nc][broken] = visited[r][c][broken] + 1
                queue.append((nr, nc, broken))
            
            # 다음 칸이 벽(1)이고, 아직 벽을 부순 적이 없는 경우(broken == 0)
            elif board[nr][nc] == 1 and broken == 0:
                # 벽을 부수고(broken -> 1) 방문 처리
                if visited[nr][nc][1] == 0:
                    visited[nr][nc][1] = visited[r][c][0] + 1
                    queue.append((nr, nc, 1))

# 4. 결과 출력
print(ans)