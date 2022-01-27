'''
** 재귀함수  ** 
1. 종료시점을 명시한다
2. 문제를 구체적으로 명시한다

[자기 자신을 호출하는 함수]
'''

# 하노이 타워


def func(n, _from, _to, _other):
    if n == 0:
        return
    else:
        func(n-1, _from, _other, _to)
        print(f"{n}번째 원판을 {_from}에서 {_to}으로 옮김")
        func(n-1, _other, _to, _from)


func(3, 1, 2, 3)
