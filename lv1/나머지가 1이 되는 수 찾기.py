def solution(s):
    answer = []
    if len(s) == 1:
        return len(s)
    for i in range(1, int(len(s)/2)+1):
        count, temp, word = 0, s[:i], ''
        for a  in [s[j:j+i] for j in range(0, len(s), i)]:
            if temp == a:
                count += 1
            else:
                if count > 1:
                    word += str(count) + temp
                else:
                    word += temp
                temp = a
                count = 1
        if count > 1:
            word += str(count) + temp
        else:
            word += temp
        answer.append(len(word))
    return min(answer)