def solution(nums):
    pick = len(nums) / 2
    if len(set(nums)) >= pick:
        return pick
    else:
        return len(set(nums))