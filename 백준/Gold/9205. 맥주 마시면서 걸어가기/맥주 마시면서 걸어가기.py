import sys
from collections import deque

def bfs():
    queue = deque([(si, sj)])

    while queue:
        ci, cj = queue.popleft()

        if abs(ei-ci) + abs(ej-cj) <= 1000:
            return "happy"

        for k in range(n):
            if visited[k]:
                continue
            ni, nj = convenience_store[k]
            if abs(ni-ci) + abs(nj-cj) <= 1000:
                visited[k] = 1
                queue.append((ni, nj))
    
    return "sad"


input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    si, sj = map(int, input().split())
    convenience_store = []
    for _ in range(n):
        con_i, con_j = map(int, input().split())
        convenience_store.append((con_i, con_j))
    ei, ej = map(int, input().split())
    visited = [0] * (n + 1)
    print(bfs())