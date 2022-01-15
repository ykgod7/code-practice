def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)):
        l = len(phone_book[i])
        try:
            if phone_book[i] == phone_book[i+1][:l]:
                answer = False
        except:
            pass

    return answer


# def solution(phoneBook):
#     phoneBook.sort()

#     for p1, p2 in zip(phoneBook, phoneBook[1:]):
#         if p2.startswith(p1):
#             return False

#     return True
