# 5.输入某年某月某日，判断这一天是这一年的第几天？
# year=int(input('输入年份'))
# if year > 0 :
#   month=int(input('输入月份'))
#   if 0 < month < 13:
#       day = int(input('输入日期'))
#       day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#       if 0 < day <= day_list[month-1]:
#           list = [0,31,59,90,120,151,181,212,243,273,304,334]
#           if (year % 4 == 0 and year % 100 !=0 or year % 400 == 0) and month > 2 :
#               days = day + list[month - 1]+1
#           else:
#               days = day + list[month - 1]
#           input('这是今年第'+str(days)+'天')
#       else:
#           input('请输入正确的日期')
#   else:
#       input('请输入正确的月份')
# else:
#     input('请输入正确的年份')
year = int(input('请输入年份：'))
month = int(input('请输入月份：'))
day = int(input('请输入日期：'))
if month<1 or month>12:
    print('月份输入错误')
else:
    month02=29 if year%4==0 and year%100 !=0 or year%400==0 else 28
    days_of_month = (0,31,month02,31,30,31,30,31,31,30,31,30,31)
    days = sum(days_of_month[:month-1])+day
    print(days)





