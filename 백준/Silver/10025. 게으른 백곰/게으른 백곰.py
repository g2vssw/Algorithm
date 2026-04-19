N, K = map(int, input().split())
li = [0] * 1000001

M = 0
for _ in range(N):
    g, x = map(int, input().split())
    li[x] = g
    M = max(M, x)

window = sum(li[:K*2 + 1])
result = window
for i in range(M + 1 - (K*2 + 1)):
    window = window - li[i] + li[i + (K*2 + 1)]
    if result < window:
        result = window

print(result)