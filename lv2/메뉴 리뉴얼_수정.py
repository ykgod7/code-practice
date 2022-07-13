from collections import Counter
from itertools import combinations

def solution(orders, course):
    answer = []
    
    for num in course:
        temp = []
        for order in orders:
            temp += list(combinations(sorted(order), num))
        
        temp = Counter(temp).most_common()
        answer += [ k for k, v in temp if v > 1 and v == temp[0][1] ]

    return sorted(''.join(x) for x in answer)