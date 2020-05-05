from functools import cmp_to_key

def compare(x, y):
	if(len(x) > len(y)): # x[0] 값이 y[0]값 보다 작으면
		return 1 # y 내용을 앞으로 보냄
	elif(len(x) < len(y)):
		return -1
	else: # x[0] 값이 y[0]값과 동일하면
		if(len(x) > len(y)): # x[1]과 y[1]을 비교해서 y[1]이 크면
			return -1 # x 내용을 앞으로 보냄
		elif(len(x) < len(y)):
			return 1
		else:
			return 0

def solution(s):
  answer = []
  s = s[2:-2].split('},{')
  s = list(map(lambda x: x.split(','),s))
  s = list(map(lambda x: list(map(int, x)),s))
  s = sorted(s,key=cmp_to_key(compare))
  
  for arr in s:
    for ele in arr:
      if ele not in answer:
        answer.append(ele)
  return answer
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))