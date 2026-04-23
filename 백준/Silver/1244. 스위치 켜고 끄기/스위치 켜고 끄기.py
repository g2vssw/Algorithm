#스위치의 갯수
numbers = int(input())
# 스위치 상태
switch = list(map(int, input().split()))
# 학생 수
N = int(input())

for n in range(N):
    #성별, 기준점
    sex, num = map(int, input().split())
    if sex == 1:
        for x in range(num-1, numbers, num):
            switch[x] = 1 - switch[x]
    elif sex == 2:
        num -= 1
        switch[num] = 1 - switch[num]
        a = 1
        while num-a >= 0 and num+a < numbers:
            if switch[num-a] == switch[num+a]:
                switch[num-a] = 1 - switch[num-a]
                switch[num+a] = 1 - switch[num+a]
                a += 1
            else:
                break

for i in range(numbers):
    print(switch[i], end=" ")
    if i % 20 == 19:
        print()