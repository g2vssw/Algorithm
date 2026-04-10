c_li = [1, 1, 2, 2, 2, 8]
 
li = list(map(int, input().split()))
 
result = []
for i in range(6):
	result.append(c_li[i] - li[i])
 
print(*result)