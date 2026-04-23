N = int(input())
di = [-2, -1, 1, 2, 2, 1, -1, -2]
dj = [1, 2, 2, 1, -1, -2, -2, -1]

for _ in range(N):
    I = int(input())
    arr = [[0 for _ in range(I)] for _ in range(I)]
    si, sj = map(int, input().split())
    ei, ej = map(int, input().split())
    queue = [(si, sj)]

    while queue:
        i, j = queue.pop(0)

        if i == ei and j == ej:
            print(arr[i][j])
            break

        for k in range(8):
            ni, nj = i + di[k], j + dj[k]
            if ni < 0 or ni >= I or nj < 0 or nj >= I:
                continue
            elif arr[ni][nj] != 0:
                continue
            elif arr[ni][nj] == 0:
                queue.append((ni, nj))
                arr[ni][nj] = arr[i][j] + 1