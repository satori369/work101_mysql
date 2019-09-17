'''
str -->  list
'''
# str01 = '2019-08-06'
str01 = '2019/08/06'
list_result = str01.split('/')
print(list_result)

#将一句英文的单词反转
#How are you  --> you are How
#将字符串按照空格拆分成列表
#将列表反转
#将列表中的元素拼接为字符串
message = 'How are you'
temp_list = message.split(' ')
message = " ".join(temp_list[::-1])
print(message)




