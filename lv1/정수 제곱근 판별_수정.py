from math import sqrt

def solution(n):
    return -1 if sqrt(n) % 1 else (sqrt(n)+1)**2