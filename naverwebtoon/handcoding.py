def func1(value):
  t = list(value)
  arr = []
  for i in t:
    arr.append(i)

    if len(arr) >= 2:
      if arr[-2] == '(' and arr[-1] != arr[-2]:
        arr.pop()
        arr.pop()

  return len(arr) == 0

def func2(value):
  if value <= 0:
    return 0
  
  return func2(value-1) + value

def func3(value):
  stack = ""
  upper = False
  for i, ele in enumerate(value):
    if upper == True:
      upper = False
      stack += ele.upper()
      continue

    if ele == "_":
      upper = True
    else:
      stack += ele
      
  return stack

def fun4(value):
  limit = value**2
  arr1 = [f'{i+1}' for i in range(0,limit)]
  arr2 = [arr1[i:i+value] for i in range(0,limit,value)] 
  for i,arr in enumerate(arr2):
    if i % 2 != 0:
      print(" ".join(arr[::1]))
    else:
      print(" ".join(arr))    
fun4(6)