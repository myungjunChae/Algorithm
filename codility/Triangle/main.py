#1차
import bisect

def solution(A):
    A = sorted(A)

    for i,a in enumerate(A):
      for j in range(i+1,len(A)-1):
        b=bisect.bisect_left(A,A[i]+A[j])
        if b > j+1:
          return 1
    return 0

#2차
def solution(A):
    A = sorted(A,reverse=True)

    for i,a in enumerate(A):
      for j in range(i+1,len(A)-1):
        t=A[i]-A[j]
        if A[j+1] > t:
          return 1
        else:
          break
    return 0
