#在控制台输入一个月份 打印对应的天数
#1 3 5 7 8 10 12  --->31天
#

yf = input('输入一个月份')
if yf == '1' or yf == '3' or yf == '5' or yf == '7' or yf == '8' or yf =='10' or yf == '12':
    print('31天')
elif yf == '4' or yf == '6' or yf == '9' or yf == '11':
    print('30天')
elif yf == '2':
    print('28天')
else:
    print('输入错误')