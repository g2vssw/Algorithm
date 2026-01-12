def solution(my_string):
    answer = 0
    for s in my_string:
        if s in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            answer += int(s)
    return answer