def solution(H):
  counter = 0
  stack=[]
  for h in H:
    while len(stack) > 0 and stack[-1] > h:
      stack.pop()

    if len(stack) == 0 or stack[-1] < h:
      stack.append(h)
      counter+=1
  
  return counter
