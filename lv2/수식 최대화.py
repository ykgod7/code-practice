from itertools import permutations

def solution(expression):
    combs = list(permutations(['*', '+', '-'], 3))

    num, ex = '', []
    for _ in expression:
        if _.isdigit():
            num += _
        else:
            ex.append(num)
            ex.append(_)
            num = ''
    ex.append(num)
    temp = ex[:]
    largest = 0
    for comb in combs:
        ex = temp[:]
        for _ in comb:
            for i in range(ex.count(_)):
                idx = ex.index(_)
                if _ == '*':
                    ex[idx-1] = int(ex[idx-1]) * int(ex[idx+1])
                elif _ == '+':
                    ex[idx-1] = int(ex[idx-1]) + int(ex[idx+1])
                else:
                    ex[idx-1] = int(ex[idx-1]) - int(ex[idx+1])
                ex.pop(idx)
                ex.pop(idx)
        if abs(ex[0]) > largest:
            largest = abs(ex[0])
    return largest