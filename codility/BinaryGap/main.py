# 커스텀 진법 변환
# def bi_conv(num):
#   T="01"
#   q,r = divmod(num,2)
#   if q == 0:
#     return T[r]
#   else:
#     return bi_conv(q) + T[r]

def solution(N):
  max=0
  count=0
  bi = bin(N)[2:]
  for b in bi:
    b=int(b)
    if b == 1:
      if max < count:
        max = count
      count=0
    elif b == 0:
      count = count+1

  return max
