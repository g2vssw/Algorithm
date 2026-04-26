import sys

input = sys.stdin.readline

N, M = map(int, input().split())
array = list(map(int, input().split()))
s = 0
ps = 0

ans = N + 1
i, j = 0, 0
s += array[j]
while j < N:
    if s - ps < M:
        j += 1
        if j < N:
            s += array[j]
    else:
        if i == j:
            ans = 1
            print(ans)
            exit()
        if j - i + 1 <= ans:
            ans = j - i + 1
        ps += array[i]
        i += 1

if ans == N + 1:
    ans = 0
    
print(ans)