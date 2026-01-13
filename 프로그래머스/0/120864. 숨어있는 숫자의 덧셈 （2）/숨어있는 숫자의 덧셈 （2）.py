def solution(my_string):
    answer = 0
    flag = 0
    num_str = ""
    for s in my_string:
        if s in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            num_str += s
            flag = 1
        else:
            if flag == 0:
                continue
            else:
                answer += int(num_str)
                num_str = ""
                flag = 0
    if num_str != "":
        answer += int(num_str)
    return answer