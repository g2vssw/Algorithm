def solution(rows, columns, queries):
    answer = []
    arr = []
    value = 0
    for i in range(rows):
        temp = []
        for j in range(columns):
            value += 1
            temp.append(value)
        arr.append(temp)
        
    for query in queries:
        min_value = 21e9
        temp = 0
        x1, y1, x2, y2 = query
        for i in range(x1 - 1, x2):
            for j in range(y1 - 1, y2):
                if i == x1 - 1:
                    min_value = min(min_value, arr[i][j])
                    if j == y1 - 1:
                        temp = arr[i][j]
                        arr[i][j] = arr[i+1][j]
                    else:
                        arr[i][j], temp = temp, arr[i][j]
                elif i == x2 - 1:
                    min_value = min(min_value, arr[i][j])
                    if j == y2 - 1:
                        arr[i][j], temp = temp, arr[i][j]
                    else:
                        arr[i][j] = arr[i][j+1]
                else:
                    if j == y1 - 1:
                        min_value = min(min_value, arr[i][j])
                        arr[i][j] = arr[i+1][j]
                    elif j == y2 - 1:
                        min_value = min(min_value, arr[i][j])
                        arr[i][j], temp = temp, arr[i][j]
        answer.append(min_value)
            
    return answer