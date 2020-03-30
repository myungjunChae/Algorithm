import sys 

def solution(A):
    result = 0
    #horizontal
    for a in A:
        n = len(a)
        for i in range(0,n):
            for j in range(n-1,i,-1):
                if a[i] == a[j]:
                    t = a[i:j+1]
                    if t == t[::-1]:
                        result = max(result, len(a[i:j+1]))

    vertical = []
    for i in range(0,len(A)):
        t = ''
        for j in range(0,len(A)):
            temp = A[j][i]
            t+=temp
        vertical.append(t)

    #vertical
    for a in vertical:
        n = len(a)
        for i in range(0,n):
            for j in range(n-1,i,-1):
                if a[i] == a[j]:
                    t = a[i:j+1]
                    if t == t[::-1]:
                        result = max(result, len(a[i:j+1]))

    return result

if __name__ == "__main__":
    sys.stdin = open("./input.txt", "r")
    for i in range(0,10):
        num = int(input().strip())
        array=[]
        for j in range(0,100):
            t=input().strip().split()[0]
            array.append(t)
        print(f'#{i+1} {solution(array)}')
