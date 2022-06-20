def solution(nums):
    def prime(num):
        for i in range(2, num//2 + 1):
            if num % i == 0:
                return False
        return True
            
    
    count = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                total = 0
                total = total + nums[i] + nums[j] + nums[k]
                
                if prime(total):
                    count += 1

    return count