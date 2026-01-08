def solution(arr):
    answer = []
    if len(arr) == len(arr[0]):
        return arr
    elif len(arr) < len(arr[0]):
        n = len(arr[0]) - len(arr)
        answer = (arr)
        for _ in range(n):
            answer.append([0 for _ in range(len(arr[0]))])
    else:
        n = len(arr) - len(arr[0])
        for i in arr:
            for _ in range(n):
                i.append(0)
            answer.append(i)
    return answer