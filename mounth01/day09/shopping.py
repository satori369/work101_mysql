shang_pin_info = {
101:{'name':'倚天剑','price':10000},
102:{'name':'屠龙刀','price':10000},
103:{'name':'九阳神功','price':10000},
104:{'name':'九阴白骨爪','price':9999},
105:{'name':'乾坤大挪移','price':8888},
106:{'name':'七伤拳','price':7777},
}
#定义购物车清单
cart_info = []

prompt = '''************
商店
************
按1购买
按2结算
按q退出
************
'''

def selcet_menu():
    while True:
        item = input('请输入:')
        if item == 'q':
            break
        if item == '1':
            buying()
        elif item == '2':
            settlment()

#购物功能
#显示商品
#检测商品是否存在
#添加到购物车清单
def buying():
    print_info()
    create_order()
    print('添加购物车成功')


def print_info():
    print('*' * 50)
    for key, value in shang_pin_info.items():
        print('%d     %s     %d' % (key, value['name'], value['price']))
    print('*' * 50)

def check_id():
    while True:
        cid = int(input('请输入商品编号：'))
        if cid in shang_pin_info:
            break
        else:
            print('商品不存在，请重新输入！')
    return cid

def create_order():

    cid = check_id()
    count = int(input('请输入商品数量：'))

    cart_info.append({'cid': cid, 'count': count})


#结算功能
#打印购物清单
#计算总价格
#接受用户输入的金额
#支付
def settlment():
    print_order()
    total_price = calc_total_price()
    paying(total_price)


def print_order():
    print('*' * 50)
    print('购物车')
    print('*' * 50)
    for item in cart_info:
        price = shang_pin_info[item['cid']]['price']
        print('%d     %d      %d' % (item['cid'], item['count'], item['count'] * price))
    print('*' * 50)

def calc_total_price():
    zong_jia = 0
    for order in cart_info:
        price = shang_pin_info[order['cid']]['price']
        zong_jia += order['count'] * price

    return zong_jia

def paying(zong_jia):
    while True:
        money = float(input('总价为%d元，请输入金额：' % zong_jia))
        if money>=zong_jia:
            print('购买成功，找零%.2f' % (money-zong_jia))
            cart_info.clear()
            break
        else:
            print('金额不足，请重新输入')


selcet_menu()
