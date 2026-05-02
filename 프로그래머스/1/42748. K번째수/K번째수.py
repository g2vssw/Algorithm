def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        cmd = commands[i]
        arr = array[cmd[0] - 1:cmd[1]]
        arr.sort()
        answer.append(arr[cmd[2] - 1])
    return answer