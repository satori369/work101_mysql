"""
空洞文件
"""
print(3+5j)

f = open('test','wb')

f.write(b'S')
f.seek(1024*1024*10,1) # 向后移动10M
f.write(b'E')

f.close()
