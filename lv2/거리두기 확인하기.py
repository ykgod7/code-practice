from itertools import combinations

def solution(places):
    answer = []

    for place in places:
        matrix = [list(x) for x in place]
        people = [(i, j) for i, room in enumerate(place) for j, person in enumerate(room) if person == 'P']
        combs = list(combinations(people, 2))

        for comb in combs:
            if sum([abs(a - b) for a, b in zip(comb[0], comb[1])]) <= 2:
                x, y = comb[0], comb[1] # (0, 0), (1, 1)
                
                if x[0] != y[0] and x[1] != y[1]:  # 대각선
                    if matrix[y[0]][x[1]] != 'X' or matrix[x[0]][y[1]] != 'X':
                        answer.append(0)
                        break
                else:
                    if x[0] == y[0]:
                        if matrix[x[0]][x[1]+1] != 'X':  # 가로
                            answer.append(0)
                            break
                    else: 
                        if matrix[x[0]+1][x[1]] != 'X': # 세로
                            answer.append(0)
                            break
        else:
            answer.append(1)
                
    return answer