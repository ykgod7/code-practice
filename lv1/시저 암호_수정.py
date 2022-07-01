def solution(s, n):
    s = list(s)
    
    for idx, letter in enumerate(s):
        if letter.isupper():
            s[idx] = chr((ord(letter) + n - ord('A'))%26 + ord('A'))
        elif letter.islower():
            s[idx] = chr((ord(letter) + n - ord('a'))%26 + ord('a'))
    return ''.join(s)