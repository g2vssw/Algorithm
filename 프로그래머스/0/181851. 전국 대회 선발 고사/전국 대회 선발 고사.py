def solution(rank, attendance):
    li = []
    for i in range(len(rank)):
        if attendance[i] == False:
            continue
        li.append((rank[i], i))
    li.sort()
    answer = li[0][1] * 10000 + li[1][1] *100 + li[2][1]
    return answer