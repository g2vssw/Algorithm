import sys
import heapq # 최소 힙(우선순위 큐)을 사용하기 위함

input = sys.stdin.readline

# 1. N(카드 더미의 개수) 입력
N = int(input())

# 2. 카드 더미 크기를 최소 힙에 삽입
# heapq는 리스트를 최소 힙처럼 다룰 수 있게 해줌
card_heaps = []
for _ in range(N):
    heapq.heappush(card_heaps, int(input()))

# 3. 예외 처리
# 카드 더미가 1개라면 비교할 필요가 없으므로 0을 출력하고 종료
if N == 1:
    print(0)
    sys.exit()

# 최종 비교 횟수 합계
total_comparisons = 0

# 4. 더미가 하나가 될 때까지 반복
while len(card_heaps) > 1:
    # 가장 작은 두 더미를 꺼냄
    first = heapq.heappop(card_heaps)
    second = heapq.heappop(card_heaps)
    
    # 두 더미를 합치는 비용 계산
    current_sum = first + second
    # 전체 비용에 누적
    total_comparisons += current_sum
    
    # 합쳐진 새로운 더미를 다시 힙에 삽입
    heapq.heappush(card_heaps, current_sum)

# 5. 결과 출력
print(total_comparisons)