def solution(S):
    dic={
        '{':'}',
        '[':']',
        '(':')'
    }
    stack = []
    
    for i,s in enumerate(S):
        if s in dic.keys():
            stack.append(s)
        else:
          if len(stack) == 0:
            return 0
          if s != dic[stack.pop()]:
            return 0

    return 1 if len(stack) == 0 else 0
            
print(solution('())(()'))
