'''
    使用装饰器,为下列功能添加验证权限的功能
'''

def print_yzqx(func):
    def yzqx(*args, **kwargs):
        print('验证权限')
        return func(*args, **kwargs)
    return yzqx

@print_yzqx
def enter_background():
    print('进入后台')

@print_yzqx
def delete_order():
    print('删除订单')

enter_background()

delete_order()
