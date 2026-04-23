def Factorial(n):
    if n == 0:
        return 1

    return n * Factorial(n-1)

N = int(input())

print(Factorial(N))