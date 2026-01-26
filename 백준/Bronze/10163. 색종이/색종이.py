N = int(input())
arr= [[0] * 1001 for _ in range(1001)]

for num in range(1, N + 1):
    si, sj, w, h = map(int, input().split())
    ei, ej = si + w, sj + h
    for i in range(si, ei):
        for j in range(sj, ej):
            arr[i][j] = num
    
answer = [0] * (N + 1)
for i in range(1001):
    for j in range(1001):
        if arr[i][j] != 0:
            answer[arr[i][j]] += 1

for num in range(1, N + 1):
    print(answer[num])