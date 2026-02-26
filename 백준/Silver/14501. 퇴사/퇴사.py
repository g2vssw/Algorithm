import sys

input = sys.stdin.readline

# 퇴사 전 N일
N = int(input())

# dp_d: 걸리는 기간 계산
dp_d = [-1] * N
# dp_v: 받을 수 있는 금액 계산
dp_v = [0] * N

# N일 동안 반복
for i in range(N):
    # 하루 마다 걸리는 기간 -1
    for j in range(i + 1):
        # 기간을 채웠거나 초기화 되어 있을 시 continue, 그것이 아니면 걸리는 기간 계산
        if dp_d[j] == 0 or dp_d[j] == -1:
            continue
        else:
            dp_d[j] -= 1
    # 상담을 완료하는데 걸리는 기간 T와 상담을 했을 때 받을 수 있는 금액 P
    T, P = map(int, input().split())
    # 상담을 완료하는데 걸리는 기간이 퇴사 전보다 길다면 continue
    if N - i < T:
        continue
    # 걸리는 시간 저장
    dp_d[i] = T
    # 해당 일(i)까지 받을 수 있는 최대 금액 계산: 이전 기간을 확인하여 기간을 채운 날의 금액 합 경우의 수를 모두 체크
    max_P = P
    for k in range(i + 1):
        # 기간을 채웠으면 기존 최대값을 비교
        if dp_d[k] == 0:
            max_P = max(max_P, (P + dp_v[k]))
    # 해당 일 최대 금액 저장
    dp_v[i] = max_P

print(max(dp_v))