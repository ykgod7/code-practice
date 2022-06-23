def solution(N, stages):
    dic = {}
    stages.sort()
    
    for i in range(1, N+1):
        try:
            dic[i] = stages.count(i) / (len(stages) - stages.index(i))
        except:
            dic[i] = 0
    
    return [a for a, b in sorted(dic.items(), key=lambda x: -x[1])]