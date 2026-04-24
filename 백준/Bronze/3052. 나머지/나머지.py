li_1 = []
for _ in range(10):
    N = int(input())
    li_1.append(N)

li_2 = []
for i in li_1:
    k = i % 42
    li_2.append(k)

print(len(set(li_2)))