'''
str字面值
'''

name = '哪吒'
name = "哪吒"

#所见即所得字符串
name = '''哪吒'''
name = """
哪
吒
"""

print(name)

str1 = '''我叫"'齐''天''大''圣'"'''
print(str1)

#c:\\

#转义字符
str4 = "我叫\"齐天大圣\""
print(str4)

str3 = 'c:\newfile\test.py'
print(str3)
#原始字符串 所以字符都只有字面意思 没有转义
str3 = r'c:\newfile\test.py'
print(str3)

