def solution(my_string):
    answer = ''
    li = ['a', 'e', 'i', 'o', 'u']
    for s in my_string:
        if s in li:
            continue
        answer += s
    return answer