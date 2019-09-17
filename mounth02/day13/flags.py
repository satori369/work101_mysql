'''
flags.py
扩展标志位演示
'''

import re
import select
s = """Hello
北京
"""
# 只能匹配ASCII
# regex = re.compile(r'\w+',flags=re.A)

# 忽略字母大小写
# regex = re.compile(r'[a-z]+',flags=re.I)

# .可以匹配换行了
# regex = re.compile(r'.+',flags=re.DOTALL)

# 可以匹配每行开头和结尾位置
regex = re.compile(r'^Hello$',flags=re.M)

pattern = '''\w+\s+\w+ 
# fgsjoigsjoi
#gsdjogk
'''

regex = re.compile(pattern,flags=re.X | re.I)
l = regex.findall(s)

l = regex.findall(s)
print(l)

