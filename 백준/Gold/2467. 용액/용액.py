import sys

input = sys.stdin.readline

# 1. 입력 받기
# N: 용액의 수 (최대 100,000)
N = int(input())
# 용액의 특성값 리스트 (이미 오름차순 정렬되어 있음)
arr = list(map(int, input().split()))

# 2. 필요한 변수 초기화
left = 0
right = N - 1

# 현재까지 찾은 0에 가장 가까운 합의 절댓값 (최초는 아주 큰 값)
min_abs_sum = float('inf')
# 결과값을 담을 리스트
result = [0, 0]

# 3. 투 포인터 탐색 수행 (두 포인터가 만날 때까지)
while left < right:
    current_sum = arr[left] + arr[right]
    
    # 현재 합의 절댓값이 기존의 최솟값보다 작으면 정보 갱신
    if abs(current_sum) < min_abs_sum:
        min_abs_sum = abs(current_sum)
        result[0] = arr[left]
        result[1] = arr[right]
        
    # 합이 정확히 0이면 더 이상 찾을 필요가 없으므로 종료
    if current_sum == 0:
        break
        
    # 합이 0보다 작으면 더 큰 값이 필요하므로 왼쪽 포인터를 오른쪽으로
    if current_sum < 0:
        left += 1
    # 합이 0보다 크면 더 작은 값이 필요하므로 오른쪽 포인터를 왼쪽으로
    else:
        right -= 1

# 4. 결과 출력
# 이미 정렬된 리스트에서 뽑았으므로 result[0], result[1] 순서대로 출력하면 됨
print(result[0], result[1])