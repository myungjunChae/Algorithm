import sys 

def solution(A,B):
    axis = -1
    array = []
    where = -1
    for i,b in enumerate(B):
        if b == 'I':
            if where != -1:
                A = A[:where] + array + A[where:]
            axis = i
            array.clear()
        if i == axis + 1:  
            where = int(b)

        if i >= axis + 3:
            array.append(b)

    A = A[:where] + array + A[where:]
    
    return " ".join(A[:10])

if __name__ == "__main__":
    sys.stdin = open("./input.txt", "r")
    for i in range(0,10):
        t1 = input()
        t2 = input().split(" ")[:-1]
        t3 = input()
        t4 = input().split(" ")[:-1]
        print(f'#{i+1} {solution(t2,t4)}')
