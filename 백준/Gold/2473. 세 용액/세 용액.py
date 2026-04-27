import sys

input = sys.stdin.readline

# 1. 입력 받기
N = int(input())
# 용액 데이터 리스트화 및 오름차순 정렬 (투 포인터의 전제 조건)
arr = list(map(int, input().split()))
arr.sort()

# 2. 필요한 변수 초기화
# 0에 가장 가까운 합 (최초엔 아주 큰 값)
min_abs_sum = float('inf')
# 결과값을 담을 리스트
result = []

# 3. 탐색 수행
# 한 개의 용액(i)을 고정하고 나머지 두 개를 투 포인터로 찾음
for i in range(N - 2):
    left = i + 1
    right = N - 1
    
    while left < right:
        current_sum = arr[i] + arr[left] + arr[right]
        
        # 0에 더 가까운 조합을 찾은 경우 정보 갱신
        if abs(current_sum) < min_abs_sum:
            min_abs_sum = abs(current_sum)
            result = [arr[i], arr[left], arr[right]]
            
        # 합이 0보다 작으면 더 큰 값이 필요하므로 왼쪽 포인터 이동
        if current_sum < 0:
            left += 1
        # 합이 0보다 크면 더 작은 값이 필요하므로 오른쪽 포인터 이동
        elif current_sum > 0:
            right -= 1
        # 합이 정확히 0이면 더 이상 찾을 필요가 없으므로 즉시 종료
        else:
            print(*(result))
            sys.exit()

# 4. 결과 출력
# 이미 정렬된 상태에서 탐색했으므로 자동으로 오름차순 출력됨
print(*(result))