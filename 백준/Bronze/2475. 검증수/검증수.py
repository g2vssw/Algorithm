li = list(map(int, input().split()))

n = 0
for num in li:
    n += num ** 2
    
print(n % 10)