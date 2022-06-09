def solution(id_list, report, k):
    index_list = [0] * len(id_list)
    reports = {name : 0 for name in id_list}
    
    for _ in set(report):
        reports[_.split()[1]] += 1
    
    for _ in set(report):
        if reports[_.split()[1]] >= k:
            index_list[id_list.index(_.split()[0])] += 1
    return index_list