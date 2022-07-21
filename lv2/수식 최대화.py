import re

def solution(s):
    answer = []
    st = re.sub('},{', '}.{', s)
    st = st.split('.')

    for _ in sorted(st, key=len):
        for num in re.findall('\d+', _):
            if int(num) not in answer:
                answer.append(int(num))

    return answer