N, M = map(int, input().split())
N_list = [i for i in range(N + 1)]

for _ in range(M):
    i, j = map(int, input().split())
    N_list[i], N_list[j] = N_list[j], N_list[i]

print(*N_list[1:])