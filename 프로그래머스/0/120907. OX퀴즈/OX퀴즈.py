def solution(quiz):
    answer = []
    for q in quiz:
        a = 0
        flag = 0
        for s in list(q.split()):
            if s == "-":
                flag = 1
            elif s == "+":
                flag = 0
            elif s == "=":
                flag = 2
            else:
                if flag == 0:
                    a += int(s)
                elif flag == 1:
                    a -= int(s)
                else:
                    if a == int(s):
                        answer.append("O")
                    else:
                        answer.append("X")
    return answer