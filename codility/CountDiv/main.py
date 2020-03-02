def solution(A, B, K):
    start = A
    count = 0
    t2 = 0
    for i in range(A,B+1):
        q,r = divmod(i,K)
        if r == 0 :
            t = B//K
            return t - q + 1 


    return count
