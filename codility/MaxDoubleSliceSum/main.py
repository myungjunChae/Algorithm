def solution(A):
  result = 0
  n = len(A)
  if n == 3:
    return 0

  left = [0]*n
  right = [0]*n

  for i in range(1,len(A)-1):
    left[i] = max(0, left[i-1]+A[i])

  for i in range(len(A)-2,0,-1):
    right[i] = max(0, right[i+1]+A[i])

  for i in range(1, len(A)-1):
    result = max(result, left[i-1]+right[i+1])

  return result
