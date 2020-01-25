def solution(n):
    answer = ''
    while n:
        n, mod = divmod(n,3)
        answer = '412'[mod] + answer
        if not mod:
            n-=1
    return answer
