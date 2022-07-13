from itertools import combinations

def solution(orders, course):
    answer = []
    course_dict = {}

    for order in orders:  
        temp = []
        for num in course: 
            temp.append(list(combinations(sorted(order), num)))
        temp = sum(temp, [])

        for comb in temp:
            if comb not in course_dict:
                course_dict[comb] = 1
            else:
                course_dict[comb] += 1

    temp = {}
    for key, value in course_dict.items():
        if len(key) in course and value > 1:
            if len(key) in temp:
                if temp[len(key)][0][-1] < value:
                    temp[len(key)] = [key + (value,)]
                elif temp[len(key)][0][-1] == value:
                    temp[len(key)] += [key + (value,)]             
            else:
                temp[len(key)] = [key + (value,)]

    for key, value in temp.items():
        for i in range(len(value)):
            answer.append(''.join(value[i][:-1]))

    return sorted(answer)