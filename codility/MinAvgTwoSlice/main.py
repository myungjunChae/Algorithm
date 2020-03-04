def solution(A):
    comp = 987654321
    result = -1

    cond = len(A) - 1
    for idx, a in enumerate(A):
      if idx + 1 <= cond:
        t = sum(A[idx:idx+2])/2
        if t < comp:
          comp=t
          result=idx
      if idx + 2 <= cond:
        t= sum(A[idx:idx+3])/3
        if t < comp:
          comp=t
          result=idx

    return result
