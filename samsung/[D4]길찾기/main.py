import sys 

def solution(A):
    route1=[-1]*100
    route2=[-1]*100

    for i,a in enumerate(A):
        if i%2==0:
            if route1[a] == -1:
                route1[a] = A[i+1]
            else :
                route2[a] = A[i+1]

    visit = [[0 for i in range(0,100)] for i in range(0,100)]
    def dfs(curr):
        result = 0

        if curr == 99: #길찾음 조건
            return 1

        r1 = route1[curr]
        r2 = route2[curr]

        if r1 != -1 and visit[curr][r1] == 0:
            visit[curr][r1] = 1
            if dfs(r1) == 1:
                return 1
        if route2[curr] != -1 and visit[curr][r2] == 0:
            visit[curr][r2] = 1
            if dfs(r2) == 1:
                return 1
                
        return 0 #길없음 조건
                
    return dfs(0)
    # return A

if __name__ == "__main__":
    sys.stdin = open("./input.txt", "r")
    for i in range(0,10):
        num = list(input().strip())
        array = list(map(int, input().strip().split()))
        print(f'#{i+1} {solution(array)}')
