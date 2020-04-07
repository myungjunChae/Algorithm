import sys 
from functools import reduce

def solution(A):
    A = list(map(int,A.split('+')))
    A = reduce(lambda x,y: x+y, A)
    return A
if __name__ == "__main__":
    sys.stdin = open("./input.txt", "r")
    for i in range(0,10):
        temp = input()
        array = input().strip().split()
        print(f'#{i+1} {solution(array[0])}')
