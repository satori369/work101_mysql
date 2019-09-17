import re

f = open('exc.txt','r')

fr = f.read()

rlist= re.split(r'\n\n',fr)

# /0/2/1.25
# 192.168.100.254/24
regex = re.compile(r'^(\S+)',flags=re.M)
regex2 = re.compile(r'[0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4}')
for i in rlist:
    l = regex.findall(i)
    print(l)

for i in rlist:
    l = regex2.findall(i)
    print(l)
# # 正则对象调用
# regex = re.compile(pattern)
# l = regex.findall(s,0,10)
# print(l)