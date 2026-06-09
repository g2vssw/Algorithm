def solution(numbers, target):
    answer = 0
    
    def dfs(count, value):
        nonlocal answer
        
        if count == len(numbers):
            if value == target:
                answer += 1
            return
        
        dfs(count + 1, value + numbers[count])
        dfs(count + 1, value - numbers[count])
    
    dfs(0, 0)
    
    return answer