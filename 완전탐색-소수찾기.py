from itertools import permutations


def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map(''.join, permutations(n, i+1))))

    a -= set(range(0, 2))

    for i in range(2, int(max(a)**0.5) + 1):
        a -= set(range(i*2, max(a) + 1, i))
    return len(a)

# permutations : 리스트 안에 있는 모든 원소 경우의 수를 반환
# set() 함수를 에라토스테네스의 체와 함께 사용하여 효율적으로 소수 찾기. range(2, max)

# import itertools

# def solution(numbers):
#     temp, answer = list(), 0
#     for i in range(1, len(numbers)+1):
#         temp.append(list(map(int, list(map(''.join, itertools.permutations(numbers, i))))))
#     num_list = list(set(sum(temp, [])))

#     for num in num_list:
#         state = True
#         if num > 1:
#             for i in range(2, num//2 + 1):
#                 if num % i == 0:
#                     state = False
#                     break

#             if state == True:
#                 answer += 1

#     return answer
