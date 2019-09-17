'''
file_write.py
'''
f = open('text.txt','w')
# f = open('text.txt','ab')

#写操作
# f.write(b'hello,word\n') # 如果希望换行则自己添加
# f.write('ha呀,干啥'.encode())

#写入列表内容
l = ['hello world\n','哈哈哈\n']
f.writelines(l)

f.close()