import bisect 

def solution(A):
    pairs = 0

    intervals = sorted( [(i-A[i], i+A[i]) for i in range(len(A))] )
    starts = [i[0] for i in intervals]

    for i in range(len(starts)):
        end = intervals[i][1]
        #starts[i]는 원의 시작점
        #end는 원의 끝점
        #두 사이에 있는 값을 찾으면 해당 원의 intersect 갯수
        count = bisect.bisect_right(starts, end)

        #본인 자신빼기
        pairs += count-1-i
        if pairs > 10000000:
            return -1
    return pairs
