list=[]
while True:
    name = input('请输入姓名')
    if name == '':
      break
    list.append(name)
for name in list:
    print(name)