def solution(A):
  n=len(A)
  left=[0]*n
  right=[0]*n
  result=0

  for i in range(0,n):
    left[i] = max(0,left[i]+A[i])

  if A[-1] > 0:
    right[-1] = A[-1]
  for i in range(n-2,-1,-1):
    right[i] = max(0, right[i+1]+A[i])

  for i in range(0,n-1):
    result = max(result,left[i]+right[i+1])

  return max(A) if result==0 else result  
