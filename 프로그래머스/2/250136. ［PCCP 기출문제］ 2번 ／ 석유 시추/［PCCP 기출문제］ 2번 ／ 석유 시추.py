from collections import deque

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def solution(land):
    answer = 0
    n, m = len(land), len(land[0])
    oil_dict = {}
    cnt = 1
    def bfs(si, sj):
        nonlocal land
        
        land[si][sj] = cnt
        queue = deque([(si, sj)])
        
        count = 1
        while queue:
            
            ci, cj = queue.popleft()
            
            for k in range(4):
                ni, nj = ci + di[k], cj + dj[k]
                if 0 <= ni < n and 0 <= nj < m and land[ni][nj] == 1:
                    count += 1
                    land[ni][nj] = cnt
                    queue.append((ni, nj))
        
        return count

    for j in range(m):
        oil = 0
        check = []
        for i in range(n):
            if land[i][j] == 0:
                continue
            elif land[i][j] == 1:
                cnt += 1
                oil_dict[cnt] = bfs(i, j)
                check.append(cnt)
                oil += oil_dict[land[i][j]]
            else:
                if land[i][j] in check:
                    continue
                else:
                    check.append(land[i][j])
                    oil += oil_dict[land[i][j]]
                    
        answer = max(answer, oil)
        
    return answer