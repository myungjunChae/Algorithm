#본 문제를 푸는 키 요소
#징검다리의 가장 작은 수 = 최소로 건널 수 있는 횟수
#징거다리의 가장 큰 수 = 최대로 건널 수 있는 횟수

import copy
def solution(stones, k):
    _min = min(stones) #최소한 건널 수 있는 사람의 수
    _max = max(stones) #최대로 건널 수 있는 사람의 수
    _mid = (_min+_max)//2 #현재 시뮬레이션하는 사람의 수

    while _mid != _min:
        stone = copy.deepcopy(stones)
        count = 0

        for i in range(0,len(stone)):
          stone[i] -= (_mid - 1) #징검다리가 3일 때, 건널 수 있는 사람은 3이여야함. 하지만 stone - mid가 0이면, 후속 조건에 걸림. 따라서 +1
          if stone[i] <= 0:
              count += 1
          else:
              count = 0
          if count >= k:
              break

        if count >= k:
          _max = _mid
          _mid = (_min+_max)//2
        else:
          _min = _mid
          _mid = (_min+_max)//2
    
    return _mid