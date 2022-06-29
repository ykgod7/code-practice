def solution(s):
    if len(s) == 4 or len(s) == 6:
        for a in s:
            if a.isalpha():
                return False
        return True
    return False