def solution(S, P, Q):
  result=[]

  #각 문자를 대응하는 숫자로 변환
  dic = {'A' : 0, 'C' : 1, 'G' : 2, 'T' : 3}
  S = list(map(lambda x : dic[x],S))

  #전체 트리 값 계산
  def func1(idx,n,k):
    if n == k:
      tree[idx]=S[n]
    else:
      mid = (n+k)//2
      tree[idx] = min(func1(idx*2+1,n,mid),func1(idx*2+2,mid+1,k))
    return tree[idx]

  l = len(S)
  tree = []
  tree[:l*4] = [-1]*l*4
  func1(0,0,len(S)-1)

  #구간에 대한 계산
  #탐색 구간은 n k
  #전체 구간은 start end
  inf = 987654321
  def func2(idx, start, end, n, k):
    if start > k  or end < n: 
      return inf
    elif start >= n and end <= k:
      return tree[idx]
    else:
      mid = (start+end)//2
      return min(func2(idx*2+1,start,mid,n,k),func2(idx*2+2,mid+1,end,n,k))

  for i in range(0,len(P)):
    result.append(func2(0,0,len(S)-1,P[i],Q[i])+1)
  return result

print(solution('CAGCCTA',[2,5,0],[4,5,6]))


