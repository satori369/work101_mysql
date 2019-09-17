msg = input('输入一个字符串')
print('第一个字符是%s' % msg[0])
print('倒数第二个字符是%s' % msg[-2])
print('前两个字符是%s' % msg[:2])
print(msg[::-1])
print(msg[1::2])




if len(msg) % 2 :
    print(msg[len(msg)//2])



