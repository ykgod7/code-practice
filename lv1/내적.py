def solution(a, b):
    return  sum(list(num1 * num2 for num1, num2 in zip(a, b)))