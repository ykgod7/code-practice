def solution(lottos, win_nums):
    rank =[6, 6, 5, 4, 3, 2, 1]

    count = lottos.count(0)
    ans = 0

    for num in win_nums:
        if num in lottos:
            ans += 1

    return rank[count + ans], rank[ans]