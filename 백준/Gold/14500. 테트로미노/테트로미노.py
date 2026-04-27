import sys

input = sys.stdin.readline

# N: 세로 크기, M: 가로 크기
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

# 상, 하, 좌, 우 이동 방향
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 전체 격자에서 가장 큰 값 (가지치기에 사용)
max_val = max(map(max, board))
ans = 0

def dfs(r, c, depth, current_sum):
    global ans
    
    # 1. 가지치기: 현재 합 + (남은 칸 수 * 격자 최댓값)이 기존 정답보다 작으면 가망 없음
    if current_sum + max_val * (4 - depth) <= ans:
        return

    # 2. 4칸을 모두 골랐다면 최댓값 갱신 후 종료
    if depth == 4:
        ans = max(ans, current_sum)
        return

    # 3. 인접한 방향으로 탐색
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        
        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
            # 'ㅗ' 모양 처리를 위한 로직: 2번째 칸에서 탐색할 때 
            # 다음 칸으로 이동하지 않고 현재 칸에서 다시 탐색하면 'ㅗ' 모양이 됨
            if depth == 2:
                visited[nr][nc] = True
                dfs(r, c, depth + 1, current_sum + board[nr][nc])
                visited[nr][nc] = False
                
            visited[nr][nc] = True
            dfs(nr, nc, depth + 1, current_sum + board[nr][nc])
            visited[nr][nc] = False

# 모든 칸을 시작점으로 하여 탐색 수행
for r in range(N):
    for c in range(M):
        visited[r][c] = True
        dfs(r, c, 1, board[r][c])
        visited[r][c] = False

print(ans)