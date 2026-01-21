def solution(n, arr1, arr2):
    answer = []
    
    def bin_make(num):
        if num == 0:
            binary = "0" * n
            return binary
        binary = ""
        while num > 0:
            re = num % 2
            binary = str(re) + binary
            num = num // 2
        if len(binary) == n:
            return binary
        else:
            k = n - len(binary)
            binary = "0" * k + binary
            return binary
    
    for i in range(n):
        binary1 = bin_make(arr1[i])
        binary2 = bin_make(arr2[i])
        binary = ""
        for j in range(n):
            if binary1[j] == "1" or binary2[j] == "1":
                binary += "#"
            elif binary1[j] == "0" and binary2[j] == "0":
                binary += " "
        answer.append(binary)
    return answer