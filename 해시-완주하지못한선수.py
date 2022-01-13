def solution(participant, completion):
    participant.sort()
    completion.sort()
    completion.append('0')
    for i in range(len(participant)):
        if participant[i] != completion[i]:
            answer = participant[i]
            break

    return answer


# from collections import Counter

# def solution(participant, completion):
#     return list(Counter(participant) - Counter(completion))[0]
