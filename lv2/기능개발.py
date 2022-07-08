def solution(progresses, speeds):
    answer = []
    idx = 0
    
    while idx < len(progresses):
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        
        count = 0
        if progresses[idx] >= 100:
            for i in range(idx, len(progresses)):
                if progresses[i] >= 100:
                    count += 1
                    idx += 1
                else:
                    answer.append(count)
                    break
    answer.append(count)
            
    return answer