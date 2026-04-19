import sys
input = sys.stdin.readline

S, P = map(int, input().split())
string = input()
a, c, g, t = map(int, input().split())
window_dicts = {"A": 0, "C": 0, "G": 0, "T": 0}
chk_dicts = {"A": a, "C": c, "G": g, "T": t}

window = string[:P]
for s in window:
    window_dicts[s] += 1
cnt = 0

if window_dicts["A"] >= chk_dicts["A"] and window_dicts["C"] >= chk_dicts["C"] and \
        window_dicts["G"] >= chk_dicts["G"] and window_dicts["T"] >= chk_dicts["T"]:
    cnt += 1


for i in range(S - P):
    window_dicts[string[i]] -= 1
    window_dicts[string[i + P]] += 1
    if window_dicts["A"] >= chk_dicts["A"] and window_dicts["C"] >= chk_dicts["C"] and \
        window_dicts["G"] >= chk_dicts["G"] and window_dicts["T"] >= chk_dicts["T"]:
        cnt += 1

print(cnt)