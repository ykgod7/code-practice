def solution(n, arr1, arr2):
    answer = []
    
    for a, b in zip(arr1, arr2):
        st = bin(a|b)[2:]
        st = st.rjust(n, '0')
        st = st.replace('1', '#').replace('0', ' ')
        answer.append(st)
    return answer