def solution(n_str):
    answer = ''
    if n_str[0] != "0":
        return n_str
    flag = 0
    for i in range(len(n_str)):
        if flag == 0 and n_str[i] == "0":
            continue
        flag = 1
        answer += n_str[i]
    return answer