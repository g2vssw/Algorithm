def solution(rsp):
    answer = ''
    for s in rsp:
        if s == "2":
            answer += "0"
        elif s == "0":
            answer += "5"
        else:
            answer += "2"
    return answer