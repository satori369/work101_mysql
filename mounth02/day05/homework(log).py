# 3. 客户端可以循环的给服务端发送消息
#
#          一个客户端退出时如何让服务端可以继续连接下一个客户端
#
#       4. 运行程序时,写一个日志文件,格式如下
#
#          1. Fri Aug 30 17:57:45 2019
#          2. Fri Aug 30 17:57:46 2019
#          3. Fri Aug 30 17:57:47 2019
#          4. Fri Aug 30 17:57:48 2019
#          5. Fri Aug 30 17:57:58 2019
#
#         每隔一秒写依次,每个时间占一行
#
#         当程序终止运行,重写启动的时候,序列号能够衔接
import time

f = open('log.txt','a+')
fr= open('log.txt','r')

# n=0

# n = len(f.readlines())

# print(n)
for line in fr:
    if type(line)==str:
        n = int(line.split('.')[0])

while True:
    time.sleep(1)
    t = time.asctime()
    n += 1
    f.write('%d.%s\n'%(n,t))
    f.flush()

# fr.close()
# f.close()