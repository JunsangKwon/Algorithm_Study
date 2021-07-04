def solution(nums):
    answer = len(nums)//2
    tmp_set = set(nums)
    nums = list(tmp_set)
    if len(nums) < answer:
        answer = len(nums)

    return answer
