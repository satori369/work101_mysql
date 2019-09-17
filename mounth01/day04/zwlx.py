#珠穆朗玛峰 8848米 求一张纸对折多少次能达到8848米
# zhd = 0.0001
# cs = 0
# while zhd <=8848:
#     cs += 1
#     zhd *= 2
# print(cs)

#随机生成两个数字
#在控制台获取用户输入的两个数字相加的结果
   #3+2=？  5
   #8+5=？  3  x
#如果用户输入正确得20分
# 共5道题
# 保存分数
# #最后打印得分
import random
fs = 0
for i in range(5):
    num1 = random.randint(0,100)
    num2 = random.randint(0,100)
    num = int(input(str(num1)+'+'+str(num2)+'=?'))
    if num == num1+num2:
      fs += 20
input('得分'+str(fs))




