# str1 = 'this is a test string'
# #判断字符串中是不是全都为空白
# print(str1.isspace())
# #判断字符串中是不是全都为数字类型
# num_str = '123456'
# print(num_str.isdigit())
# #判断字符串是否以xx开头
# print(str1.startswith('t'))
# #判断字符串是否以xx结尾
# print(str1.endswith('ing'))

# #查找
# str1 = '01234'
# # 查找指定字符串  返回索引值
# print(str1.find('0'))
# #如果没找到 返回-1
# print(str1.find('5'))
# #可指定开始索引和结束索引 不包含结束索引
# # print(str1.find('4',0,4)) #0 1 2 3-> -1
#
# str2 = 'this is a test string'
# #数一下字符串里的t有几个
# print(str2.count('t'))#字符串里有4个t 返回4
# print(str2.count('e',0,9))#0-9有0个e 返回0
#
# #修改
# #替换 将旧的字符串替换成新的字符串
# str1 = 'this is a test string'
# print(str1.replace('is','are'))
# #替换 最多换1次
# print(str1.replace('is','are',1))
# #如果指定的旧的字符串不存在 就什么都不做
# print(str1.replace('there','that',1))

# str1 = ' hello '
# print(str1.lstrip())#左边空格删掉
# print(str1.rstrip())#右边空格删掉
# print(str1.strip())#两边删掉
#
# print(str1.lstrip(' h'))
# print(str1.rstrip('o '))

str1 = 'He said'
print(str1.lower())#转小写
print(str1.upper())#转大写
print(str1.swapcase())#小写转大写 大写转小写



