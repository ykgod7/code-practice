from functools import reduce
from collections import Counter


def solution(clothes):
    cnt = Counter([kind for val, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer

# 반복문 [x for x, y in list]  ==> [x[0]. x[1], x[2]]
# reduce 함수 : 여러 개의 데이터를 대상으로 누적 집계를 내기 위해 사용
# reduce(함수, 순회 가능 데이터, 초기값)


# def solution(clothes):
#     total = dict()
#     count = 0

#     for x, y in clothes:
#         if y not in total:
#             total[y] = [x]
#         else:
#             total[y].append(x)

#     if len(total.keys()) > 1:
#         count += 1
#         for _ in total.keys():
#             count *= (len(total[_])+1)
#         count -= 1
#     else:
#         count = len(clothes)

#     return count
