'''
字符串相关方法(函数)
语法：
字符串.函数()
'''
#判断
# str1 = 'this is a test string'
# #判断字符串中是不是全都为空白
# print(str1.isspace())
# #判断字符串中是不是全都为数字类型
# num_str = '123456'
# print(num_str.isdigit())
# #判断字符串是否以xx开头
# print(str1.startswith('this'))
# #判断字符串是否以xx结尾
# print(str1.endswith('ing'))

#查找
# str1 = '01234'
#查找指定字符串  返回索引值
# print(str1.find('0'))
# #如果没找到返回-1
# print(str1.find('5'))
# #可以指定开始索引和结束索引 不包含结束索引
# print(str1.find('4',0,4))#0 1 2 3  ->  -1

# str2 = 'this is a test string'
# #       012345678
# print(str2.count('t'))
# #可以指定范围 没找到返回0
# print(str2.count('e',0,9))#0

#修改
#替换 将旧的字符串替换成新的字符串
# str1 = 'this is a test string'
# print(str1.replace('is','are'))
# #替换 最多换1次
# print(str1.replace('is','are',1))
# #如果指定的旧的字符串不存在 就什么都不做
# print(str1.replace('there','that'))

# str1 = ' hello '
# print(str1.lstrip())
# print(str1.rstrip())
# print(str1.strip())
#
# print(str1.lstrip(' h'))
# print(str1.rstrip('o '))

# str1 = 'He said'
# print(str1.lower())#转小写
# print(str1.upper())#转大写
# print(str1.swapcase())#小写转大写 大写转小写






