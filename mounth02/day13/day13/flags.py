"""
flags.py
扩展标志位演示
"""

import re

s = """Hello
北京
"""

# 只能匹配ASCII编码
# regex = re.compile(r'\w+',flags=re.A)

# 忽略字母大小写
# regex = re.compile(r'[a-z]+',flags=re.I)

# . 可以匹配换行
# regex = re.compile(r'.+',flags=re.S)

# ^ $ 可以匹配每行开头结尾位置
# regex = re.compile(r'Hello$',flags=re.M)

pattern = '''hello # 匹配Hello
\s #匹配换行
\w+ # 匹配 北京
'''
regex = re.compile(pattern,flags=re.X | re.I)

l = regex.findall(s)
print(l)
