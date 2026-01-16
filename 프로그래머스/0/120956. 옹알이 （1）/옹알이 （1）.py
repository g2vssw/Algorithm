def solution(babbling):
    answer = 0
    for s in babbling:
        while True:
            if "aya" not in s and "ye" not in s and "woo" not in s and "ma" not in s:
                if len(s.split()) == 0:
                    answer += 1
                break
            for ba in ["aya", "ye", "woo", "ma"]:
                if ba in s:
                    s = s.replace(ba, " ")
    return answer