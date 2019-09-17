"""
regex.py  re模块
"""

import re

s = "Alex:1997,Sunny:1996" # 目标字符串
pattern = r"(\w+):(\d+)" # 正则表达式

# re模块调用
l = re.findall(pattern,s)
print(l)

# 正则对象调用
regex = re.compile(pattern)
l = regex.findall(s,0,10)
print(l)


# 正则表达式内容切割字符串
l = re.split(r',',s)
print(l)


# 替换目标字符串
s = re.subn(r':','--',s,4)
print(s)






