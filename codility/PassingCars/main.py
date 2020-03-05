# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    result = 0
    count = 0
    for i in range(len(A)-1,-1,-1):
        if A[i] == 0:
            result += count
        else:
            count +=1 
    
    return -1 if result > 1000000000 else result
