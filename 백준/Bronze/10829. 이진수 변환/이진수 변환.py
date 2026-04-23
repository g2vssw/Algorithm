def binary(n):
    if n == 0:
        return

    binary(n // 2)
    return print(n % 2, end="")

N = int(input())

binary(N)