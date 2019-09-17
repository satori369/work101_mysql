# 1.在控制台获取输入的月份 显示对应的季度
# 或提示月份错误
# while True:
#     yf = int(input('输入月份'))
#     if   yf == 1 or yf == 2 or yf == 3:
#         print('春季')
#     elif yf == 4 or yf == 5 or yf == 6:
#         print('夏季')
#     elif yf == 7 or yf == 8 or yf == 9:
#         print('秋季')
#     elif yf == 10 or yf == 11 or yf == 12:
#         print('冬季')
#     else:
#         print('月份错误')
#     if input('输入e退出') == 'e':
#         break



# 2.在控制台获取年龄
# 如果小于0 打印输入错误
# 如果小于2 打印是婴儿
# 如果小于2~13  儿童
#       13~20  青年
#       20-65  成年
#       65~130 老年人
#       超过130 不可能
# while True:
#     age = int(input('输入年龄:'))
#     if age<0:
#        print('还没出生哈?')
#     elif 0<=age<2:
#         print('婴儿')
#     elif 2<=age<13:
#         print('儿童')
#     elif 13<=age<20:
#         print('青年')
#     elif 20<=age<65:
#         print('成年')
#     elif 65<=age<130:
#         print('老年人')
#     else:
#         print('长生不老药哪买的')



# 3.根据身高和体重 参照BMI 返回身体状况
# BMI 体重(kg)/身高(m)**2
# 中国参考标准
# BMI<18.5   体重过低
# 18.5<=BMI<24   正常
# 24<=BMI<28     超重
# 28<=BMI<30     I度肥胖

# m = float(input('请输入身高'))
# kg = float(input('输入体重'))
# BMI = kg/m**2
# if BMI <18.5:
#     print('体重过低')
# elif 18.5<=BMI<24:
#     print('体重正常')
# elif 24<=BMI<28:
#     print('超重')
# elif 28<=BMI<30:
#     print('I度肥胖')


# 4.题目：企业发放的奖金根据利润提成。
# 利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，
# 高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
# while True:
#   ll = float(input('输入当月利润多少万:'))
#   if ll<=10:
#       print(ll*0.1)
#   elif 10<ll<20:
#       print(1 + (ll-10)*0.075)
#   elif 20<=ll<40:
#       print(1 + 0.75 + (ll-20)*0.05)
#   elif 40<=ll<60:
#       print(1 + 0.75 + 1 + (ll-40)*0.03)
#   elif 60<=ll<=100:
#       print(1 + 0.75 + 1 + 0.6 + (ll-60)*0.015)
#   elif ll>100:
#       print(1 + 0.75 + 1 + 0.6 + 0.6 + (ll-100)*0.01)

# 5.输入某年某月某日，判断这一天是这一年的第几天？

year=int(input('输入年份'))
if year > 0 :
  month=int(input('输入月份'))
  if 0 < month < 13:
      day = int(input('输入日期'))
      day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
      if 0 < day <= day_list[month-1]:
          list = [0,31,59,90,120,151,181,212,243,273,304,334]
          if (year % 4 == 0 and year % 100 !=0 or year % 400 == 0) and month > 2 :
              days = day + list[month - 1]+1
          else:
              days = day + list[month - 1]
          input('这是今年第'+str(days)+'天')
      else:
          input('请输入正确的日期')
  else:
      input('请输入正确的月份')
else:
    input('请输入正确的年份')

# 6.打印出1000以内所有的"水仙花数"，
# 所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
# 例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
num = 100
while num < 999:
    num += 1
    b = num // 100
    s = num // 10 % 10
    g = num % 10
    if b**3 + s**3 + g**3 == b * 100 + s * 10 + g:
      print(num)
else:
    print('以上是1000以内水仙花数')