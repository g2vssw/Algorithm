def solution(s):
    answer = ''
    flag = 0
    for i in range(len(s)):
        if s[i] == " ":
            flag = 0
            answer += s[i]
        else:
            if flag == 0:
                answer += s[i].upper()
                flag = 1
            else:
                answer += s[i].lower()
                flag = 0
    return answer