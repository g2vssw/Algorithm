A = int(input())
B = int(input())
C = int(input())
cnt_li = [0] * 10

value = A * B * C
my_str = str(value)

for i in my_str:
    cnt_li[int(i)] += 1

for k in cnt_li:
    print(k)