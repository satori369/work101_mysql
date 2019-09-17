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
dict_info = {
    '北京':{},
    '四川':{}
}
list03 = ['烤鸭','豆汁','卤煮','炸酱面']
list04 = ['故宫','天安门','天坛']
list05 = ['火锅','串串','毛血旺']
list06 =['峨眉山','九寨沟','春熙路']
listx =[list03,list04,list05,list06]


# def liebiao(dict_info):
for i in dict_info:
    for c in dict_info[i]['美食']:
        print('%s的美食有:' % (listx[c]))

# liebiao(dict_info)