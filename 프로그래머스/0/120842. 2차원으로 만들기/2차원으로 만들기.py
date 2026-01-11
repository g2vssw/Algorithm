def solution(num_list, n):
    answer = []
    li = []
    cnt = 1
    for i in range(len(num_list)):
        if cnt == n:
            li.append(num_list[i])
            answer.append(li)
            li = []
            cnt = 1
            continue
        li.append(num_list[i])
        cnt += 1
    return answer