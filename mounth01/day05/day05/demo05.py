'''
list  --> str
'''
list01 = ['a','b','c']
str01 = '+'.join(list01)
print(str01)
print(type(str01))

# str_result = ''
# for i in range(10):
#     # str_result += str(i)
#     # '' + '0'  产生新的字符串 '0'
#     # '0' + '1' 产生新的字符串 '01'
#     # '01' + '2'  产生新的字符串 '012'
#     str_result = str_result + str(i)

#思想：通过可变对象list保存所有要拼接的字符串 最后在将列表里的内容转为字符串
list_result = []
for i in range(10):
    list_result.append(str(i))

str_result = ''.join(list_result)
print(str_result)









