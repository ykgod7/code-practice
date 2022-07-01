def solution(n):
    answer = '수박'
    if n % 2 != 0:
        return answer * int(n/2) + answer[0]
    return answer * int(n/2)