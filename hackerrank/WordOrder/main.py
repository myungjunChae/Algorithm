size = int(input())
t=dict()

for i in range(0, size):
  c = input()
  if c in t.keys():
    t[c] += 1
  else:
    t[c] = 1

print(f'{len(t)}')
for i in t.values():
 print(f'{i} ', end='') 
