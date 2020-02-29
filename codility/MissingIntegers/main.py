def solution(A):
    result=1
    A=sorted(A)
    for a in A:
      if a==result:
        result+=1
    return result
