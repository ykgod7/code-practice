# from functools import reduce


def solution(genres, plays):
    answer = []
    d = {e: [] for e in set(genres)}   # 리스트 안에 있는 값으로 리스트를 생성한는 법
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1], e[2]])
    genreSort = sorted(list(d.keys()), key=lambda x: sum(
        map(lambda y: y[0], d[x])), reverse=True)
    for g in genreSort:
        temp = [e[1]
                for e in sorted(d[g], key=lambda x: (x[0], -x[1]), reverse=True)]
        answer += temp[:min(len(temp), 2)]
    return answer


# def solution(genres, plays):
#     genre_list = list(set(genres))
#     for i in range(len(genre_list)):
#         count = 0
#         for a, b in list(zip(genres, plays)):
#             if genre_list[i] == a:
#                 count += b
#         genre_list[i] = [genre_list[i], count]
#     genre_list.sort(key=lambda x: -x[1])

#     old_list = list(zip(genres, plays, range(len(genres))))
#     old_list.sort(key=lambda x: x[1], reverse=True)
#     new_list = list()
#     id = 0
#     for i in range(len(genre_list)):
#         count = 0
#         genre = genre_list[i][0]
#         for j in range(len(genres)):
#             if genre == old_list[j][0] and count < 2:
#                 new_list.append((id, old_list[j][1], old_list[j][2]))
#                 count += 1
#         id += 1

#     answer = []
#     for i in range(len(new_list)):
#         answer.append(new_list[i][2])
#     return answer
