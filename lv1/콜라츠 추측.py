def solution(num):
    for count in range(500):
        if num == 1:
            return count

        if num % 2: # 홀수라면
            num = num * 3 + 1
        else:
            num /= 2

    return -1