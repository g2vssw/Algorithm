def solution(s):
    answer = []
    count = 0
    re_count = 0
    while s != "1": 
        count += 1
        cnt = 0
        for n in s:
            if n == "0":
                cnt += 1
        num = len(s) - cnt
        re_count += cnt
        s = str(bin(num)[2:])
    answer.append(count)
    answer.append(re_count)
    return answer