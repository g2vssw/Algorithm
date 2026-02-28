import sys

input = sys.stdin.readline

def queen_cheak(ci, cj, path):
    
    if len(path) == 0:
        return 1
    
    for pi, pj in path:
        if ci == pi or cj == pj or (pi - pj) == (ci - cj) or (pi + pj) == (ci + cj):
            return 0
    
    return 1

def n_queen():
    
    cnt = 0

    def backtrack(si, path):
        nonlocal cnt

        if len(path) == N:
            cnt += 1
        
        for j in range(N):
            if queen_cheak(si, j, path):
                path.append((si, j))
                backtrack(si + 1, path)
                path.pop()

    backtrack(0, [])

    return cnt

N = int(input())

result = n_queen()

print(result)