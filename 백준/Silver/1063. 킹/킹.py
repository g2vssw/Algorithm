import sys

input = sys.stdin.readline

di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]

d_dict = {
        "T": 0,
        "RT": 1,
        "R": 2,
        "RB": 3,
        "B": 4,
        "LB": 5,
        "L": 6,
        'LT': 7,
        }

i_change_dict = {
                "A": 0,
                "B": 1,
                "C": 2,
                "D": 3,
                "E": 4,
                "F": 5,
                "G": 6,
                "H": 7
                }

i_change_reverse_dict = {
                0: "A",
                1: "B",
                2: "C",
                3: "D",
                4: "E",
                5: "F",
                6: "G",
                7: "H"
                }

# 킹의 위치 K, 돌의 위치 R, 움직이는 횟수 N
K, R, N = input().split()
N = int(N)

C = [[8 - int(K[1]), i_change_dict[K[0]]], [8 - int(R[1]), i_change_dict[R[0]]]]

d_list = []
for _ in range(N):
    d = input().strip()
    d_list.append(d)

for d in d_list:
    k = d_dict[d]
    ki, kj = C[0]
    nki, nkj = ki + di[k], kj + dj[k]
    if nki < 0 or nki >= 8 or nkj < 0 or nkj >= 8:
        continue
    elif nki == C[1][0] and nkj == C[1][1]:
        ri, rj = C[1]
        nri, nrj = ri + di[k], rj + dj[k]
        if nri < 0 or nri >= 8 or nrj < 0 or nrj >= 8:
            continue
        C[1][0], C[1][1] = nri, nrj
        C[0][0], C[0][1] = nki, nkj
    else:
        C[0][0], C[0][1] = nki, nkj

for i, j in C:
    print(f'{i_change_reverse_dict[j]}{8 - i}')