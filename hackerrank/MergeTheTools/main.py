def merge_the_tools(string, k):
  string = list(string)

  while string:
    dic=dict()
    for i in range(0,min(k, len(string))):
      dic[string.pop(0)] = 0

    temp =''
    for i in dic.keys():
      temp += str(i)
    
    print(temp)
