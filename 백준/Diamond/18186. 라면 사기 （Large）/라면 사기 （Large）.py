import sys

input = sys.stdin.readline

n, b, c = map(int, input().split())

count_buy = list(map(int, input().split()))
lamen = [[0, 0], [0, 0]]

answer = 0
# b > c인 경우 연속해서 사는 게 이득: small 코드 활용
if b > c:
    for i in range(n - 1):
        # 현재 처리
        # i번째 공장에서 새로 사는 라면 비용 합산
        answer += count_buy[i] * b
        answer += lamen[0][0] * c
        answer += lamen[0][1] * c

        # 이번 단계에서 3원에 사는 라면이 있으면
        # 다음 단계에서 2원에 살 수 있는 라면만큼 추가
        if count_buy[i+1] > count_buy[i]:
            lamen[1][0] += count_buy[i]
            count_buy[i+1] -= count_buy[i]
        else:
            lamen[1][0] += count_buy[i+1]
            count_buy[i+1] = 0

        # 이번 단계에서 2원에 살 수 있는 라면이 있으면
        # 다음 단계에서 2원에 살 수 있는 라면만큼 추가
        if count_buy[i+1] > lamen[0][0]:
            lamen[1][1] += lamen[0][0]
            count_buy[i+1] -= lamen[0][0]
        else:
            lamen[1][1] += count_buy[i+1]
            count_buy[i+1] = 0
        
        # 상태 전이
        # 예비 저장소(lamen[1])에 담긴 할인권들을 다음 공장(i+1)용 현재 상태로 변경
        lamen[0][0] = lamen[1][0]
        lamen[0][1] = lamen[1][1]
        lamen[1] = [0, 0]
    
    # 마지막 공장(n-1)에 남은 라면과 이전에서 넘어온 할인권 최종 정산
    answer += count_buy[n-1] * b
    answer += lamen[0][0] * c
    answer += lamen[0][1] * c

    print(answer)
    
# b <= c인 경우 모두 b가격으로 구매하는 것이 저렴
else:
    for i in range(n):
        answer += count_buy[i] * b

    print(answer)