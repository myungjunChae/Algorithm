import sys 

def solution(A):
    dic={"ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}

    A = sorted(list(map(lambda x : dic[x],A)))

    for i,a in enumerate(A):
        for string,integer in dic.items():
            if integer == a:
                A[i] = string

    return " ".join(A)




if __name__ == "__main__":
    sys.stdin = open("./input.txt", "r")
    int(input().strip())

    for i in range(0,10):
        num = list(input().strip())
        array=list(input().strip().split())
        print(f'#{i+1} {solution(array)}')
