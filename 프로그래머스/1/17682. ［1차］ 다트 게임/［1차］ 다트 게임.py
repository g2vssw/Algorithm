def solution(dartResult):
    answer = []
    num = 0
    for dart in dartResult:
        if dart in ["S", "D", "T"]:
            if dart == "S":
                answer.append(num)
                num = 0
            elif dart == "D":
                answer.append(num ** 2)
                num = 0
            else:
                answer.append(num ** 3)
                num = 0
        elif dart in ["*", "#"]:
            if dart == "*":
                pop1 = answer.pop() * 2
                if len(answer) != 0:
                    pop2 = answer.pop() * 2
                    answer.append(pop2)
                answer.append(pop1)
            else:
                pop1 = answer.pop() * -1
                answer.append(pop1)
        else:
            if num != 0:
                num = int(str(num) + dart)
            else:
                num = int(dart)    
    return sum(answer)