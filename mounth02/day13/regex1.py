'''
regex1.py  re模块演示
生成match对象的函数
'''

import re

s = '热烈庆祝达内17周年,2002年至今,学生60万'
pattern = r'\d+'

# 返回迭代对象
it = re.finditer(pattern,s)

# 每个match对象对应一处匹配内容
for i in it:
    print(i.group()) # 获取match对象匹配内容

# 完全匹配
# obj1 = re.findall(r'\w',s)
# obj2 = re.search(r'\w',s)
# print(obj1)
# print(obj2.group())
# obj = re.fullmatch(r'.+',s)
# print(obj.group())

# 匹配开始
obj = re.match(r'\w+',s)
print(obj.group())
#
# # 匹配第一处
obj = re.search(r'\w+',s)
print(obj.group())