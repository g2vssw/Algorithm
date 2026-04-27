import sys

input = sys.stdin.readline

def solve():
    # 1. n(동전 종류), k(목표 금액) 입력
    n, k = map(int, input().split())
    
    coins = []
    for _ in range(n):
        coins.append(int(input()))
    
    # 2. DP 테이블 초기화 (1차원 배열로 메모리 절약)
    # k가 최대 10,000이므로 10,001칸의 리스트는 4MB 안에 충분히 들어감
    dp = [0] * (k + 1)
    
    # 0원을 만드는 경우의 수는 1가지 (아무것도 안 내기)
    dp[0] = 1
    
    # 3. 각 동전별로 DP 테이블 갱신
    for coin in coins:
        # 현재 동전의 가치(coin)부터 목표 금액(k)까지 탐색
        for i in range(coin, k + 1):
            # i원을 만드는 방법 = 기존 방법 + (i - 현재동전)을 만드는 방법
            # 이 누적 방식이 2차원 DP의 행을 압축한 형태임
            dp[i] += dp[i - coin]
            
    # 4. 결과 출력 (k원을 만드는 모든 경우의 수)
    print(dp[k])

# 함수 호출
solve()