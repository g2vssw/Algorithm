N = int(input())

words = set()

for _ in range(N):
    word = input()
    words.add(word)

words = list(words)
words.sort()
words.sort(key=len)

for w in words:
    print(w)