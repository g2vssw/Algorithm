import math

def solution(signals):
    answer = -1
    
    cycles = [g + y + r for g, y, r in signals]
    
    max_time = math.lcm(*cycles)
    
    for t in range(1, max_time + 1):
        all_yellow = True
        
        for g, y, r in signals:
            c = g + y + r
            
            cycle_time = (t - 1) % c
            
            if not (g <= cycle_time < g + y):
                all_yellow = False
                break
            
        if all_yellow:
            answer = t
            break
    
    return answer