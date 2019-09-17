'''
buffer.py
缓冲区演示
'''

f = open('test.txt','w')

while True:
    data = input('<<')
    if not data:
        break
    f.write(data+'\n')

f.close()
