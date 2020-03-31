import sys 

def solution(result,t1,t2):
    if t2 == 0:
        return result
    return solution(result*t1,t1,t2-1)

if __name__ == "__main__":
    sys.stdin = open("./input.txt", "r")
    for i in range(0,10):
        num = int(input().strip())
        t=list(map(int, input().strip().split()))
        print(f'#{i+1} {solution(1,t[0],t[1])}')
