def solution(numbers, target):
    result=0
    def core(numbers, sum):
      if len(numbers) > 0:
        t=numbers.pop(0)
        core(numbers[:],sum+t)
        core(numbers[:],sum-t)
      else:
        if sum == target:
          nonlocal result
          result+=1

    core(numbers,0)

    return result
