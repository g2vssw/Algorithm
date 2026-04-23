def nanugi(K, L):
    if K % 2 == 1:
        K = (K + 1) // 2
    elif K % 2 == 0:
        K = K // 2

    if L % 2 == 1:
        L = (L + 1) // 2
    elif L % 2 == 0:
        L = L // 2

    pandan(K, L)

def pandan(K, L):
    global cnt
    if K == L:
        return cnt
    else:
        cnt += 1
        nanugi(K, L)

N, K, L = map(int, input().split())
cnt = 0
pandan(K, L)
print(cnt)