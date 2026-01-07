def solution(my_string, target):
    answer = my_string.find(target)
    if answer == -1:
        answer = 0
    else:
        answer = 1
    return answer