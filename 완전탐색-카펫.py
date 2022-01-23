def solution(brown, red):
    for i in range(1, int(red**(1/2))+1):
        if red % i == 0:
            if 2*(i + red//i) == brown-4:
                return [red//i+2, i+2]

# def solution(brown, yellow):
#     tot = brown + yellow
#     answer = list()

#     for i in range(3, int(tot/2) + 1):
#         if tot % i == 0 :
#             num = (tot/i, i)
#             answer.append(num)
#     for x, y in answer:
#         if (x - 1) * 2 + (y - 1) * 2 == brown:
#             answer = [y, x]
#     return answer
