dj = float(input('商品单价:'))
sl = int(input('商品数量:'))
je = int(input('收款金额:'))
zl = je - dj * sl
if zl >= 0:
    print('找零:'+str(zl),'元')
else:
    print('金额不足')