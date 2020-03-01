def solution(A):
    dic = dict()
    
    for a in A:
      if a in dic.keys():
        return 0
      dic[a]=1
        
    for idx, a in enumerate(sorted(list(dic))):
      if a != idx+1:
        return 0
    return 1
