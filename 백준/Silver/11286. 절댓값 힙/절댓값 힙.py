import sys
import heapq

input = sys.stdin.readline

def solve():
    N = int(input())
    # 절댓값 힙을 위한 리스트
    abs_heap = []
    
    for _ in range(N):
        x = int(input())
        
        if x != 0:
            # (절댓값, 원래 값) 튜플로 푸시
            # 1순위: abs(x), 2순위: x 기준으로 자동 정렬됨
            heapq.heappush(abs_heap, (abs(x), x))
        else:
            # x가 0일 때 출력 및 제거 연산
            if not abs_heap:
                print(0)
            else:
                # 힙에서 꺼낸 튜플의 1번 인덱스(원래 값) 출력
                print(heapq.heappop(abs_heap)[1])

# 함수 즉시 실행
solve()