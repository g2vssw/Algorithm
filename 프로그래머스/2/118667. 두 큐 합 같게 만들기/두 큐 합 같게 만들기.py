from collections import deque

def solution(queue1, queue2):
    answer = 0
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    sum1 = sum(queue1)
    sum2 = sum(queue2)
    total_sum = sum1 + sum2

    if total_sum % 2 != 0:
        return -1
    
    limit = len(queue1) * 4
    target = total_sum // 2
    
    while sum1 != target:
        
        if answer > limit:
            answer = -1
            break
        
        if sum1 > sum2:
            temp = queue1.popleft()
            queue2.append(temp)
            sum1 -= temp
            sum2 += temp
        else:
            temp = queue2.popleft()
            queue1.append(temp)
            sum2 -= temp
            sum1 += temp
        
        answer += 1
        
    return answer