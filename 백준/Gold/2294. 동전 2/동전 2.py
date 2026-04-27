import sys

input = sys.stdin.readline

def solve():
    # 1. n(동전 종류), k(목표 금액) 입력
    n, k = map(int, input().split())
    
    # 중복된 가치의 동전이 들어올 수 있으므로 set으로 받아 중복 제거
    coins = set()
    for _ in range(n):
        coins.add(int(input()))
    
    # 2. DP 테이블 초기화
    # 최솟값을 찾아야 하므로 아주 큰 값(k + 1)으로 채움
    inf = k + 1
    dp = [inf] * (k + 1)
    
    # 0원을 만드는 최소 개수는 0개
    dp[0] = 0
    
    # 3. 각 동전별로 DP 테이블 갱신
    for coin in coins:
        # 동전의 가치부터 k원까지 탐색
        for i in range(coin, k + 1):
            # 기존의 dp[i]와 (현재 동전을 하나 썼을 때의 개수) 중 최솟값 선택
            if dp[i - coin] != inf: # 이전에 만들 수 있었던 금액인 경우에만 갱신
                dp[i] = min(dp[i], dp[i - coin] + 1)
                
    # 4. 결과 출력
    # dp[k]가 초기값 그대로라면 k원을 만들 수 없다는 뜻이므로 -1 출력
    if dp[k] == inf:
        print(-1)
    else:
        print(dp[k])

# 함수 실행
solve()