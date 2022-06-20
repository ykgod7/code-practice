def solution(n, lost, reserve):
    _reserve = set(reserve) - set(lost)
    _lost = set(lost) - set(reserve)
    
    for num in _reserve:
        if num - 1 in _lost:
            _lost.remove(num-1)
        elif num + 1 in _lost:
            _lost.remove(num+1) 
    
    answer = n - len(_lost)
    return answer