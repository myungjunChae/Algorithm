def check(a,b):
  if len(a) != len(b):
    return False

  for i in range(0,len(a)):
    if b[i] == '*':
      continue
    if a[i] != b[i]:
      return False
  return True

def solution(user_id, banned_id):
  filtering = []
  visit = []
  comb = []

  for banned in banned_id:
    filtering.append(list(filter(lambda x : check(x,banned), user_id)))

  def bfs(i,j):
    #1개 조합 완성 
    if len(filtering) <= i:
      comb.append(visit.copy())
      return

    for j in range(0,len(filtering[i])):
      user = filtering[i][j]
      if user not in visit:
        visit.append(user)
        bfs(i+1,0)
        visit.pop()
    return

  bfs(0,0)
  comb = list(map(lambda x: sorted(x),comb))
  comb = list(set(map(tuple,comb)))
  return len(comb)


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["*rodo", "*rodo", "******"]))