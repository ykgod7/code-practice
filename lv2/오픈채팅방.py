def solution(record):
    names, answer = {}, []
    printer = {'Enter': '님이 들어왔습니다.', 'Leave': '님이 나갔습니다.'}
    
    for r in record:
        temp = r.split(' ')
        if temp[0] in ['Enter', 'Change']:
            names[temp[1]] = temp[2]
    
    for r in record:
        temp = r.split(' ')
        if r.split(' ')[0] in ['Enter', 'Leave']:
            answer.append(f'{names[temp[1]]}{printer[temp[0]]}')
            
    return answer