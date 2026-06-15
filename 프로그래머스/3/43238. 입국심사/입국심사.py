def solution(n, times):
    answer = 0
    start_min = min(times) * n // len(times)
    end_min = max(times) * n // len(times)
    while start_min <= end_min:
        mid_min = (start_min + end_min) // 2
        
        people = 0
        for time in times:
            people += mid_min // time
            
        
        if people >= n:
            answer = mid_min
            end_min = mid_min - 1
        else:
            start_min = mid_min + 1
    
    return answer