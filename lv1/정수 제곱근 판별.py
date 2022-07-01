import math

def solution(n):
    if not n % math.sqrt(n):
        return (math.sqrt(n) + 1) ** 2
    return -1