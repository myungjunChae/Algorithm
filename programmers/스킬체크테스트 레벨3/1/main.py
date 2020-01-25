import collections

def solution(dirs):
    array=[] 
    x=5
    y=5
    dirs = list(dirs)

    while dirs:
      t = dirs.pop(0)
      t1 = int(f'{x}{y}')
      if t == 'L':
        if x == 0: 
          continue 
        x-=1
      elif t == 'R':
        if x == 10: 
          continue 
        x+=1
      elif t == 'U':
        if y == 0: 
          continue 
        y-=1
      elif t == 'D':
        if y == 10: 
          continue 
        y+=1

      t2 = int(f'{x}{y}')
      array.append(str(t2) + str(t1) if t1 > t2 else str(t1) + str(t2))
  
    return len(list(collections.Counter(array)))
