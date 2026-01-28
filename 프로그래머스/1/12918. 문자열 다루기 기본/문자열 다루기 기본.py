def solution(s):
    answer = True
    if len(s) not in [4, 6]:
        answer = False
    else:
        for cheak in s:
            if cheak not in "0123456789":
                answer = False
    return answer