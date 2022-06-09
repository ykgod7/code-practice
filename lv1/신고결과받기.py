def solution(id_list, report, k):
    answer = []

    name_list = {name : [] for name in id_list}
    message_list = {name : 0 for name in id_list}

    for target in report:
        a, b = target.split()[0], target.split()[1]
        if a not in name_list[b]:
            name_list[b].append(a)

    for key, values in name_list.items():
        if len(values) >= k:
            for value in values:
                message_list[value] += 1

    return list(message_list.values())