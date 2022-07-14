import math

def solution(str1, str2):
    str1_list = [f'{x.lower()}{str1[i+1].lower()}'  for i, x in enumerate(str1) if i < len(str1) - 1 and x.isalpha() and str1[i+1].isalpha()]
    str2_list = [f'{x.lower()}{str2[i+1].lower()}'  for i, x in enumerate(str2) if i < len(str2) - 1 and x.isalpha() and str2[i+1].isalpha()]

    temp = str1_list[:]
    and_list = []

    for x in str2_list:
        if x in temp:
            temp.remove(x)
            and_list.append(x)

    try:
        return math.trunc(len(and_list) / (len(str1_list + str2_list) - len(and_list)) * 65536)
    except:
        return 65536