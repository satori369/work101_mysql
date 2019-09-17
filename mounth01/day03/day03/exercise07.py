#重复执行exerciese01.py代码 直到按e键退出
#休息+练习 17:00～17:15
#死循环  循环条件永远满足
while True:
    season = input('请输入季度：')
    if season == '春':
        print('1月2月3月')
    elif season == '夏':
        print('4月5月6月')
    elif season == '秋':
        print('7月8月9月')
    elif season == '冬':
        print('10月11月12月')

    if input('输入e退出') == 'e':
        break
