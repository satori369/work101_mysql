'''
list  --> str
'''
#
# list01 = ['a','b','c']
# str01 = '你你你你的'.join(list01)
# print(str01)
# print(type(str01))

str_result = ''
for i in range(10):
    #str_result += str(i)
    str_result = str_result + str(i)
    str2 = ''.join(str_result)
print(str2)

