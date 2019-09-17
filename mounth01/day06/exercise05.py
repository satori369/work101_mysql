# 在控制台录入人的信息(姓名,年龄,性别,体重)
#名称为空字符串 停止
#将所有人的信息打印
xinxi ={}
while True:
    name = input('输入姓名')
    if name == '':
        break
    else:
        age = int(input('输入年龄'))
        gender = input('输入性别')
        weight = float(input('输入体重'))

        xinxi[name] = [age, gender, weight]
print(xinxi)
for key,value in xinxi.items():
    print('%s的年龄是%d,性别是%s,体重是%.1f'%(key,value[0],value[1],value[2]))
# for name,value in xinxi.intems():
#      print('%s的年龄是%d,性别是%s,体重是%.1f' % (name, value[0],value[1],value[2],))
# list_info = []
# while True:
#     name = input('输入姓名')
#     if name =='':
#         break
#     else:
#         age = int(input('输入年龄'))
#         gender = input('输入性别')
#         weight = float(input('输入体重'))
#         #创建保存用户信息的字典
#         dict_info = {'name':name,'age':age,'gender':gender,'weight':weight}
#         #将字典添加到列表
#         list_info.append(dict_info)
# # print(list_info)
# #获取列表中的每条数据
# for dict_item in list_info:
#     print('%s的年龄是%d,性别是%s,体重是%.1f'%(dict_item['name'],dict_item['age'],dict_item['gender'],dict_item['weight']))