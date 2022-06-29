def solution(a, b):
    return sum([num for num in range(sorted([a,b])[0], sorted([a,b])[1]+1)])