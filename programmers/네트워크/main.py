def solution(n, computers):
  visit = [-1 for i in range(0,len(computers))]
  count = 0

  def dfs(i):
    visit[i] = count
    for j in range(0,n):
      if i == j:
        continue 
      if computers[i][j] == 1 and visit[j] == -1:
        dfs(j)

  for i in range(0,n):
    if(visit[i] == -1):
      dfs(i) 
      count += 1

  return len(set(visit))
