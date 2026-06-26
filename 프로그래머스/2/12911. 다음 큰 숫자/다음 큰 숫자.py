def solution(n):
    
    bin_n = str(bin(n)[2:])
    
    N = bin_n.count("1")
    
    m = n
    while True:
        
        m += 1
        
        bin_m = str(bin(m)[2:])
        
        M = bin_m.count("1")
        
        if M == N:
            answer = int(bin_m, 2)
            break
            
    return answer