arr = [list(input()) for _ in range(5)]

max_len = 0
for l in arr:
    max_len = max(max_len, len(l))

result = []
for j in range(max_len):
    for i in range(5):
        try:
            result.append(arr[i][j])
        except:
            continue

print(''.join(result))