import sys
import heapq

input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    k = int(input().strip())
    max_heap, min_heap = [],[]
    dic = {}
    for _ in range(k):
        command, num = input().strip().split()
        if command == 'I':
            heapq.heappush(max_heap, -int(num))
            heapq.heappush(min_heap, int(num))
            if int(num) in dic.keys():
                dic[int(num)] += 1
            else:
                dic[int(num)] = 1
        else:
            if int(num) == 1:
                while True:
                    if max_heap:
                        if dic[-max_heap[0]] == 0:
                            heapq.heappop(max_heap)
                        else: 
                            break
                    else:
                        break
                if max_heap:
                    dic[-heapq.heappop(max_heap)] -= 1

            else:
                while True:
                    if min_heap:
                        if dic[min_heap[0]] == 0:
                            heapq.heappop(min_heap)
                        else: 
                            break
                    else:
                        break
                if min_heap:
                    dic[heapq.heappop(min_heap)] -= 1
    # 마지막 동기화    
    while True:
            if max_heap:
                if dic[-max_heap[0]] == 0:
                            heapq.heappop(max_heap)
                else: 
                    break
            else:
                break
    while True:
        if min_heap:
            if dic[min_heap[0]] == 0:
                heapq.heappop(min_heap)
            else: 
                break
        else:
            break

    if min_heap:
        _max = -heapq.heappop(max_heap)
        _min = heapq.heappop(min_heap)
        print(_max, _min)
    else:
        print('EMPTY')