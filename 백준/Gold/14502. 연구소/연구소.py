import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

# 방향 벡터 (상, 우, 하, 좌)
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def bfs():
    """ BFS를 활용해 바이러스 확산 후 안전 영역 크기 반환 """
    queue = deque(virus_positions)  # 초기 바이러스 위치를 큐에 삽입
    visited = [row[:] for row in arr]  # 기존 맵을 복사 (deepcopy 대신 list slicing 사용)

    while queue:
        i, j = queue.popleft()
        for k in range(4):  # 4방향 탐색
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0:
                visited[ni][nj] = 2  # 바이러스 확산
                queue.append((ni, nj))

    # 안전 영역 계산
    return sum(row.count(0) for row in visited)


def find_max_safe_area():
    """ 벽 3개를 세울 수 있는 모든 경우의 수를 확인하고 최댓값 찾기 """
    global result
    for walls in combinations(empty_spaces, 3):  # 벽 3개를 놓을 위치를 조합으로 선택
        for i, j in walls:
            arr[i][j] = 1  # 벽 세우기

        # BFS로 안전 영역 계산 후 최댓값 갱신
        result = max(result, bfs())

        for i, j in walls:
            arr[i][j] = 0  # 벽 복구


# 입력 처리
N, M = map(int, input().split())
arr = []
virus_positions = []  # 초기 바이러스 위치 저장
empty_spaces = []  # 벽을 세울 수 있는 빈 공간 저장

for i in range(N):
    row = list(map(int, input().split()))
    arr.append(row)
    for j in range(M):
        if row[j] == 2:
            virus_positions.append((i, j))  # 바이러스 위치 저장
        elif row[j] == 0:
            empty_spaces.append((i, j))  # 빈 공간 위치 저장

# 벽 3개를 배치하는 모든 경우를 탐색하며 최대 안전 영역 찾기
result = 0
find_max_safe_area()

print(result)