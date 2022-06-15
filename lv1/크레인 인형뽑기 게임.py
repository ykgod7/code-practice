def solution(board, moves):
    for i in range(1, len(board[0]) + 1):     # queue 생성
        globals()['queue_' + str(i)] = []

    for nums in board:      # queue에 숫자 넣기
        for i in range(len(nums)):
            if nums[i] != 0:
                eval('queue_' + str(i + 1)).append(nums[i])

    box, current, count = [], '', 0

    for num in moves:
        if not eval('queue_' + str(num)):
            current = ''
        else:
            current = eval('queue_' + str(num)).pop(0)

            if not box:
                box.append(current)
            elif current == box[-1]:          
                count += 2
                box.pop()
                if not box:
                    current = ''
            else:
                box.append(current)

    return count