def solution(n):  
    return sum([a for a in range(1, n+1) if n % a == 0])