def Quad_Tree(s1, s2, n, arr):
    chk = []
    for i in range(s1, n + s1):
        for j in range(s2, n + s2):
            chk.append(arr[s1][s2])
            if arr[i][j] == arr[s1][s2]:
                continue
            else:
                chk.append(arr[i][j])
                break

    if len(set(chk)) == 1:
        return chk[0]
    else:
        result = '(' + Quad_Tree(s1, s2, n // 2, arr) + Quad_Tree(s1, s2 + n // 2, n // 2, arr) + Quad_Tree(s1 + n // 2, s2, n // 2, arr) + Quad_Tree(s1 + n // 2, s2 + n // 2, n // 2, arr) + ')'
        return result

N = int(input())

arr = [list(input()) for _ in range(N)]

print(Quad_Tree(0, 0, N, arr))