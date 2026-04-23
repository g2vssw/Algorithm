N, K = map(int, input().split())
li = list(map(int, input().split()))

window = sum(li[:K])
max_value = window

for i in range(1, N - K + 1):
    window = window - li[i-1] + li[i+K-1]
    max_value = max(max_value, window)

print(max_value)