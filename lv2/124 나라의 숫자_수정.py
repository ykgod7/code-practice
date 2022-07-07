def solution(n):
    num = ['1', '2', '4']
    answer = ''
    
    while n > 0:
        answer = num[(n-1) % 3] + answer
        n = (n-1) // 3
    return answer