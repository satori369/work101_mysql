"""
regex2.py
match对象属性方法演示
"""
import re

pattern = r'(ab)cd(?P<pig>ef)'
regex = re.compile(pattern)
obj = regex.search("abcdefghi",0,7)

# 属性变量
# print(obj.pos)  # 目标字符串开始位置
# print(obj.endpos) # 匹配目标结束位置
# print(obj.re) # 正则
# print(obj.string) # 目标字符串
# print(obj.lastgroup) # 最后一组组名
# print(obj.lastindex) # 最后一组序号

# 属性方法
print(obj.span()) # 匹配内容在目标字符串中的位置
print(obj.start())
print(obj.end())
print(obj.groupdict()) # 捕获组组名和对应内容字典
print(obj.groups()) # 子组对应内容
print(obj.group()) # 获取match对象内容
print(obj.group('pig'))

