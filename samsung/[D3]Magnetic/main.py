import sys 

def solution(A):
    # 1 = N극 = i++
    # 2 = S극 = i--
    # 무조건 2(S극)가 더 큰 row index를 가짐 (아래있음)

    # 자성이 적용된 배열을 만들 필요성이 없어서 주석처리함
    # def move(A):
    #     B = [a[:] for a in A]

    #     for i in range(0,100):
    #         for j in range(0,100):
    #             if A[i][j] == 1 and i+1 <= 99 and A[i+1][j] == 0: #N극
    #                 A[i][j] = 0
    #                 A[i+1][j] = 1
    #             elif A[i][j] == 2 and i-1 >= 0 and A[i-1][j] == 0: #S극
    #                 A[i][j] = 0
    #                 A[i-1][j] = 2

    #     if A==B:
    #         return A

    #     return move(A)

    # A=move(A)
    
    count = 0
    for j in range(0,100):
        check = False
        for i in range(99,-1,-1):
            if A[i][j] == 2:
                check = True
            elif A[i][j] == 1 and check == True:
                check = False
                count += 1


    return count
        
if __name__ == "__main__":
    sys.stdin = open("./input.txt", "r")
    for i in range(0,10):
        index = int(input().strip())
        array = []
        for j in range(0,100):
            t=list(input().strip())
            t=list(map(int,filter(lambda x: x != ' ', t)))
            array.append(t)
        print(f'#{i+1} {solution(array)}')
