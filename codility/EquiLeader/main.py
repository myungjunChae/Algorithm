import collections

def solution(A):
  counter = collections.Counter(A)
  s=counter.most_common(1)[0][0]
  s_num=counter.most_common(1)[0][1]
  length=len(A)
  s_counter = 0
  result=0

  for i,a in enumerate(A):
    if a == s:
      s_counter+=1
    if s_counter > (i+1)//2:
      if s_num - s_counter > (length-(i+1))//2:
        result+=1
  
  return result
