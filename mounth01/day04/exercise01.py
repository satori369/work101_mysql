#猜数字
#用户输入一个数字 电脑随机生成一个数字
#判断用户输入的数字和电脑随机生成的数字是否相同
#导入随机模块
#产生一个从1到100之间的随机数
import random
num2 = random.randint(1,5)
print(num2)
count = 0
while count<3:
  count += 1
  num = int(input('输入一个数字'))
  if num < num2:
      print('猜小了')
  elif num > num2:
      print('猜大了')
  elif num == num2:
      print('猜对了,总共猜了'+str(count)+'次')
      break
else:
    #循环条件不满足时执行的代码
    print('你输了,正确的数字是' + str(num2))



