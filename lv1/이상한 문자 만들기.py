def solution(s):
    s = list(s)
    i = 0
    for idx, letter in enumerate(s):
        if letter == ' ':
            i = 0
        elif i % 2 == 0:
            s[idx] = letter.upper()
            i += 1
        else:
            s[idx] = letter.lower()
            i += 1
    return ''.join(s)