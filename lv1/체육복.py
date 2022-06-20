def solution(n, lost, reserve):
    answer = n - len(lost)
    temp = reserve[:]
    temp.sort()
    lost.sort()

    for i in reserve:
        if i in lost:
            answer += 1
            temp.remove(i)
            lost.remove(i)

    for j in temp:
        if j - 1 in lost:
            answer += 1 
            lost.remove(j-1)
        elif j + 1 in lost:
            answer += 1 
            lost.remove(j+1)

    return answer