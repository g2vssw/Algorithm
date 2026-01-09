def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
    

def solution(numer1, denom1, numer2, denom2):
    answer = []
    numer = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2
    g = gcd(numer, denom)
    answer.append(numer/g)
    answer.append(denom/g)
    return answer