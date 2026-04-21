def paper_number(s1, s2, n):
    global cnt_m
    global cnt_0
    global cnt_p

    flag = 0
    for i in range(s1, s1 + n):
        for j in range(s2, s2 + n):
            if arr[s1][s2] == arr[i][j]:
                continue
            else:
                flag = 1
                break

    if flag == 0:
        if arr[s1][s2] == -1:
            cnt_m += 1
            return
        elif arr[s1][s2] == 0:
            cnt_0 += 1
            return
        else:
            cnt_p += 1
            return
    else:
        paper_number(s1, s2, n // 3)
        paper_number(s1, s2 + n // 3, n // 3)
        paper_number(s1, s2 + (n // 3) * 2, n // 3)
        paper_number(s1 + n // 3, s2, n // 3)
        paper_number(s1 + n // 3, s2 + n // 3, n // 3)
        paper_number(s1 + n // 3, s2 + (n // 3) * 2, n // 3)
        paper_number(s1 + (n // 3) * 2, s2, n // 3)
        paper_number(s1 + (n // 3) * 2, s2 + n // 3, n // 3)
        paper_number(s1 + (n // 3) * 2, s2 + (n // 3) * 2, n // 3)
        return

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt_m = 0
cnt_0 = 0
cnt_p = 0
paper_number(0, 0, N)

print(cnt_m)
print(cnt_0)
print(cnt_p)