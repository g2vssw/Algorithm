import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while True:
        
        first_scoville = heapq.heappop(scoville)

        if first_scoville >= K:
            break
        
        elif len(scoville) <= 0:
            answer = -1
            break
        
        second_scoville = heapq.heappop(scoville)

        heapq.heappush(scoville, first_scoville + (second_scoville * 2))
        
        answer += 1
    
    
    
    return answer