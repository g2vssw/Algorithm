import sys

input = sys.stdin.readline

def solve():
    # 1. N 입력
    n = int(input())

    # 2. 첫 번째 줄 입력 및 초기화
    # max_dp와 min_dp를 첫 번째 줄의 값으로 시작함
    first_row = list(map(int, input().split()))
    max_dp = first_row[:]
    min_dp = first_row[:]

    # 3. 두 번째 줄부터 N번째 줄까지 반복 (슬라이딩 윈도우)
    for _ in range(n - 1):
        a, b, c = map(int, input().split())

        # 최대 점수 계산 (현재 줄의 결과를 임시 저장)
        # 0번: 이전 0, 1 중 최대 + 현재 값
        # 1번: 이전 0, 1, 2 중 최대 + 현재 값
        # 2번: 이전 1, 2 중 최대 + 현재 값
        next_max = [
            a + max(max_dp[0], max_dp[1]),
            b + max(max_dp[0], max_dp[1], max_dp[2]),
            c + max(max_dp[1], max_dp[2])
        ]
        
        # 최소 점수 계산
        next_min = [
            a + min(min_dp[0], min_dp[1]),
            b + min(min_dp[0], min_dp[1], min_dp[2]),
            c + min(min_dp[1], min_dp[2])
        ]

        # 갱신: 이전 정보를 현재 계산된 정보로 덮어씀
        max_dp = next_max
        min_dp = next_min

    # 4. 결과 출력
    print(max(max_dp), min(min_dp))

# 함수 실행
solve()