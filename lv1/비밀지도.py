from itertools import zip_longest

def solution(n, arr1, arr2):
    answer = []
    binary_list = [[format(a, 'b')[::-1], format(b, 'b')[::-1]] for a, b in zip(arr1, arr2)]

    for binary in binary_list:
        temp = ''.join(max(str1, str2) for str1, str2 in zip_longest(binary[0], binary[1], fillvalue='0'))

        if len(temp) < n:
            while len(temp) < n:
                temp += '0'

        answer.append(temp[::-1].replace('1', '#').replace('0', ' '))

    return answer