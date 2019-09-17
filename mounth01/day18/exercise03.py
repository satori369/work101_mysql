'''
    应用
    价值:逻辑连续
'''

def give_gife_money(money):
    def child_buy(target,price):
        nonlocal money
        if price < money:
            money -= price
            print('购买了%s,还剩下%d'%(target,money))
        else:
            print('钱不够')

    return child_buy

#得到10000压岁钱
action=give_gife_money(10000)
action('变形金刚',200)
action('电脑',8000)
action('手机',8848)