def solution(N, stages):
    answer = []
    rate_list = []
    num = [0] * (N + 2)
    den = len(stages)
    
    for stage in stages:
        num[stage] += 1
        
    for i in range(1, N + 1):
        if den == 0:
            rate = 0
        else:
            rate = num[i] / den
            
        den -= num[i]
        rate_list.append((rate, i))
        
    rate_list.sort(key=lambda x: (-x[0], x[1]))

    for fr in rate_list:
        answer.append(fr[1])
    
    return answer