sz1 = int(input('输入一个数字'))
ysf = input('输入一个运算符:+-*/')
sz2 = int(input('输入第二个数字'))
#判断 如果用户输入的内容是+
if ysf =='+':
    print(sz1+sz2)
elif ysf =='-':
    print(sz1-sz2)
elif ysf =='*':
    print(sz1*sz2)
elif ysf =='/':
    print(sz1/sz2)
else:
    print('运算符有误')