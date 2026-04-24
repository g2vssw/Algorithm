S = input()
S2 = S.upper()
my_set_list = list(set(S2))
my_set_list.reverse()
cnt_li = [0] * len(my_set_list)

for i in range(len(my_set_list)):
    cnt_li[i] = S2.count(my_set_list[i])

if cnt_li.count(max(cnt_li)) >= 2:
    print('?')
else:
    print(my_set_list[cnt_li.index(max(cnt_li))])