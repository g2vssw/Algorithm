def solution(my_string):
    my_list = sorted(list(my_string.lower()))
    answer = "".join(my_list)
    return answer