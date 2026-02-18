import sys

input = sys.stdin.readline\

di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]

def reverse_othello(ci, cj, color):
    
    for k in range(8):
        ni, nj = ci + di[k], cj + dj[k]
        pos = []
        while 0 <= ni < 6 and 0 <= nj < 6 and arr[ni][nj] == color:
            pos.append((ni, nj))
            ni += di[k]
            nj += dj[k]

        if 0 <= ni < 6 and 0 <= nj < 6 and arr[ni][nj] != "." and arr[ni][nj] != color:
            for pi, pj in pos:
                if color == "W":
                    arr[pi][pj] = "B"
                else:
                    arr[pi][pj] = "W"

N = int(input())

arr = []
for i in range(6):
    row = []
    for j in range(6):
        if (i, j) in [(2, 2), (3, 3)]:
            row.append("W")
        elif (i, j) in [(2, 3), (3, 2)]:
            row.append("B")
        else:
            row.append(".")
    arr.append(row)

for i in range(N):
    R, C = map(int, input().split())
    if i % 2 == 0:
        arr[R-1][C-1] = "B"
        reverse_othello(R-1, C-1, "W")
    else:
        arr[R-1][C-1] = "W"
        reverse_othello(R-1, C-1, "B")

B_cnt = 0
W_cnt = 0
for row in arr:
    print("".join(row))
    for el in row:
        if el == "B":
            B_cnt += 1
        elif el == "W":
            W_cnt += 1

if B_cnt > W_cnt:
    print("Black")
else:
    print("White")