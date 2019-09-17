
#商品模型
class ShoppingModel:
    def __init__(self, name, price,cid):
        self.name=name
        self.price=price
        self.cid=cid

# 购物车
class Cart:
    def __init__(self,cid=0,count=0):
        self.cid=cid
        self.count=count

#购物车逻辑控制器
#加载商品
#添加商品到订单
#生成订单
#根据订单计算总价格
class ShoppingManagerController:
    def __init__(self):
       self.__gwc_list=[]

    @property
    def gwc_list(self):
        return self.__gwc_list

    #加载商品
    def splb(self):
        for key, value in ShoppoingConsoleView.shang_pin_info.items():
            print('%d     %s     %d' % (key, value['name'], value['price']))

    #添加到购物车
    def tjsp(self,shangpin):
        self.__gwc_list.append(shangpin)


    # 生成订单
    def scdd(self):
        for i in self.gwc_list:
            for key, value in ShoppoingConsoleView.shang_pin_info.items():
                if i.cid==key:
                    sl_dj=i.count*value['price']
                    print(i.cid,i.count,sl_dj)

    def zongjia(self):
        zongjia=0
        for i in self.gwc_list:
            for key, value in ShoppoingConsoleView.shang_pin_info.items():
                if i.cid == key:
                    sl_dj = i.count * value['price']
                    zongjia+=sl_dj
        return zongjia

    #清空购物车
    def cart_clear(self):
        self.gwc_list.clear()



# f01=ShoppingManagerController
# s01=Cart(105,55)
# f01.tjsp(s01)

#购物车控制台界面视图
#入口 显示界面 1 2 q
#选择 1执行xx  2执行xx q退出
#1执行的函数
#2执行的函数
class ShoppoingConsoleView:
    shang_pin_info = {
         101: {'name': '倚天剑', 'price': 10000},
         102: {'name': '屠龙刀', 'price': 10000},
         103: {'name': '九阳神功', 'price': 10000},
         104: {'name': '九阴白骨爪', 'price': 9999},
         105: {'name': '乾坤大挪移', 'price': 8888},
         106: {'name': '七伤拳', 'price': 7777},
     }
    def __init__(self):
        self.__kzzx=ShoppingManagerController()

    #界面1
    def jiemian(self):
        print('''************
商店
************
按1购买
按2结算
按q退出
************
''')
    #选项
    def __xuanxiang(self):
        while True:
            item = input('请输入:')
            if item == 'q':
                break
            if item == '1':
                self.__goumaijm()
            elif item == '2':
                self.jiesuan()

    #入口
    def menu(self):
        while True:
            self.jiemian()
            self.__xuanxiang()

    #选项1
    def __goumaijm(self):
        print('*' * 50)
        self.__kzzx.splb()
        print('*' * 50)
        while True:
            cid = int(input('请输入商品编号：'))
            if cid in self.shang_pin_info:
                break
            else:
                print('商品不存在，请重新输入！')
        count = int(input('请输入商品数量：'))
        shangpin=Cart(cid,count)
        self.__kzzx.tjsp(shangpin)
        self.jiemian()



    #选项2
    def jiesuan(self):
        self.__kzzx.scdd()
        while True:
             zongjia=self.__kzzx.zongjia()
             shoukuan=int(input('总价为%s请付款:'%zongjia))
             if shoukuan >= zongjia:
                 print('购买成功，找零%.2f' % (shoukuan - zongjia))
                 self.__kzzx.cart_clear()
                 self.jiemian()
                 break
             else:
                 print('金额不足，请重新输入')


view = ShoppoingConsoleView()
view.menu()

#购物车控制台界面视图
#入口 显示界面 1 2 q

#选择 1购买  2结算 q退出

# 1执行的函数
#2执行的函数

#购物车逻辑控制器
#加载商品
#添加商品到订单
#生成订单
#根据订单计算总价格