def solution(lottos, win_nums):
    answer = []
    cnt_0 = 0
    cnt = 0
    for num in lottos:
        if num in win_nums:
            cnt += 1
        elif num == 0:
            cnt_0 += 1
    if cnt == 6:
        answer = [1, 1]
    elif cnt_0 == 6:
        answer = [1, 6]
    elif cnt == 0 and cnt_0 == 0:
        answer = [6, 6]
    else:
        answer.append(7 - (cnt + cnt_0))
        answer.append(7 - (cnt))
    return answer