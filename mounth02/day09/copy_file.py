'''
创建两个进程
分别复制上下两个部分
'''
from multiprocessing import Process
import os

filename = 'log.txt'
print(filename)
size = os.path.getsize(filename)
print(size)
# print(os.listdir('day09'))

# 上半部分
def top():
    fr = open(filename,'rb')
    fw = open('top.txt','wb')
    fw.write(fr.read(size//2))
    fr.close()
    fw.close()

def bot():
    fr = open(filename, 'rb')
    fw = open('bot.txt', 'wb')
    fr.seek(size//2)
    fw.write(fr.read())
    fr.close()
    fw.close()

p1 = Process(target=top)
p2 = Process(target=bot)

p1.start()
p2.start()
p1.join()
p2.join()