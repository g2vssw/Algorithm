def solution(bin1, bin2):
    answer = ''
    bin0 = str(int(bin1) + int(bin2))
    flag = 0
    for i in range(-1, -len(bin0) - 1, -1):
        n = int(bin0[i])
        if n + flag == 2:
            flag = 1
            answer += "0"
        elif n + flag == 3:
            flag = 1
            answer += "1"
        elif n + flag == 1:
            flag = 0
            answer += "1"   
        elif n + flag == 0:
            flag = 0
            answer += "0"
    if flag == 1:
        answer += "1"
    return answer[::-1]