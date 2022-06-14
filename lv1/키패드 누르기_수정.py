def solution(numbers, hand):
    answer = ''
    
    dic = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
        '*': [3, 0], 0: [3, 1], '#': [3, 2]
    }
    
    left, right = dic['*'], dic['#']
    
    for num in numbers:
        now = dic[num]
        
        if num in [1, 4, 7]:
            answer += 'L'
            left = dic[num]
        elif num in [3, 6, 9]:
            answer += 'R'
            right = dic[num]
        else:
            left_d, right_d = 0, 0
        
            for a, b, c in zip(left, right, now):
                left_d += abs(a - c)
                right_d += abs(b - c)
                
            if left_d > right_d:
                answer += 'R'
                right = dic[num]
            elif left_d < right_d:
                answer += 'L'
                left = dic[num]
            else:
                if hand == 'left':
                    answer += 'L'
                    left = dic[num]
                else:
                    answer += 'R'
                    right = dic[num]
    return answer