def solution(nums):
    answer = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                flag = False
                number = nums[i] + nums[j] + nums[k]
                for l in range(2, number):
                    if(number % l == 0):
                        flag = True
                        break
                if(not flag):
                    answer += 1

    return answer
