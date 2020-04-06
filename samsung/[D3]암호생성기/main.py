import sys 

def solution(A):
    count = 0
    while True:
        if A[-1] == 0:
            break
        count+=1

        if count >= 6:
            count = 1 

        A = A[1:]+[A[0]-count] if A[0]-count >= 0 else A[1:]+[0]

    return " ".join(list(map(str,A)))

if __name__ == "__main__":
    sys.stdin = open("./input.txt", "r")
    for i in range(0,10):
        num = int(input().strip())
        t=list(map(int, input().strip().split()))
        print(f'#{i+1} {solution(t)}')
