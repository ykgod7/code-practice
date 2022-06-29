def solution(arr, divisor):
    temp = sorted(num for num in arr if num % divisor == 0)
    if len(temp) > 0:
        return temp
    else:
        return [-1]