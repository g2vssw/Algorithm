arr = [list(input().split()) for _ in range(9)]
manda_dict = {}
m_g = []

for i in range(3, 6):
    for j in range(3, 6):
        if i == 4 and j == 4:
            continue
        else:
            manda_dict[arr[i][j]] = []
            m_g.append(arr[i][j])

for i in range(9):
    for j in range(9):
        if i in [0, 1, 2]:
            if j in [0, 1, 2]:
                if i ==  1 and j == 1:
                    continue
                else:
                    manda_dict[arr[1][1]].append(arr[i][j])
            elif j in [3, 4, 5]:
                if i ==  1 and j == 4:
                    continue
                else:
                    manda_dict[arr[1][4]].append(arr[i][j])
            elif j in [6, 7, 8]:
                if i ==  1 and j == 7:
                    continue
                else:
                    manda_dict[arr[1][7]].append(arr[i][j])
        elif i in [3, 4, 5]:
            if j in [0, 1, 2]:
                if i ==  4 and j == 1:
                    continue
                else:
                    manda_dict[arr[4][1]].append(arr[i][j])
            elif j in [3, 4, 5]:
                continue
            elif j in [6, 7, 8]:
                if i ==  4 and j == 7:
                    continue
                else:
                    manda_dict[arr[4][7]].append(arr[i][j])
        else:
            if j in [0, 1, 2]:
                if i ==  7 and j == 1:
                    continue
                else:
                    manda_dict[arr[7][1]].append(arr[i][j])
            elif j in [3, 4, 5]:
                if i ==  7 and j == 4:
                    continue
                else:
                    manda_dict[arr[7][4]].append(arr[i][j])
            elif j in [6, 7, 8]:
                if i ==  7 and j == 7:
                    continue
                else:
                    manda_dict[arr[7][7]].append(arr[i][j])

m_g.sort()

for i in range(len(m_g)):
    print(f'#{i + 1}. {m_g[i]}')
    li = manda_dict[m_g[i]]
    li.sort()
    for j in range(len(li)):
        print(f'#{i + 1}-{j + 1}. {li[j]}')