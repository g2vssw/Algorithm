L = int(input())

string = input()

M = 1234567891
r = 31

result = 0
for i in range(L):
    value = ord(string[i]) - ord('a') + 1
    result += value * (r ** i)
    
print(result % M)