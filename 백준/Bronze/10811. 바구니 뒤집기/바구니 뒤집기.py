N, M = map(int, input().split())

li = [0]
for num in range(1, N+1):
    li.append(num)
    
for _ in range(M):
    i, j = map(int, input().split())
    li[i:j+1] = li[j:i-1:-1]

print(*li[1:])