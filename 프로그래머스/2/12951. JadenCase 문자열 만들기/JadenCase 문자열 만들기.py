def solution(s):
    answer = ''
    words = s.split(" ") 
    
    for word in words:
        if len(word) == 0:
            answer += " "
            continue
            
        for i in range(len(word)):
            if word[i].isalpha():
                if i == 0:
                    answer += word[i].upper()
                else:
                    answer += word[i].lower()
            else:
                answer += word[i]
                
        answer += " "
        
    answer = answer[:-1]
    
    return answer