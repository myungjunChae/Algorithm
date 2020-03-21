import sys

def solution(A):
    counter = 0

    for i in range(2,len(A)):
        calc = A[i] - max(A[i-2:i]+A[i+1:i+3])
        counter += calc if calc > 0  else 0

    return counter

if __name__ == "__main__":
    sys.stdin = open("./input.txt", "r")
    for i in range(10):
        c = int(input().strip())
        array = list(map(int, input().strip().split()))
        print(f'#{i+1} {solution(array)}')
