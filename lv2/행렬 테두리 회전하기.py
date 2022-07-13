def solution(rows, columns, queries):
    answer = []
    matrix = [[j for j in range(1+i*columns, 1+columns+i*columns)] for i in range(rows)]
    
    for x1, x2, x3, x4 in queries:
        tmp = matrix[x1-1][x2-1]
        min_num = []
        min_num.append(tmp)
        
        for i in range(x1-1, x3-1):
            min_num.append(matrix[i+1][x2-1])
            matrix[i][x2-1] = matrix[i+1][x2-1]
        
        for i in range(x2-1, x4-1):
            min_num.append(matrix[x3-1][i+1])
            matrix[x3-1][i] = matrix[x3-1][i+1]
        
        for i in reversed(range(x1, x3)):
            min_num.append(matrix[i-1][x4-1])
            matrix[i][x4-1] = matrix[i-1][x4-1]
        
        for i in reversed(range(x2, x4)):
            min_num.append(matrix[x1-1][i-1])
            matrix[x1-1][i] = matrix[x1-1][i-1]
        
        matrix[x1-1][x2] = tmp
        answer.append(min(min_num))

    return answer