def solution(n):
    answer = [False, False] + [True] * (n-1)

    for i in range(2, n+1):
        if answer[i] == True:
            for j in range(2, int(i**(1/2))+1):
                if i % j == 0:
                    for a in range(i, n+1, i):
                        answer[a] = False
                    break
    return answer.count(True)