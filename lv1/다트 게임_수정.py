import re

def solution(dartResult):
    option = {'S': 1, 'D': 2, 'T': 3}
    bonus = {'': 1, '*': 2, '#': -1}
    p = re.compile('(\d+)([SDT])([#*]?)')
    result = p.findall(dartResult)
    
    for i in range(len(result)):
        if result[i][2] == '*' and i > 0:
            result[i-1] *= 2
        result[i] = int(result[i][0]) ** option[result[i][1]] * bonus[result[i][2]]
          
    return sum(result)