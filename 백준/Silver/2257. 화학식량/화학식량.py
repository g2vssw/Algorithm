import sys

input = sys.stdin.readline

chemical_formula = input().strip()
chemical_dict = {"H": 1, 
                 "C": 12, 
                 "O": 16}

temp = 0
stack = []
for string in chemical_formula:
    if string == "(":
        stack.append(string)
    elif string == ")":
        while True:
            s = stack.pop()
            if s == "(":
                break
            temp += s
        stack.append(temp)
        temp = 0
    elif string in ["H", "C", "O"]:
        stack.append(chemical_dict[string])
    elif string in ["2", "3", "4", "5", "6", "7", "8", "9"]:
        num = int(string)
        s = stack.pop()
        s *= num
        stack.append(s)

stack.append(temp)

print(sum(stack))