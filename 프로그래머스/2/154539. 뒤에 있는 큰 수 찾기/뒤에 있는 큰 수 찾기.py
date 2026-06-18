def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    for i in range(len(numbers) - 1, -1, -1):
        c_number = numbers[i]
        while stack and stack[-1] <= c_number:
            stack.pop()
        if stack:
            answer[i] = stack[-1]
        stack.append(c_number)
    return answer