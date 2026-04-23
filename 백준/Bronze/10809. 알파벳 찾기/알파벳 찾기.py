S = input()
dat = [-1] * 26

for i in S:
    dat[ord(i)-ord('a')] = S.index(i)
print(*dat)