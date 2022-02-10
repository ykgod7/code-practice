def dfs(i, computers, visited):
    visited[i] = True

    for idx, val in enumerate(computers[i]):
        if val == 1 and not visited[idx]:
            dfs(idx, computers, visited)


def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    # visited = [False] * n    :  속도가 느림

    for i in range(n):
        if visited[i] == False:
            dfs(i, computers, visited)
            answer += 1

    return answer
