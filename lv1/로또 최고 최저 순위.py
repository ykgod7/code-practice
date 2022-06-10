def solution(lottos, win_nums):
    nums = [6,5,4,3,2,1]
    count = 0
    for num in win_nums:  
        if num in lottos:
            count += 1

    high = count + lottos.count(0)  
    low = count

    if low == 0:
        low = 1
    if high == 0:
        high = 1

    return [nums[high-1], nums[low-1]]