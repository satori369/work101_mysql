'''
file_read.py
文件读取演示
'''

#打开文件
f = open('test.txt','r')


#读操作
# while True:
#     #到文件结尾时会独处空字串
#     data = f.read(20)
#     if not data:
#         break
#     print('读取到的数据:',data)

#每次读取一行内容
# data = f.readline(5)
# print('一行内容:',data)
# data = f.readline()
# print('一行内容:',data)
# data = f.readline()
# print('一行内容:',data)

#将内容读取到一个列表
#参数表达的是读取到该字符串所在的行
data = len(f.readlines())
print(data)

# #文件对象可迭代,每次一行
# for line in f:
#     print(line)

#关闭
f.close()