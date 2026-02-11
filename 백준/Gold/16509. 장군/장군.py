import sys
from collections import deque

input = sys.stdin.readline

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

cheak_dict = {0: ((-1, -1), (-1, 1)),
              1: ((-1, 1), (1, 1)),
              2: ((1, -1), (1, 1)),
              3: ((-1, -1), (1, -1))
              }

def bfs(si, sj, cnt):
    
    visited[si][sj] = 1
    queue = deque([(si, sj, cnt)])
    
    while queue:

        ci, cj, cnt = queue.popleft()

        if (ci, cj) == (ki, kj):
            return cnt
        
        for k in range(4):
            ni1, nj1 = ci + di[k], cj + dj[k]
            if ni1 < 0 or ni1 >= N or nj1 < 0 or nj1 >= M or (ni1, nj1) == (ki, kj):
                continue
            for mi, mj in cheak_dict[k]:
                ni2, nj2 = ni1 + mi, nj1 + mj
                if ni2 < 0 or ni2 >= N or nj2 < 0 or nj2 >= M or (ni2, nj2) == (ki, kj):
                    continue
                else:
                    ni, nj = ni2 + mi, nj2 + mj
                    if ni < 0 or ni >= N or nj < 0 or nj >= M or visited[ni][nj] == 1:
                        continue
                    visited[ni][nj] = 1
                    queue.append((ni, nj, cnt + 1))

    return -1

    
si, sj = map(int, input().split())
ki, kj = map(int, input().split())
N, M = 10, 9

visited = [[0] * M for _ in range(N)]

result = bfs(si, sj, 0)

print(result)