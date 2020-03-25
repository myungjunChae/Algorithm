import sys 

def solution(num, A):

    A = sorted(A)
    max_value = A[-1]
    max_index = len(A)-1

    min_value = A[0]
    min_index = 0

    while num:
        if max_value == A[max_index] and min_value == A[min_index]:
            A[max_index]-=1
            max_index-=1

            A[min_index]+=1
            min_index+=1
        else:
            if max_value != A[max_index]:
                max_index = len(A)-1
                max_value = A[max_index]

            if min_value != A[min_index]:
                min_index = 0
                min_value = A[min_index]
            
            continue

        num-=1

    A = sorted(A)
    return A[-1] - A[0]

if __name__ == "__main__":
    sys.stdin = open("./input.txt", "r")
    for i in range(0,10):
        num = int(input().strip())
        array=list(map(int, input().strip().split()))
        print(f'#{i+1} {solution(num,array)}')
