def solution(s, n):
    temp = [ord(letter) for letter in list(s)]

    for idx, num in enumerate(temp):
        if num in range(65, 91):
            temp[idx] = num + n
            if temp[idx] > 90:
                temp[idx] -= 26
        elif num in range(97, 123):
            temp[idx] = num + n
            if temp[idx] > 122:
                temp[idx] -= 26

    return ''.join([chr(num) for num in temp])