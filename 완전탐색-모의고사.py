def solution(answers):
    answer = []
    score = [0, 0, 0]
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i, num in enumerate(answers):
        if num == pattern1[i % len(pattern1)]:
            score[0] += 1
        elif num == pattern2[i % len(pattern2)]:
            score[1] += 1
        elif num == pattern3[i % len(pattern3)]:
            score[2] += 1

    for i in range(3):
        if score[i] == max(score):
            answer.append(i+1)
    return answer

# def solution(answers):
#     answer = []
#     person = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
#     nums = []
#     l = len(answers)  # [5, 5, 11]

#     for i in range(3):
#         if len(person[i]) >= l:
#             person[i] = person[i][:l]
#         else:
#             a = l // len(person[i])
#             b = l % len(person[i])
#             person[i] = person[i] * a + person[i][:b]

#     for i in range(3):
#         count = 0
#         for j in range(l):
#             if person[i][j] == answers[j]:
#                 count += 1
#         nums.append(count)

#     m = max(nums)

#     for i in range(3):
#         if nums[i] == m:
#             answer.append(i+1)

#     return answer
