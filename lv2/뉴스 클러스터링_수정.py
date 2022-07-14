import math
import re

def solution(str1, str2):
    st1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if re.findall('[a-zA-Z]{2,}', str1[i:i+2])]
    st2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if re.findall('[a-zA-Z]{2,}', str2[i:i+2])]
    
    inter = set(st1) & set(st2)
    union = set(st1) | set(st2)
    
    result1 = sum([min(st1.count(num), st2.count(num))  for num in inter])
    result2 = sum([max(st1.count(num), st2.count(num))  for num in union])
    
    if result2 == 0:
        return 65536
    else:
        return math.trunc(result1 / result2 * 65536)
