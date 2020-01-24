import collections

def minion_game(s):
  answer = ''
  vowels = 'AEIOU'  
  player={'Stuart':0, 'Kevin':0} #vowels

  unique = list(collections.Counter(s))
  t1 = list(filter(lambda x : x in vowels,unique)) #kevin
  length = len(s)
  for i in range(0, length):
    if s[i] in t1:
      player['Kevin'] += length-i
    else:
      player['Stuart'] += length-i

  if player['Stuart'] > player['Kevin']:
    answer = f"Stuart {player['Stuart']}"
  elif player['Stuart'] < player['Kevin']:
    answer =  f"Kevin {player['Kevin']}"
  else:
    answer = 'Draw'

  print(answer)

minion_game('BANANA')
