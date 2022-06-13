def solution(s):
    word_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    word = []
    st = list(s[:])

    for i in range(len(st)):
        if st[i].isalpha():
            word.append(st[i])

        if ''.join(word) in word_list:
            idx = str(word_list.index(''.join(word)))
            s = s.replace(''.join(word), idx)
            word.clear()
            
    return int(s)