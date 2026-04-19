n, m = map(int, input().split())
pay = list(map(int, input().split()))

window = sum(pay[:m])
result = window
for i in range(n - m):
    window = window - pay[i] + pay[i + m]
    if result < window:
        result = window

print(result)