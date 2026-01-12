def solution(s):
    answer = 0
    str_list = list(s.split())
    safe = 0
    for st in str_list:
        if st == "Z":
            answer -= safe
            continue
        safe = int(st)
        answer += int(st)
    return answer