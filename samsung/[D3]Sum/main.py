import sys 

def solution(A):
    result = 0
    max_value = 0
    n = len(A)
    row_list = [0] * 100
    col_list = [0] * 100
    dia_list = [0] * 2

    for i,a in enumerate(A):
        for j, value in enumerate(a):
            row_list[i]+=value
            col_list[j]+=value

            if i==j:
                dia_list[0]+=value

            if i+n == j:
                dia_list[1]+=value
    return max(row_list + col_list + dia_list)
if __name__ == "__main__":
    sys.stdin = open("./input.txt", "r")
    for i in range(0,10):
        num = int(input().strip())
        array=[]
        for j in range(0,100):
            array.append(list(map(int, input().strip().split())))
        print(f'#{i+1} {solution(array)}')
