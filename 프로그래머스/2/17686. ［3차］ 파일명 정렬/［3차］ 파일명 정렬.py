def solution(files):
    sort_file = []
    for i in range(len(files)):
        file = files[i]
        temp_tuple = []
        temp = ""
        flag = 0
        for s in file:
            if flag == 0:
                if "0" <= s <= "9":
                    flag = 1
                    temp_tuple.append(temp)
                    temp = ""
                    temp += s
                else:
                    temp += s
            elif flag == 1:
                if "0" <= s <= "9":
                    temp += s
                else:
                    flag = 2
                    temp_tuple.append(temp)
                    temp = ""
                    temp += s
            else:
                temp += s
                
        temp_tuple.append(temp)
        
        sort_file.append(temp_tuple)
        
    answer = sorted(sort_file, key=lambda x: (x[0].lower(), int(x[1])))
    answer = ["".join(item) for item in answer]
                    
    return answer