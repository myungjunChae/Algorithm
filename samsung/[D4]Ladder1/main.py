import sys 

def solution(A):
    j = len(A)-1
    i = -1
    for idx, a in enumerate(A[-1]):
        if a == 2:
            i = idx

    while True:
        if j == 0:
            break

        if i >= 1:
            if A[j][i-1] == 1:
                while i != 0 and A[j][i-1] != 0:
                    i-=1
                j-=1
                continue
        if i <= len(A)-2:
            if A[j][i+1] == 1:
                while i != len(A)-1 and A[j][i+1] != 0:
                    i+=1
                j-=1
                continue
        
        j-=1

    return i

if __name__ == "__main__":
    sys.stdin = open("./input.txt", "r")
    for i in range(0,10):
        num = int(input().strip())
        array=[]
        for j in range(0,100):
            array.append(list(map(int, input().strip().split())))
        print(f'#{i+1} {solution(array)}')
