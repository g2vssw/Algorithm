arr = [list(map(int, input().split())) for _ in range(9)]
max_value = 0
max_i = 0
max_j = 0


for i in range(9):
    for j in range(9):
        if max_value < arr[i][j]:
            max_value = arr[i][j]
            max_i, max_j = i, j

print(max_value)
print(max_i+1, max_j+1)