def solution(sizes):
    temp1, temp2 = 0, 0

    for size in sizes:
        a, b = sorted(size)[1], sorted(size)[0]
        if temp1 > a and temp2 > b:
            pass
        elif temp1 > b and temp2 > a:
            pass
        else:
            print(a, b, temp1, temp2)
            if a > temp1:
                temp1 = a
            if b > temp2:
                temp2 = b            
        
    return temp1 * temp2