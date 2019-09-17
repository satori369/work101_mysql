# 3. 给ListHelper中添加新功能,并在技能列表中测试使用.
#     -- 获取最小值
#     -- 降序排列
#     -- 根据条件删除可迭代对象中的元素
#         删除技能列表中所有攻击力小于10的技能
from mounth01.day18.common.list_helper import ListHelper
from mounth01.day18.exercise01 import list01

# ListHelper.order_reverse_by(list01,lambda e:e.atk)
# for item in list01:
#     print(item.name,item.atk)



ListHelper.del_by(list01,lambda e:e.atk<7000 )
for item in list01:
    print(item.name,item.atk)