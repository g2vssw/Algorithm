def solution(s):
    answer = ''
    if len(s) % 2 == 0:
        i = len(s) // 2
        answer += s[i-1] + s[i]
    else:
        i = (len(s) - 1) // 2
        answer += s[i]
    return answer