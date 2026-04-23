baseball = []
num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(len(num)):
    for j in range(len(num)):
        for k in range(len(num)):
            if i != j and j != k and i != k:
                baseball.append(str(num[i])+str(num[j])+str(num[k]))

N = int(input())

for _ in range(N):
    n, s, b = map(int, input().split())
    answer = str(n)

    chk = []
    for k in range(len(baseball)):
        S = 0
        B = 0
        for i in range(3):
            if answer[i] == baseball[k][i]:
                S += 1
            elif answer[i] != baseball[k][i] and answer[i] in baseball[k]:
                B += 1

        if s == S and b == B:
            chk.append(baseball[k])

    baseball = chk

print(len(chk))