# 4. 创建打印函数运行时间的装饰器
#     def fun01():
#         ...
#
#     fun01()

import time


def print_yzqx(func):
    def yzqx(*args, **kwargs):
        time01 = time.time()
        print('验证权限')
        func(*args, **kwargs)
        time02 = time.time()
        return print(time02-time01)
    return yzqx

@print_yzqx
def enter_background():
    print('进入后台')

@print_yzqx
def delete_order():
    print('删除订单')

enter_background()
delete_order()