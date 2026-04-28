def solution(n, m):
    # 최대공약수
    a, b = max(n, m), min(n, m)
    while b:
        a, b = b, a % b
    gcd = a
    
    # 최대공배수
    lcm = (n * m) // gcd
    
    return [gcd, lcm]