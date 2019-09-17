# num = int(input('输入2个数字'))
# if (num%10 - num//10) > 0 :
#     print('最大的数字是:'+str(num%10))
# elif (num//10 - num%10) > 0 :
#     print('最大的数字是:' + str(num // 10))
# else :
#     print('最大的数字是:',num%10)

# num1 = int(input('输入第一个数字'))
# num2 = int(input('输入第二个数字'))
# num3 = int(input('输入第三个数字'))
# if num1>=num2 and num1>=num3:
#     print('最大的是'+str(num1))
# elif num2>=num1 and num2>=num3:
#     print('最大的是' + str(num2))
# elif num3>=num1 and num3>=num2:
#     print('最大的是' + str(num3))

num1 = int(input('输入第一个数字'))
num2 = int(input('输入第二个数字'))
num3 = int(input('输入第三个数字'))
num4 = int(input('输入第四个数字'))

max_value =num1
if max_value<num2:
    max_value = num2
if max_value<num3:
    max_value = num3
if max_value<num4:
    max_value = num4
print(max_value)