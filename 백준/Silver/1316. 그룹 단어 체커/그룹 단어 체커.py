N = int(input())
dat = [0] * 26
current = ''
result = 0

for _ in range(N):
    s = input()

    for word in s:
        if dat[ord(word)-97] == 0:
            dat[ord(word)-97] += 1
            current = word
        elif dat[ord(word)-97] == 1 and current == word:
            continue
        elif dat[ord(word)-97] == 1 and current != word:
            dat = [0] * 26
            break

    if dat == [0] * 26:
        continue
    else:
        result += 1
        dat = [0] * 26

print(result)