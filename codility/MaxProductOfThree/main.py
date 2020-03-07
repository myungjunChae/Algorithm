def solution(A):
  #candidate
  ppp=-9987654321
  ppm=-9987654321
  pmm=-9987654321
  mmm=-9987654321

  P=list((sorted(filter(lambda x : x>=0,A))))
  M=list((sorted(filter(lambda x : x<0,A))))
  lp = len(P)
  lm = len(M)
  if lp >= 3:
    ppp = P[lp-1]*P[lp-2]*P[lp-3]
  if lp >= 2 and lm >= 1:
    ppm = P[0]*P[1]*M[lm-1]
  if lp >= 1 and lm >= 2:
    pmm = P[lp-1]*M[0]*M[1]
  if lm >= 3:
    mmm = M[lm-1]*M[lm-2]*M[lm-3]

  return max([ppp,ppm,pmm,mmm])
