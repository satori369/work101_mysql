# 2.计算一个字符串中的字符以及字符出现的次数
# 输入 this is a test string
# t:4 h:1 i:3 s:4 a:1 e:1 r:1 n:1 g:1
# #思路
#判断字符出现的次数
#如果统计过 次数加1 如果没统计过则等于1
#setdefult()
str_target = 'this is a test string'
dict_result = {}
for ch in str_target:
    # #判断字符是否为字典中的键
    # if ch not in dict_result:
    #     #如果不是 在字典中添加键值对
    #     dict_result[ch] = 1
    # else:
    #     #在字典中 将对应的值加1
    #     # dict_result[ch] = dict_result[ch]+1
    #     dict_result[ch] += 1
    # 判断字符是否为字典中的键 如果不是添加键值对
    # 如果是 将值加1
    dict_result.setdefault(ch,0)
    dict_result[ch]+=1

print(dict_result)





