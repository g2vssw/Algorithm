def solution(str1, str2):
    str_all = set()
    
    str1_dict = {}
    for i in range(len(str1) - 1):
        if "a" <= str1[i] <= "z" or "A" <= str1[i] <= "Z":
            if "a" <= str1[i+1] <= "z" or "A" <= str1[i+1] <= "Z":
                c_s = str1[i].upper()
                n_s = str1[i+1].upper()
                str_all.add(c_s + n_s)
                str1_dict[c_s + n_s] = str1_dict.get(c_s + n_s, 0) + 1
                
    str2_dict = {}
    for i in range(len(str2) - 1):
        if "a" <= str2[i] <= "z" or "A" <= str2[i] <= "Z":
            if "a" <= str2[i+1] <= "z" or "A" <= str2[i+1] <= "Z":
                c_s = str2[i].upper()
                n_s = str2[i+1].upper()
                str_all.add(c_s + n_s)
                str2_dict[c_s + n_s] = str2_dict.get(c_s + n_s, 0) + 1
    
    inter_value = 0
    union_value = 0
    for s in str_all:
        s1 = str1_dict.get(s, 0)
        s2 = str2_dict.get(s, 0)
 
        inter_value += min(s1, s2)
        union_value += max(s1, s2)    
                
    if union_value:
        answer = int((inter_value / union_value) * 65536)
    else:
        answer = 65536
                
    return answer