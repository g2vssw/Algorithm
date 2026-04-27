import sys
from collections import Counter

input = sys.stdin.readline

# 1. 입력 받기
T = int(input()) # 목표 합

n = int(input())
A = list(map(int, input().split()))

m = int(input())
B = list(map(int, input().split()))

# 2. 배열 A의 모든 가능한 부분 합 구하기
# sums_a 리스트에 모든 부분 합을 저장 (O(N^2))
sums_a = []
for i in range(n):
    current_sum = 0
    for j in range(i, n):
        current_sum += A[j]
        sums_a.append(current_sum)

# 3. 배열 B의 모든 가능한 부분 합 구하며 빈도수 기록
# dict를 사용하여 특정 합이 몇 번 나오는지 저장 (O(M^2))
sums_b = Counter()
for i in range(m):
    current_sum = 0
    for j in range(i, m):
        current_sum += B[j]
        sums_b[current_sum] += 1

# 4. 결과 계산
# A의 부분 합을 하나씩 확인하며 (T - a_sum)이 B의 부분 합에 있는지 체크
ans = 0
for a_sum in sums_a:
    target = T - a_sum
    if target in sums_b:
        ans += sums_b[target]

# 5. 최종 경우의 수 출력
print(ans)