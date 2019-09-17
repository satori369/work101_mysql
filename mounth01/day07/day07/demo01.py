#从列表中依次取10 20 30 放入到max函数中 求最大值
max_value = max([10,20,30])
#从列表中依次取name shibw 放入到dict函数 创建字典
#单独的name 无法创建字典 需要指定键值对
# dict01 = dict(['name','shibw'])

#从列表中取['name','shibw'] 将'name'作为键 'shibw'作为值 创建字典
dict01 = dict([['name','shibw']])
dict02 = dict([('name','shibw')])