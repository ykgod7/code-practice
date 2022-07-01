def solution(x):
    return False if x % sum([a for a in list(map(int, str(x)))]) else True