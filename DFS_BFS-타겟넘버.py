from collections import deque
from itertools import product


# deque 함수 사용
def solution(numbers, target):
    answer = 0
    queue = deque()
    n = len(numbers)

    queue.append([numbers[0], 0])
    queue.append([-1*numbers[0], 0])

    while queue:
        num, idx = queue.popleft()
        idx += 1

        if idx < n:
            queue.append([num+numbers[idx], idx])
            queue.append([num-numbers[idx], idx])
        else:
            if num == target:
                answer += 1
    return answer


# product 함수 사용
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)
