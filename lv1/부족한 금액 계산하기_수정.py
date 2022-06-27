def solution(price, money, count):
    return abs(min(0, money - sum(price * i for i in range(1, count + 1))))