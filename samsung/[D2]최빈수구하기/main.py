import sys 
import collections

def solution(A):
    return collections.Counter(A).most_common(1)[0][0]

if __name__ == "__main__":
    sys.stdin = open("./input.txt", "r")
    size = int(input().strip())
    for i in range(size):
        temp = input()
        array = list(map(int, input().strip().split()))
        print(f'#{i+1} {solution(array)}')
