#重复执行exercise01.py代码
# 直到按e退出
while True:
    jd = input('输入一个季度:')
    if jd == '春天':
        print('1月2月3月')
    elif jd == '夏天':
        print('4月5月6月')
    elif jd == '秋天':
        print('7月8月9月')
    elif jd == '冬天':
        print('10月11月12月')

    if input('输入e退出') == 'e':
      break
