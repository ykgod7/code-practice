def solution(d, budget):
    answer = 0
    
    for i in range(len(d)):
        if answer + sorted(d)[i] > budget:
            return i
        answer += sorted(d)[i]

    return i + 1