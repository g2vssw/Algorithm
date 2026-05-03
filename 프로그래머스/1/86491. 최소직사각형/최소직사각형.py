def solution(sizes):
    num1, num2 = -1, -1
    for size in sizes:
        w, h = size[0], size[1]
        if w >= h:
            num1 = max(num1, w)
            num2 = max(num2, h)
        else:
            num1 = max(num1, h)
            num2 = max(num2, w)
    answer = num1 * num2
    return answer