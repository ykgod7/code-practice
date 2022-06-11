def solution(new_id):
    new_id = list(new_id)

    temp = new_id[:] # 2번
    for letter in temp:
        if letter.isalpha() == False and letter.isdigit() == False:
            if letter != '-' and letter != '_' and letter != '.':
                new_id.remove(letter)

    idx, prev = [], '' # 3번
    for i in range(len(new_id)):  
        if new_id[i] == '.':
            if prev == '.':
                idx.append(i)
            else:
                prev = '.'
        else:
            prev = ''
    for i in idx:
        new_id[i] = ''
    new_id = list(''.join(new_id).strip())

    if new_id[0] == '.':  # 4번
        new_id.pop(0)

    if len(new_id) == 0:   # 5번
        new_id.append('a')
    if new_id[-1] == '.':  # 4번
        new_id.pop()  


    if len(new_id) > 15:
        new_id = new_id[:15]
        if new_id[-1] == '.':  # 4번
            new_id.pop()
    elif len(new_id) < 3:
        while len(new_id) < 3:
            new_id.append(new_id[-1])

    return ''.join(new_id).lower()