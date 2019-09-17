#获取用户输入的年份和月份 打印这个月份有多少天
#容器的思想去处理代码
year = int(input('输入年份:'))
month = int(input('输入月份:'))
# if month < 1 or month> 12 :
#     print('月份输入错误')
# elif month == 2:
#     if year % 4 == 0 and year%100 !=0 or year %400 ==0:
#         print('29天')
#     else:
#         print('28天')
# elif month in (4,6,9,11):
#     print('30天')
# else:
#     print('31天')

###############
if 0<month<13:
    month02 = 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
    days_month = [31,month02,31,30,31,30,31,31,30,31,30,31]
    print('这个月有%s天' % (days_month[month-1]))

else:
    print('月份错误')

