from collections import deque

def solution(x, y, n):
    
    if x == y:
        return 0
    
    queue = deque([(x, 0)])
    visited = {x}

    while queue:
        
        cur_val, cnt = queue.popleft()
        
        for next_val in (cur_val + n, cur_val * 2, cur_val * 3):
            if next_val == y:
                return cnt + 1
            
            if next_val < y and next_val not in visited:
                visited.add(next_val)
                queue.append((next_val, cnt + 1))

    return -1