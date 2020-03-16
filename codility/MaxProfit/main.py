def solution(A):
    min_value=99999
    profit=0
    max_profit=0

    for i in range(1,len(A)):
      if min_value > A[i-1] :
        min_value = A[i-1]

      profit = max(0,A[i]-min_value)
      max_profit = max(max_profit,profit)

    return max_profit
