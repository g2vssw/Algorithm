def solution(cap, n, deliveries, pickups):
    answer = 0
    
    deliver_need = 0
    pickup_need = 0
    
    for i in range(n - 1, -1, -1):
        deliver_need += deliveries[i]
        pickup_need += pickups[i]
        
        while deliver_need > 0 or pickup_need > 0:
            deliver_need -= cap
            pickup_need -= cap
            
            answer += (i + 1) * 2
    
    return answer