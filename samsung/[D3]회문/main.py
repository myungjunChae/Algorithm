import sys 

def solution(n,A):
    count = 0
    reverse = [''] *8
    for a in A:
        a=a[0]
        for i in range(0,len(a)-n):
            t = a[i:i+n]
            if t == t[::-1]: #역순을 나타냄
                count+=1

    # for a in A:
    #     for i, value in enumerate(a[0]):
    #         reverse[i] += value
            
    # for a in reverse:
    #     a=a[0]
    #     for i in range(0,len(a)-n):
    #         t = a[i:i+n]
    #         if t == t[::-1]: 
    #             count+=1

    return count
        

    #print(n,A)
        
if __name__ == "__main__":
    sys.stdin = open("./input.txt", "r")
    for i in range(0,10):
        num = int(input().strip())
        array=[]
        for j in range(0,8):
            array.append(list(input().strip().split()))
        print(f'#{i+1} {solution(num,array)}')
