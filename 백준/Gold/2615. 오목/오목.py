import sys

input = sys.stdin.readline

# 왼쪽 끝, 세로일 경우 가장 위에 있는 바둑알의 위치를 출력해야 함으로
# 대각선 위오른쪽, 가로 오른쪽, 대각선 아래오른쪽, 세로 아래
di = [-1, 0, 1, 1]
dj = [1, 1, 1, 0]

def omok():
    for i in range(19):
        for j in range(19):
            if arr[i][j] != 0:
                ci, cj = i, j
                color = arr[i][j]

                for k in range(4):
                    count = 1
                    ni, nj = ci + di[k], cj + dj[k]
                    pi, pj = ci - di[k], cj - dj[k]

                    # 육목 체크를 위해 시작점인지 확인
                    if 0 <= pi < 19 and 0 <= pj < 19 and arr[pi][pj] == color:
                        continue
                    # 연속된 돌 세기
                    while 0 <= ni < 19 and 0 <= nj < 19 and arr[ni][nj] == color:
                        count += 1
                        ni += di[k]
                        nj += dj[k]

                    # 바둑알이 5개일 경우에만 승리
                    if count == 5:
                        return [color, f"{ci + 1} {cj + 1}"]
                    else:
                        continue
    
    return [0]

arr = [list(map(int, input().split())) for _ in range(19)]

results = omok()

for result in results:
    print(result)