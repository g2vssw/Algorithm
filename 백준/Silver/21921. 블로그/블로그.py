N, X = map(int, input().split())
visited_list = list(map(int, input().split()))

window = sum(visited_list[:X])
result = window
cnt = 1
for i in range(N - X):
    window = window - visited_list[i] + visited_list[i + X]
    if result < window:
        result = window
        cnt = 1
    elif result == window:
        cnt += 1

if result:
    print(result)
    print(cnt)
else:
    print("SAD")