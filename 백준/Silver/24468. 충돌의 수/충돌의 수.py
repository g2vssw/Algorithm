import sys

input = sys.stdin.readline

# 상자의 길이 L, 공의 개수 N, 시간 T
L, N, T = map(int, input().split())

# R이면 1, L면 -1로 입력
balls = []
for _ in range(N):
    S, C = input().split()
    if C == "R":
        balls.append([int(S), 1])
    else:
        balls.append([int(S), -1])

# 충돌 카운트
result = 0

# 시간 T
for _ in range(T):
    # 방향으로 이동
    for ball in balls:
        ball[0] += ball[1]
        # 벽에 충돌 시 방향 전환
        if ball[0] in [0, L]:
            ball[1] *= -1
        
    # 현재 좌표(balls[i][0]) 키로, balls 인덱스를 값으로 하는 딕셔너리 생성
    position_dict = {}
    for i in range(len(balls)):
        if balls[i][0] not in position_dict:
            position_dict[balls[i][0]] = []
        position_dict[balls[i][0]].append(i)

    # 충돌 확인 후 방향 전환
    for position in position_dict:
        if len(position_dict[position]) == 2:
            result += 1
            idx1, idx2 =  position_dict[position]
            balls[idx1][1] *= -1
            balls[idx2][1] *= -1
    
print(result)