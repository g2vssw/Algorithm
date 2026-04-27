import sys

input = sys.stdin.readline

# 1. 입력 받기
N = int(input())

# N이 1인 경우 소수가 없으므로 바로 0 출력 후 종료
if N == 1:
    print(0)
    sys.exit()

# 2. 에라토스테네스의 체를 이용해 N까지의 모든 소수 구하기
is_prime = [True] * (N + 1)
is_prime[0] = is_prime[1] = False # 0과 1은 소수가 아님

for i in range(2, int(N**0.5) + 1):
    if is_prime[i]:
        # i가 소수라면, i의 배수들은 모두 소수가 아님
        for j in range(i * i, N + 1, i):
            is_prime[j] = False

# 소수들만 모은 리스트 생성
primes = [i for i, p in enumerate(is_prime) if p]

# 3. 투 포인터를 사용하여 연속합 찾기
count = 0        # 조건에 맞는 경우의 수
start = 0        # 시작 포인터
current_sum = 0  # 현재 구간의 합

# end 포인터를 한 칸씩 늘려가며 탐색
for end in range(len(primes)):
    current_sum += primes[end]
    
    # 합이 N보다 크다면 작아질 때까지 start를 오른쪽으로 이동
    while current_sum > N:
        current_sum -= primes[start]
        start += 1
    
    # 합이 정확히 N이 되면 경우의 수 추가
    if current_sum == N:
        count += 1

# 4. 결과 출력
print(count)