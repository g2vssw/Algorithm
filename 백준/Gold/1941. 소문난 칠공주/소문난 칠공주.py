import sys
from collections import deque

input = sys.stdin.readline

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def bfs(si, sj):
    
    bfs_visited = [[False] * 5 for _ in range(5)]
    bfs_visited[si][sj] = True

    queue = deque([(si, sj)])

    count = 1
    while queue:

        ci, cj = queue.popleft()

        for k in range(4):
            ni, nj = ci + di[k], cj + dj[k]
            if 0 <= ni < 5 and 0 <= nj < 5 and bfs_visited[ni][nj] == False and visited[ni][nj] == True:
                count += 1
                bfs_visited[ni][nj] = True
                queue.append((ni, nj))

    if count == 7:
        return True
    return False

def check():
    for i in range(5):
        for j in range(5):
            if visited[i][j]:
                # bfs 활용하여 체크
                if bfs(i, j):
                    return True
                else:
                    return False

def dfs(n, cnt, s_cnt):
    global result

    # 조기 종료: 7명이 모이면 즉시 확인 후 종료
    if cnt == 7:
        if s_cnt >= 4:
            if check():
                result += 1
        return
    
    # 불가능한 경우 가지치기: 현재 다솜파 수 + 남은 자리 수가 4명 미만이면 종료
    if s_cnt + (7 - cnt) < 4:
        return

    # 끝에 도달하면
    if n == 25:
        return

    # 포함하는 경우
    visited[n//5][n%5] = True
    if arr[n//5][n%5] == "S":
        dfs(n + 1, cnt + 1, s_cnt + 1)
    else:
        dfs(n + 1, cnt + 1, s_cnt)
    # 백트래킹
    visited[n//5][n%5] = False

    # 포함하지 않는 경우
    dfs(n + 1, cnt, s_cnt)


arr = [list(input().strip()) for _ in range(5)]

result = 0

visited = [[False] * 5 for _ in range(5)]

# 학생번호(0 ~ 24), 포함 학생수, 다솜파 수
dfs(0, 0, 0)

print(result)