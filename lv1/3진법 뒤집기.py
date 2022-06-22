def solution(n):
    answer, total = [], 0
    while n > 2:
        answer.insert(0, n % 3)
        n = n // 3
    answer.insert(0, n)

    for i in range(len(answer)):
        total += answer[i] * (3 ** i)
    return total
