#打印所有城市的美食
dict_info = {
    "北京":{
        "美食":['烤鸭','豆汁','卤煮','炸酱面'],
        '景区':['故宫','天安门','天坛'],
    },
    "四川":{
        "美食":['火锅','串串','毛血旺'],
        '景区':['峨眉山','九寨沟','春熙路'],
    }
}
def liebiao(dict_info):
    for key in dict_info:
        for item in dict_info[key]['美食']:
            print('%s的美食有：' % key,item)
        for item2 in dict_info[key]['景区']:
            print('%s的景区有：' % key, item2)

liebiao(dict_info)