def solution(X, Y):
    answer = ''
    for i in range(9, -1, -1):
        t = str(i)
        cnt_x = X.count(t)
        cnt_y = Y.count(t)
        cnt_com = min(cnt_x, cnt_y)
        answer += t * cnt_com
        
    if not answer:
        answer = "-1"
    elif answer[0] == "0":
        answer = "0"
    return answer