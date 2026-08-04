def solution(elements):
    arr = set()
    num = len(elements)
    elements = elements * 2
    for n in range(1, num + 1):
        for i in range(num):
            temp = sum(elements[i:i+n])
            arr.add(temp)
    return len(arr)