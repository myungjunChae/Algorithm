import sys 

def solution(A):
    x = 1
    y = 1
    visit = [[0 for i in range(0,16)] for j in range(0,16)]
    def dfs(x,y):
        #end 조건
        if A[x][y-1]==3 or A[x][y+1]==3 or A[x-1][y]==3 or A[x+1][y]==3:
            return 1

        if y-1 >= 0 and A[x][y-1] == 0 and visit[x][y-1] == 0:
            visit[x][y-1]=1
            if dfs(x,y-1) == 1:
                return 1
        if y+1 <= 15 and A[x][y+1] == 0 and visit[x][y+1] == 0:
            visit[x][y+1]=1
            if dfs(x,y+1) == 1:
                return 1
        if x-1 >= 0 and A[x-1][y] == 0 and visit[x-1][y] == 0:
            visit[x-1][y]=1
            if dfs(x-1,y) == 1:
                return 1
        if x+1 <= 15 and A[x+1][y] == 0 and visit[x+1][y] == 0:
            visit[x+1][y]=1
            if dfs(x+1,y) == 1:
                return 1
        
        return 0

    return dfs(x,y)

if __name__ == "__main__":
    sys.stdin = open("./input.txt", "r")
    for i in range(0,10):
        num = int(input().strip())
        array=[]
        for j in range(0,16):
            t=list(map(int,input().strip()))
            array.append(t)
        print(f'#{i+1} {solution(array)}')
