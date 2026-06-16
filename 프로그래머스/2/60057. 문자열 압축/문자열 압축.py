def solution(s):
    answer = 21e9
    for i in range(len(s)):
        value = 0
        cur_str = ""
        count = 1
        for j in range(0, len(s), i + 1):
            if cur_str == "":
                cur_str = s[j:j+i+1]
            else:
                if s[j:j+i+1] == cur_str:
                    count += 1
                else:
                    if count == 1:
                        value += len(cur_str)
                    else:
                        value += (len(cur_str) + len(str(count)))
                    cur_str = s[j:j+i+1]
                    count = 1
        if count == 1:
            value += len(cur_str)
        else:
            value += (len(cur_str) + len(str(count)))
        answer = min(answer, value)
    return answer