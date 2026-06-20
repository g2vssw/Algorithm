def to_de(n, k):
    return int(str(n), k)

def from_de(n, k):
    if n == 0:
        return 0
    
    result = ""
    while n > 0:
        result += str(n % k)
        n = n // k
    
    return int(result[::-1])
    
def solution(expressions):
    answer = []
    
    max_poss = 0
    for expr in expressions:
        for s in expr:
            if s in "0123456789":
                max_poss = max(max_poss, int(s))
    
    possible_k = set()
    for i in range(max_poss + 1, 10):
        possible_k.add(i)
        
    complete_expe = []
    incomplete_expe = []
    for expr in expressions:
        if expr[-1] == "X":
            incomplete_expe.append(expr)
        else:
            complete_expe.append(expr)
    
    fail_k = set()
    for k in possible_k:
        for expr in complete_expe:
            parts = expr.split()
            num1 = to_de(int(parts[0]), k)
            oper = parts[1]
            num2 = to_de(int(parts[2]), k)
            value = to_de(int(parts[4]), k)
            
            if oper == "+":
                check = num1 + num2
            else:
                check = num1 - num2
                
            if check != value:
                fail_k.add(k)
                break
                
    possible_k -= fail_k
    
    for expr in incomplete_expe:
        parts = expr.split()
        check_set = set()
        for k in possible_k:    
            num1 = to_de(int(parts[0]), k)
            oper = parts[1]
            num2 = to_de(int(parts[2]), k)
            
            if oper == "+":
                check = from_de(num1 + num2, k)
            else:
                check = from_de(num1 - num2, k)
            
            check_set.add(check)
    
        if len(check_set) == 1:
            value = list(check_set)[0]
        else:
            value = "?"
        
        result = f"{parts[0]} {parts[1]} {parts[2]} = {value}"
        answer.append(result)
            
    return answer