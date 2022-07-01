def solution(n, m):
    prime = [i for i in range(1, min(n,m)+1) if min(n,m) % i == 0]
    answer = []

    for i in reversed(prime):
        if max(n, m) % i == 0:
            answer.append(i)
            break

    answer.append(answer[0] * (n/answer[0]) * (m/answer[0]))

    return answer