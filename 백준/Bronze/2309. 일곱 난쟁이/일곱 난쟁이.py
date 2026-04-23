dwarf = []
for _ in range(9):
    N = int(input())
    dwarf.append(N)

dwarf.sort()
stranger_height_sum = sum(dwarf) - 100

stranger_i = 0
stranger_j = 0
for i in range(9):
    for j in range(9):
        if dwarf[i] != dwarf[j] and stranger_height_sum == dwarf[i] + dwarf[j]:
            stranger_i = i
            stranger_j = j

dwarf.pop(stranger_i)
dwarf.pop(stranger_j)

for num in dwarf:
    print(num)