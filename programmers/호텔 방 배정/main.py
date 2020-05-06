# 모범 답안
# def solution(k, room_number):
#     room_dic = {}
#     ret = []
#     for i in room_number:
#         n = i
#         visit = [n]
#         while n in room_dic:
#             n = room_dic[n]
#             visit.append(n)
#         ret.append(n)
#         for j in visit:
#             room_dic[j] = n+1
#     return ret

def find_room(x, rooms):
  if x not in rooms:
    rooms[x] = x + 1
    return x
  y = find_room(rooms[x], rooms)
  rooms[x] = y+1
  return y
  

def solution(k, room_number):
  result=[]
  rooms = dict()
  for room in room_number:
    result.append(find_room(room, rooms))
  
  return result