bowls = input()

result = 0
cheak = ""
for bowl in bowls:
    if cheak == "":
        cheak = bowl
        result += 10
        continue
    if cheak == bowl:
        result += 5
    else:
        cheak = bowl
        result += 10

print(result)