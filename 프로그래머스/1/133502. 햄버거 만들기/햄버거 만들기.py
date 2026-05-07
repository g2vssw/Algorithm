def solution(ingredient):
    answer = 0
    stack = []
    for n in ingredient:
        stack.append(n) 
        
        if len(stack) >= 4 and stack[-4:] == [1, 2, 3, 1]:
            answer += 1    
            
            for _ in range(4):
                stack.pop()
    return answer