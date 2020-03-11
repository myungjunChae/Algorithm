def solution(S):
  stack=[]
  for s in S:
    if len(stack)>=1:
      if stack[-1] == '(' and s == ')':
        stack.pop()
      else:
        stack.append(s)
    else:
      stack.append(s)

  return 1 if len(stack) == 0 else 0 
