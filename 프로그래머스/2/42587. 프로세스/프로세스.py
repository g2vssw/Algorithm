from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque()
    
    for num in priorities:
        queue.append(num)
    
    flag = 0
    idx = location
    while queue:
        
        if flag:
            break
        
        process = queue.popleft()
        idx -= 1
        if idx == -1:
            flag = 1
            idx = len(queue)
        
        check = 1
        for num in queue:
            if process < num:
                check = 0
                flag = 0
                queue.append(process)
                break
        
        if check:
            answer += 1

    return answer