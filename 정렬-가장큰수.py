def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=False)   # lamda, sort(key) 배우기
    return str(int(''.join(numbers)))
