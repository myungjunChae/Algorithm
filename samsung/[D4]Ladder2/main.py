import sys 

def solution(A):
    dic = dict()
    start = [i for i,a in enumerate(A[0]) if a == 1]

    for s in start:
        i=0
        j=s
        dic[s]=1
        visit = [[0]*100]*100

        while True:
            if i == len(A)-1:
                break

            if j >= 1 and A[i][j-1] == 1 and visit[i][j-1] == 0: #좌측
                visit[i][j-1] = 1
                j-=1
                dic[s] +=1 
                continue

            if j <= len(A)-2 and A[i][j+1] == 1 and visit[i][j+1] == 0: #우측
                visit[i][j+1] = 1
                j+=1
                dic[s] +=1 
                continue
            
            visit[i+1][j] = 1
            i+=1 
            dic[s] +=1 

    print(sorted(dic.items(),key=lambda x : (x[1])))
        

if __name__ == "__main__":
    sys.stdin = open("./input.txt", "r")
    for i in range(0,10):
        num = int(input().strip())
        array=[]
        for j in range(0,100):
            array.append(list(map(int, input().strip().split())))
        print(f'#{i+1} {solution(array)}')
