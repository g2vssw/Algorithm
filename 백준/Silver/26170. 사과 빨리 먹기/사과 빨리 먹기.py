import sys

input = sys.stdin.readline

# 방향 지정: 상우하좌
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def dfs(arr, ci, cj, apple, dis):
    # global을 활용해 모든 이동 횟수 result 저장
    global result

    # 사과 3개 먹으면 return
    if apple == 3:
        result.append(dis)
        return
    
    # 4방향
    for k in range(4):
        # 다음 좌표 지정
        ni, nj = ci + di[k], cj + dj[k]
        # 범위, 장애물 확인
        if 0 <= ni < 5 and 0 <= nj < 5 and arr[ni][nj] != -1:
            # 다음 좌표에 사과가 있으면 apple + 1
            if arr[ni][nj] == 1:
                apple += 1

            # 기존 arr[ni][nj] 값 temp 저장
            temp = arr[ni][nj]
            # 방문 처리
            arr[ni][nj] = -1

            dfs(arr, ni, nj, apple, dis + 1)

            # 백트래킹: 방문 처리 초기화, 사과 갯수 초기화
            arr[ni][nj] = temp

            if arr[ni][nj] == 1:
                apple -= 1
        
# 5 x 5 보드
arr = [list(map(int, input().split())) for _ in range(5)]
r, c = map(int, input().split())

# 시작 세팅: 시작 지점에 사과가 있으면 1 없으면 0
if arr[r][c]:
    apple = 1
else:
    apple = 0
# 방문 처리
arr[r][c] = -1

# 보드, ci, cj, 사과, 이동 횟수
result = []
dfs(arr, r, c, apple, 0)

# 결과가 있으면 최소 값 없으면 -1 출력
if result:
    result = min(result)
else:
    result = -1

print(result)