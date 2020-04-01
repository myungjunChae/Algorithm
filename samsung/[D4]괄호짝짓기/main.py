import sys 

def solution(A):
    stack = []
    dic = {
        '{':'}',
        '(':')',
        '[':']',
        '<':'>'
    }

    for a in A[0]:
        if a in dic:
            stack.append(a)
        elif a in dic.values():
            if len(stack) > 0:
                if dic[stack[-1]] == a:
                    stack.pop()
                else:
                    return 0
    
    return 1 if len(stack)==0 else 0
if __name__ == "__main__":
    sys.stdin = open("./input.txt", "r")
    for i in range(0,10):
        temp = input()
        array = input().strip().split()
        print(f'#{i+1} {solution(array)}')
