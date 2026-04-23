N = int(input())

def func(num):
    if num == 1 or num == 0:
        return 1

    return num * func(num-1)

print(func(N))