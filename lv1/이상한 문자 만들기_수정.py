def solution(s):
    return ' '.join(map(lambda x: ''.join([letter.lower() if idx % 2 else letter.upper() for idx, letter in enumerate(x)]), s.split(' ')))