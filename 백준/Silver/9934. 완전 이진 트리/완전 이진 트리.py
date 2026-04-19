def binary_tree(i, arr):
    mid = len(arr) // 2
    trees[i].append(arr[mid])

    left = arr[:mid]
    right = arr[mid + 1:]

    if len(arr) == 1:
        return

    binary_tree(i + 1, left)
    binary_tree(i + 1, right)

K = int(input())
sequence = list(map(int, input().split()))
trees = [[] for _ in range(K)]

binary_tree(0, sequence)

for tree in trees:
    print(*tree)