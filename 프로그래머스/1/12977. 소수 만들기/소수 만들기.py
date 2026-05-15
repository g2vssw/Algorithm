def solution(nums):
    answer = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                num = nums[i] + nums[j] + nums[k]
                flag = 1
                for l in range(2, int(num ** 0.5) + 1):
                    if num % l == 0:
                        flag = 0
                        break
                if flag:
                    answer += 1
    return answer