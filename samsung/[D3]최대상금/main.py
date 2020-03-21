import sys 

def solution(A):
    max_cnt = A[1]
    A = list(str(A[0]))
    result = 0
    visit = []

    def dfs(curr_cnt, A):
        value = int("".join(A))
        if [value,curr_cnt] in visit:
            return
        
        visit.append([value,curr_cnt])
            
        if curr_cnt == max_cnt:
            nonlocal result 
            result = max(result, value)
            return

        for i in range(len(A)):
            for j in range(i+1,len(A)):
                A[i],A[j] = A[j],A[i]
                dfs(curr_cnt+1,A)
                A[i],A[j] = A[j],A[i]

    dfs(0,A)
    return result

if __name__ == "__main__":
    sys.stdin = open("./input.txt", "r")
    size = int(input().strip())
    for i in range(size):
        array = list(map(int, input().strip().split()))
        print(f'#{i+1} {solution(array)}')
