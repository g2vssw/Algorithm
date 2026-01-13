def solution(s):
    answer = []
    black_list = set()
    for ss in s:
        if ss in black_list:
            continue
        if ss in answer:
            answer.remove(ss)
            black_list.add(ss)
            continue
        answer.append(ss)
    answer.sort()
    return "".join(answer)