#随机加法开始
#随机生成2个数字
#在控制台获取用户输入的两个数字相加的结果
import random
score = 0
# cs = 0
# while cs<5:
#     cs += 1
for i in range(5):
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    num = int(input(str(num1)+'+'+str(num2)+'=?'))
    if num == num1+num2:
      score += 20
print('得分'+str(score))









