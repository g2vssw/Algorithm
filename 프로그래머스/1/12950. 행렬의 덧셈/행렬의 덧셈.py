def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        li = []
        for j in range(len(arr1[0])):
            li.append(arr1[i][j] + arr2[i][j])
        answer.append(li)
    return answer