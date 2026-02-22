import sys

input = sys.stdin.readline

def good_cheak(cheak):
    L = len(cheak)
    for i in range(1, L // 2 + 1):
        if cheak[-i:] == cheak[-i*2:-i]:
            return 0
    return 1

def permutation():

    def backtrack(seq):

        if len(seq) == N:
            return seq
        
        for s in "123":
            n_seq = seq + s
            if good_cheak(n_seq):
                result = backtrack(n_seq)
                
                if result:
                    return result

    result = backtrack("")

    return result

N = int(input())

result = permutation()

print(result)