def solution(s):
    answer = 0
    x = ""
    x_cnt, d_cnt = 0, 0
    for c in s:
        if x == "":
            x = c
            x_cnt += 1
        elif c == x:
            x_cnt += 1
        else:
            d_cnt += 1
            if x_cnt == d_cnt:
                x = ""
                x_cnt, d_cnt = 0, 0
                answer += 1
    if x != "":
        answer += 1 
    return answer