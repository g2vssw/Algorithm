def D_sum(path):
    global result
    total = 0
    for i in range(N-1):
        total += abs(path[i] - path[i + 1])
    result = max(result, total)

def recur():
    if len(path) == N:
        D_sum(path)
        return

    for i in range(N):
        if used[i]:
            continue
        used[i] = True
        path.append(A[i])
        recur()
        path.pop()
        used[i] = False


N = int(input())
A = list(map(int, input().split()))
path = []
used = [False] * (N + 1)
result = 0
recur()

print(result)