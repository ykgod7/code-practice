from itertools import combinations

def solution(nums):
    def prime(num):
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    return [prime(sum(c)) for c in combinations(nums, 3)].count(True)