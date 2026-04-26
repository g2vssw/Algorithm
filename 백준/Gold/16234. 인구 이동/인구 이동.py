import sys
from collections import deque

input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, 1, 0 ,-1]

def find_union(sy, sx, visited):
    que = deque([(sy, sx)])
    visited[sy][sx] = True

    union_cells = [(sy, sx)] # 연합에 속한 나라 좌표
    total_population = areas[sy][sx] # 연합의 총 인구수

    while que:
        cy, cx = que.popleft()
        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]

            # 방문하지 않았고, 국경을 열 수 있는 조건이라면
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                diff = abs(areas[cy][cx] - areas[ny][nx])
                if L <= diff <= R:
                    visited[ny][nx] = True
                    que.append((ny, nx))
                    union_cells.append((ny, nx))
                    total_population += areas[ny][nx]

    return union_cells, total_population

N, L, R = map(int, input().split())
areas = [list(map(int, input().split())) for _ in range(N)]

days = 0
while True:

    flag = False
    visited = [[False] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                union_cells, total_population = find_union(r, c, visited) # 하나의 연합이 찾아짐

                if len(union_cells) > 1:
                    flag = True
                    # 인구 이동이 필요할 때만 계산 및 재할당 수행
                    new_population = total_population // len(union_cells)
                    for y, x in union_cells:
                        areas[y][x] = new_population

    if not flag:
        print(days)
        break

    days += 1
