import sys
from collections import deque

input = sys.stdin.readline

def bfs(start, end):
    
    queue =  deque([(start, 0)])
    visited[start] = 1

    while queue:
        
        node, cnt = queue.popleft()
    
        # b번째 징검다리에 도착하면 종료
        if node == end:
            return cnt
        
        # Right →
        for next_node in range(node + bridge[node], N + 1, bridge[node]):
            if visited[next_node]:
                continue
            visited[next_node] = 1
            queue.append((next_node, cnt + 1))

        # Left ←
        for next_node in range(node - bridge[node], 0, - bridge[node]):
            if visited[next_node]:
                continue
            visited[next_node] = 1
            queue.append((next_node, cnt + 1))

    # 도착하지 못 할 경우
    return -1

N = int(input())
bridge = [0] + list(map(int, input().split()))
a, b = map(int, input().split())
# 인덱스 번호와 맞추기 위해 앞에 0 추가
visited = [0] * (N + 1)

result = bfs(a, b)

print(result)