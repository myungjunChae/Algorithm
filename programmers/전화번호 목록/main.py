def solution(phone_book):
    for i in range(0, len(phone_book)):
      length = len(phone_book[i])
      array = list(filter(lambda x : len(x) >= length,phone_book))
      array.remove(phone_book[i])

      for j in array:
        if phone_book[i] == j[0:length]:
          return False
    return True
