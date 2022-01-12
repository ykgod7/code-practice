def solution(citations):
    answer = 0

    citations.sort()

    for i in range(1, len(citations)+1):
        min_num = citations[-i]
        if min_num >= i:
            answer = i

    return answer


# def solution(citations):
#     citations.sort(reverse=True)
#     answer = max(map(min, enumerate(citations, start=1)))
#     return answer
