# 4.定义一个购物功能
# shang_pin_info = {
# 101:{'name':'倚天剑','price':10000},
# 102:{'name':'屠龙刀','price':10000},
# 103:{'name':'九阳神功','price':10000},
# 104:{'name':'九阴白骨爪','price':9999},
# 105:{'name':'乾坤大挪移','price':8888},
# 106:{'name':'七伤拳','price':7777},
# }
# 要求 用户运行程序时显示菜单：
# ************
# 商店
# ************
# 按1购买
# 按2结算
# ************
#
# 如果用户按1显示：
# *************
# 101   倚天剑   10000
# 102   屠龙刀   10000
# 103   九阳神功   10000
# ....
# *************
# 请输入商品编号 (显示添加到购物车或商品不存在)
#
# 再次显示菜单：
# ************
# 商店
# ************
# 按1购买
# 按2结算
# ************
#
# 如果用户输入2：
# 显示
# ************
# 购物车
# ************
# 101 1 10000(编号  数量  价格)
# 102 3 30000
# ************
# 请输入金额：(如果金额大于总价格 找零 否则提示钱不够)
# shang_pin_info = {
# 101:{'name':'倚天剑','price':10000},
# 102:{'name':'屠龙刀','price':10000},
# 103:{'name':'九阳神功','price':10000},
# 104:{'name':'九阴白骨爪','price':9999},
# 105:{'name':'乾坤大挪移','price':8888},
# 106:{'name':'七伤拳','price':7777},
# }


# 要求 用户运行程序时显示菜单：
# ************
# 商店
# ************
# 按1购买
# 按2结算
# ************
while_1 = 0
while_2 = 0
while_3 = 0
while_4 = 0
while_5 = 0
while_6 = 0
dict_gwc = {101: while_1,
            102: while_2,
            103: while_3,
            104: while_4,
            105: while_5,
            106: while_6,
            }

while True:
    input01= int(input('***********'
                       '\n商店'
                       '\n***********'
                       '\n按1购买'
                       '\n按2结算'
                       '\n***********'))
    if input01==1 :
        input02= int(input('*************************'
                           '\n101  倚天剑       10000'
                           '\n102  屠龙刀       10000'
                           '\n103  九阳神功     10000'
                           '\n104  九阴白骨爪    9999'
                           '\n105  乾坤大挪移    8888'
                           '\n106  七伤拳        7777'
                           '\n请输入商品编号添加到购物车'
                           '\n*************************'))
        if input02 == 101:
            while_1 += 1
            dict_gwc[input02]= while_1
        elif input02 == 102:
            while_2 += 1
            dict_gwc[input02]= while_2
        elif input02 == 103:
            while_3 += 1
            dict_gwc[input02]= while_3
        elif input02 == 104:
            while_4 += 1
            dict_gwc[input02]= while_4
        elif input02 == 105:
            while_5 += 1
            dict_gwc[input02]= while_5
        elif input02 == 106:
            while_6 += 1
            dict_gwc[input02]= while_6
        else:
            print('商品不存在')
    elif input01 == 2:
        break
    else:
        print('请输入1或2')

dict_gwcje = {101: [while_1, while_1 * 10000],
            102: [while_2, while_2 * 10000],
            103: [while_3, while_3 * 10000],
            104: [while_4, while_4 * 9999],
            105: [while_5, while_5 * 8888],
            106: [while_6, while_6 * 7777],
            }

if (dict_gwcje.get(101))[0] == 0:
    del dict_gwcje[101]
if (dict_gwcje.get(102))[0] == 0:
    del dict_gwcje[102]
if (dict_gwcje.get(103))[0] == 0:
    del dict_gwcje[103]
if (dict_gwcje.get(104))[0] == 0:
    del dict_gwcje[104]
if (dict_gwcje.get(105))[0] == 0:
    del dict_gwcje[105]
if (dict_gwcje.get(106))[0] == 0:
    del dict_gwcje[106]

list=[]
hejije=0
for iii in dict_gwcje:
    list.append(iii)

for i,ii in dict_gwcje.items():
    print('编号%d有%d件,金额%d元'%(i,ii[0],ii[1]))
    hejije += ii[1]

input03 = int(input('合计金额是%d,请付款'%(hejije)))
if input03 >= hejije:
    zl = input03-hejije
    print('找零%d元'%(zl))
else:
    print('钱不够')
