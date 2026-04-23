T = int(input())

for tc in range(1, T+1):
    R, S = input().split()
    result =''
    for i in S:
        result += i*int(R)

    print(result)