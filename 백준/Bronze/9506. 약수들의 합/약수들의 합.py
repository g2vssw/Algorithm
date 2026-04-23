import sys
sys.setrecursionlimit(10**6)

def divisor(n):
    global K
    if n == 1:
        return
    if N % n == 0:
        K.add(N // n)
    divisor(n-1)


while True:
    N = int(input())
    K = set()

    if N == -1:
        break

    divisor(N)
    
    li = list(K)
    li.sort()

    if sum(K) == N:
        result = ' + '.join(map(str, li))
        print(f'{N} = {result}')
    else:
        print(f'{N} is NOT perfect.')