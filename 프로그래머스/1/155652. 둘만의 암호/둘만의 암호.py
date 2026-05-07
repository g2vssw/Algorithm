def solution(s, skip, index):
    answer = ''
    for c in s:
        c_c = c
        cnt = index
        while cnt > 0:
            c_c = chr(ord(c_c) + 1)
            
            if c_c > 'z':
                c_c = 'a'
                
            if c_c in skip:
                continue
            else:
                cnt -= 1
        answer += c_c
    return answer