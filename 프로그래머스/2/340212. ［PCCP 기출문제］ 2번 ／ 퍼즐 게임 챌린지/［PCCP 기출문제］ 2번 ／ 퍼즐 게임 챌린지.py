def solution(diffs, times, limit):
    answer = float('inf')
    start_level = 1
    max_level = max(diffs)
    
    while start_level <= max_level:
        
        mid_level = (start_level + max_level) // 2
        
        time_sum = 0
        for i in range(len(diffs)):
            if diffs[i] <= mid_level:
                time_sum += times[i]
            elif diffs[i] > mid_level:
                time_sum += (times[i-1] + times[i]) * (diffs[i] - mid_level) + times[i]
        
        if time_sum <= limit:
            answer = min(answer, mid_level)
            max_level = mid_level - 1
        else:
            start_level = mid_level + 1
    
    return answer