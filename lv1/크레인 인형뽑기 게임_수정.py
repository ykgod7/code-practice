def solution(board, moves):
    answer = 0
    queue = []
    
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                queue.append(board[j][i-1])
                board[j][i-1] = 0
                
                if len(queue) > 1:
                    if queue[-1] == queue[-2]:
                        queue.pop()
                        queue.pop()
                        answer += 2
                break
    return answer