import sys

input = sys.stdin.readline

# 1. 두 문자열 입력 받기
# strip()으로 양 끝의 개행 문자를 제거함
S1 = input().strip()
S2 = input().strip()

# 각 문자열의 길이 계산
len1 = len(S1)
len2 = len(S2)

# 2. DP 테이블 초기화
# 가로(len2+1), 세로(len1+1) 크기의 2차원 배열 생성
# 인덱스 0은 '아무것도 선택하지 않은 상태'를 의미하여 계산을 편하게 함
dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

# 3. DP 테이블 채우기 (2중 루프)
# 모든 문자를 하나씩 비교하며 최적해(LCS 길이)를 누적함
for i in range(1, len1 + 1):
    for j in range(1, len2 + 1):
        # 두 문자가 같은 경우 (S1[i-1]과 S2[j-1]이 실제 문자)
        if S1[i-1] == S2[j-1]:
            # 대각선 왼쪽 위(이전까지의 LCS)에서 1을 더함
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            # 두 문자가 다른 경우
            # 'S1의 현재 문자를 제외한 값'과 'S2의 현재 문자를 제외한 값' 중 큰 것을 가져옴
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

# 4. 결과 출력
# 테이블의 가장 마지막 칸(-1, -1)에 전체 문자열에 대한 LCS 최대 길이가 담김
print(dp[len1][len2])