def solution(A):
    leader = -1
    if len(A) >= 1:
      sortedA = sorted(A)
      condidate = sortedA[len(sortedA)//2]
      counter = 0

      for a in sortedA:
        if a == condidate:
          counter +=1

      if counter > len(sortedA)//2:
        leader = condidate

      return leader if leader == -1 else A.index(leader)
    
    return leader
