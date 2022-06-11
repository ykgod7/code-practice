'''
<< 정규식이란? >>

. ^ $ * + ? {} [] \ | ()

1. [] : 문자와 매치하는 것 
ex) [a-d]  >>>  [abcd] 문자 중 매칭되는 것

2. . : \n 을 제외한 모든 문자와 매치
ex) a.b  >>>  aab(o) a0b(o) abc(x)  a와 b 사이에 줄바꿈 외 모두 매치

3. * : 앞의 문자가 0번이상 무한대로 반복될 수 있음
ex) go*gle  >>>  ggle, gogle, google, goooooogle

4. + : 앞의 문자가 최소 1번 이상 반복되야 매치
ex) go+gle  >>>  ggle은 매치되지 않는다 

5. {m, n} : 앞의 문자가 반복되는 횟수를 정함
ex) go{2}gle, go{2,4}  >>>  google과 매치, o가 2번 이상, 4번 이하 반복되는 문자열과 매치

6. ? : 앞의 문자가 0~1번 반복되면 매치
ex) go?gle  >>>  google은 매치되지 않는다

7. | : 또는 

8. ^ : 문자열의 맨 처음과 일치함을 나타냄
ex) re.search('^Life', 'Life is too short')  >>>  True
ex) re.search('^Life', 'My Life')  >>>  False

9. $ : 문자열의 맨 끝과 일치함을 나타냄
ex) re.search('short$', 'Life is too short')  >>>  True

10. \b : 공백을 나타내는 메타문자
'''


import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^\.|\.$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^\.|\.$', '', st)
    st = st if len(st) > 2 else st + ''.join([st[-1] for i in range(3-len(st))])
    
    return st