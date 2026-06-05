def solution(progresses, speeds):
    answer = []
    stack = []
    cnt = 0
    
    while cnt < len(progresses):
        for i in range(len(progresses)):
            if progresses[i] >= 100:
                continue
            else:
                progresses[i] += speeds[i]
                if progresses[i] >= 100:
                    stack.append(i)
            
        stack.sort(reverse=True)
        
        if stack and stack[-1] == cnt:
            check = 0
            while stack and stack[-1] == cnt:
                stack.pop()
                check += 1
                cnt += 1
            answer.append(check)
    
    return answer