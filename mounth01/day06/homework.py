# 1.存储各个城市的美食与景区(不用输入) 在控制台显示
# 北京：
#    美食：烤鸭 豆汁 卤煮 炸酱面
#    景区：故宫 天安门 天坛
# 四川：
#    美食：火锅 串串 毛血旺
#    景区：峨眉山 九寨沟 春熙路
# ...
# list03 = ['烤鸭','豆汁','卤煮','炸酱面']
# list04 = ['故宫','天安门','天坛']
# list05 = ['火锅','串串','毛血旺']
# list06 =['峨眉山','九寨沟','春熙路']
# dict01 = {'北京':['美食','景区'],'四川':['美食','景区']}
# # print(dict01.get('北京')[0])
# print(dict01.setdefault(dict01.get('北京')[0],'烤鸭'))
# print(dict01)
# dict02 = ('烤鸭','豆汁','卤煮','炸酱面')



# dict01 = {'北京':[{'美食':'烤鸭 豆汁 卤煮 炸酱面'},{'景区':'故宫 天安门 天坛'}],'四川':[{'美食':'火锅 串串 毛血旺'},{'景区':'峨眉山 九寨沟 春熙路'}]}
# print(dict01)
# list01 = ['北京','四川']
# list02 = ['美食','景区']
# list03 = ('烤鸭  豆汁  卤煮  炸酱面')
# list04 = ('故宫  天安门  天坛')
# list05 = ('火锅  串串  毛血旺')
# list06 =('峨眉山  九寨沟  春熙路')
# list_x =[list03,list04,list05,list06]
# dict ={}
# for i1 in list01:
#     print(i1+str(':'))
#     for i2 in list02:
#         print('\t' + i2 + ':')
#         # for i2 in list_x:
#         #     a = i2
#         #     print(a)
#         if i1=='北京' and i2== '美食' :
#             print('      '+str(list_x[0]))
#         elif i1=='北京'and i2=='景区':
#             print('      ' + str(list_x[1]))
#         elif i1=='四川'and i2=='美食':
#             print('      ' + str(list_x[2]))
#         elif i1=='四川'and i2=='景区':
#             print('      ' + str(list_x[3]))
#-__________________________________________________-
# dict_info = {
#     '北京':{
#         '美食':['烤鸭','豆汁','卤煮','炸酱面'],
#         '景区':['故宫','天安门','天坛']
#     },
#     '四川':{
#         '美食':['火锅','串串','毛血旺'],
#         '景区':['峨眉山','九寨沟','春熙路']
#     }
# }
# #查询字典的内容
# for item in dict_info['北京']['美食']:
#     print(item)
#________________________________________________________________


# 2.计算一个字符串中的字符以及字符出现的次数
# 输入 this is a test string
# t:4 h:1 i:3 s:4 a:1 e:1 r:1 n:1 g:1
#思路
#判断字符出现的次数
#如果统计过 次数加1 如果没统计过则等于1
#setdefult()

# str1 = 'this is a test string'
# print('这句话里有%s个t'%(str1.count('t')))#字符串里有4个t
# print('这句话里有%s个h'%(str1.count('h')))
# print('这句话里有%s个i'%(str1.count('i')))
# print('这句话里有%s个s'%(str1.count('s')))
# print('这句话里有%s个a'%(str1.count('a')))
# print('这句话里有%s个e'%(str1.count('e')))
# print('这句话里有%s个r'%(str1.count('r')))
# print('这句话里有%s个n'%(str1.count('n')))
# print('这句话里有%s个g'%(str1.count('g')))

str_target = 'this is a test string'
dict_result ={}
for ch in str_target:
    # # 判断字符是否为字典中的键
    # if ch not in dict_result:
    #     #如果不是 在字典中添加键值对
    #     dict_result[ch] = 1
    # else:
    #     #在地点中将对应的值加1
    #     #dict_result[ch]=dict_result[ch]+1
    #     dict_result[ch] += 1
    dict_result.setdefault(ch,0)
    dict_result[ch]+=1
print(dict_result)










