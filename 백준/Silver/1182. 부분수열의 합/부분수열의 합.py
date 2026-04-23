def partial(idx, sm, chk):
    global cnt

    if idx == N:
        if sm == S and chk > 0:
            cnt += 1
        return


    partial(idx + 1, sm + li[idx], chk + 1)
    partial(idx + 1, sm, chk)


N, S = map(int, input().split())
li = list(map(int, input().split()))
cnt = 0

partial(0, 0, 0)

print(cnt)