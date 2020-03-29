import sys 

def solution(find, A):
    return A.count(find)
        
if __name__ == "__main__":
    sys.stdin = open("./input.txt", "r")
    for i in range(0,10):
        index = int(input().strip())
        find = input().strip()
        A = input().strip()
        print(f'#{i+1} {solution(find,A)}')
