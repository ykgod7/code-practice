def solution(dartResult):
    answer = []
    count, score = -1, ''
    
    for letter in dartResult:
        if letter.isdigit():
            score += letter        
        elif letter.isalpha():
            answer.append(int(score))
            score = ''
            count += 1
            if letter == 'D':
                answer[count] = answer[count]**2
            elif letter == 'T':
                answer[count] = answer[count]**3
        else:
            if letter == '*':
                if count > 0:
                    answer[count] *= 2
                    answer[count-1] *= 2
                else:
                    answer[count] *= 2
            else:
                answer[count] *= -1

    return sum(answer)