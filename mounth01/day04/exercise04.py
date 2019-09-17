number = int(input('输入一个整数'))
for i in range(2,number):
    if number % i == 0:
        print(str(number)+'不是素数')
        #如果发现满足条件的数字 就不用再判断后面的数字,结束循环
        break
else:
    print('是素数')