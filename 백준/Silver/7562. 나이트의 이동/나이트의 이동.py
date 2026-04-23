T = int(input())

for _ in range(T):
    N = int(input())
    queue = [tuple((map(int, input().split())))]
    e_i, e_j = map(int, input().split())
    arr = [[0 for _ in range(N)] for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    di = [-2, -1, 1, 2, 2, 1, -1, -2]
    dj = [1, 2, 2, 1, -1, -2, -2, -1]

    while queue:
        i, j = queue.pop(0)

        if i == e_i and j == e_j:
            break

        for k in range(8):
            ni, nj = i + di[k], j + dj[k]

            if ni < 0 or ni >= N or nj < 0 or nj >= N:
                continue
            elif arr[ni][nj] == 0:
                arr[ni][nj] = arr[i][j] + 1
                queue.append((ni, nj))

    print(arr[e_i][e_j])