import heapq as h

def solution(scoville, K):
    answer = 0
    h.heapify(scoville)
    while scoville[0] < K:
      try:
        h.heappush(scoville, h.heappop(scoville)+h.heappop(scoville)*2)
        answer += 1
      except:
        return -1
    return answer
