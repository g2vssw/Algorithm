def solution(polynomial):
    answer = ''
    x_num = 0
    num = 0
    polynomial_list = list(polynomial.split(" + "))
    for s in polynomial_list:
        if s == "x":
            x_num += 1
            continue
        if "x" in s:
            x_num += int(s[:-1])
        else:
            num += int(s)
    if x_num != 0 and num != 0:
        if x_num == 1:
            answer = "x" + " + " + str(num)
        else:
            answer = str(x_num) + "x" + " + " + str(num)
    elif x_num != 0 and num == 0:
        if x_num == 1:
            answer = "x"
        else:
            answer = str(x_num) + "x"
    elif x_num == 0 and num != 0:
        answer = str(num)
    return answer