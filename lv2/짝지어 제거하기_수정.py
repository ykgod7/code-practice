def solution(s):
    answer = []
    for i in s:
        if not(answer):
            answer.append(i)
        else:
            if i == answer[-1]:
                answer.pop()
            else:
                answer.append(i)
    if answer:
        return 0
    else: 
        return 1