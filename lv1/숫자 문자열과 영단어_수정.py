def solution(s):
    word_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    for i in range(len(word_list)):
        s = s.replace(word_list[i], str(i))
            
    return int(s)