N = int(input())
li = list(map(int, input().split()))
max_value = max(li)

new_li = []
for s in li:
    new_li.append(s / max_value * 100)

result = sum(new_li) / N

print(result)