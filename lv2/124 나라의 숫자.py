def solution(n):
    base = ''

    while n > 0:
        n, mod = divmod(n-1, 3)
        if mod == 0:
            mod = 1
        elif mod == 1:
            mod = 2
        else:
            mod = 4
        base += str(mod)


    return base[::-1]