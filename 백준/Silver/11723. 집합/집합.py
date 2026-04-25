import sys

input = sys.stdin.readline
m = int(input())
s = set()

for _ in range(m):
    command = input().split()
    
    if len(command) == 1:
        if command[0] == 'all':
            s = set(range(1, 21))
        else: # empty
            s.clear()
        continue
    
    op, x = command[0], int(command[1])
    
    if op == 'add':
        s.add(x)
    elif op == 'remove':
        s.discard(x) # x가 없어도 에러를 내지 않음
    elif op == 'check':
        print(1 if x in s else 0)
    elif op == 'toggle':
        if x in s:
            s.remove(x)
        else:
            s.add(x)