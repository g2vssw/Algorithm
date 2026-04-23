def colored_paper1(s1, s2, n):
    flag = 0
    for i in range(s1, s1 + n):
        for j in range(s2, s2 + n):
            if arr[s1][s2] == arr[i][j]:
                continue
            else:
                flag = 1
                break

    if flag == 0:
        if arr[s1][s2] == 0:
            return 1
        else:
            return 0
    else:
        return colored_paper1(s1, s2, n // 2) + colored_paper1(s1, s2 + n // 2, n // 2) + \
               colored_paper1(s1 + n // 2, s2, n // 2) + colored_paper1(s1 + n // 2, s2 + n // 2, n // 2)

def colored_paper2(s1, s2, n):
    flag = 0
    for i in range(s1, s1 + n):
        for j in range(s2, s2 + n):
            if arr[s1][s2] == arr[i][j]:
                continue
            else:
                flag = 1
                break

    if flag == 0:
        if arr[s1][s2] == 0:
            return 0
        else:
            return 1
    else:
        return colored_paper2(s1, s2, n // 2) + colored_paper2(s1, s2 + n // 2, n // 2) + \
               colored_paper2(s1 + n // 2, s2, n // 2) + colored_paper2(s1 + n // 2, s2 + n // 2, n // 2)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
print(colored_paper1(0, 0, N))
print(colored_paper2(0, 0, N))