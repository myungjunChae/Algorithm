def solution(board, moves):
  count = 0
  stack = []

  board = list(map(list,[*zip(*board)]))

  for m in moves:
    i = m-1
    for j in range(0,len(board[i])):
      if board[i][j] != 0:
        stack.append(board[i][j])
        board[i][j] = 0
        break
    
    if len(stack)>=2 and stack[-1] == stack[-2]:
      stack.pop()
      stack.pop()
      count+=2

  return count