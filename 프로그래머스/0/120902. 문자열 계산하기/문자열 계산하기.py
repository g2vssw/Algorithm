def solution(my_string):
    answer = 0
    str_list = list(my_string.split())
    flag = 0
    for s in str_list:
        if s == "+":
            flag = 0
        elif s == "-":
            flag = 1
        else:
            if flag == 0:
                answer += int(s)
            else:
                answer -= int(s)
    return answer