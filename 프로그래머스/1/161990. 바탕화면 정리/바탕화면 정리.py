def solution(wallpaper):
    N = len(wallpaper)
    M = len(wallpaper[0])
    si, sj, ei, ej = 21e8, 21e8, -1, -1
    for i in range(N):
        for j in range(M):
            if wallpaper[i][j] == "#":
                si = min(si, i)
                sj = min(sj, j)
                ei = max(ei, i + 1)
                ej = max(ej, j + 1)
    answer = [si, sj, ei, ej]
    return answer