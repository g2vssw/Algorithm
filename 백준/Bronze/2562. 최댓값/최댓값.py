li = []
for _ in range(9):
    N = int(input())
    li.append(N)

print(max(li))
print(li.index(max(li))+1)