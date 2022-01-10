def solution(array, commands):
    answer = []

    for i, j, k in commands:
        num_list = array[i-1:j]
        num_list.sort()
        answer.append(num_list[k-1])

    return answer
