def solution(a, b):
    return sum(range(sorted([a,b])[0], sorted([a,b])[1]+1))