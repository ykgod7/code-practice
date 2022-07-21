import re
from collections import Counter

def solution(s):
    st = Counter(re.findall('\d+', s))
    return list(map(int, [k for k, v in sorted(st.items(), key=lambda x: x[1], reverse=Tr