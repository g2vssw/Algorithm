def solution(s):
    answer = True
    stack = []
    for c in s:
        if stack:
            if c == ")":
                if stack[-1] == "(":
                    stack.pop()
            else:
                stack.append(c)
        else:
            if c == ")":
                answer = False
                break
            else:
                stack.append(c)
    if stack:
        answer = False
    return answer