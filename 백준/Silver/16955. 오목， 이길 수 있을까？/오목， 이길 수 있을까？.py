arr= [list(input()) for _ in range(10)]

di = [0, 1, 1, 1]
dj = [1, 1, 0, -1]

def cheak(arr):
    for i in range(10):
        for j in range(10):
            if arr[i][j] == ".":
                arr[i][j] = "X"
            
                for k in range(4):
                    count = 1
                    ni, nj = i + di[k], j + dj[k]
                    while 0 <= ni < 10 and 0 <= nj < 10 and arr[ni][nj] == "X":
                            count += 1
                            ni += di[k]
                            nj += dj[k]
                    
                    ni, nj = i - di[k], j - dj[k]
                    while 0 <= ni < 10 and 0 <= nj < 10 and arr[ni][nj] == "X":
                            count += 1
                            ni -= di[k]
                            nj -= dj[k]
                    
                    if count >= 5:
                        return 1
                
                arr[i][j] = "."    
    
    return 0

print(cheak(arr))