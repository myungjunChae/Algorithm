def solution(A, B):
  alive = []

  for i,b in enumerate(B):
    if len(alive) >= 1:
      while True:
        pop = alive.pop()
        if B[pop]-B[i] == 1:
          prev = A[pop]
          curr = A[i]
          if prev > curr:
            alive.append(pop)
            break
          else:
            if len(alive):
              continue
            else:
              alive.append(i)
              break
        else:
          alive.append(pop)
          alive.append(i)
          break
    else:
      alive.append(i)

  return len(alive)
