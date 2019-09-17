#再控制台分别输入4个数字
#打印最大的数字

#1.在控制台输入两个数字 打印最大的数字
# num1 = float(input('请输入第一个数字：'))
# num2 = float(input('请输入第二个数字：'))
# #如果第一个数比第二个数大 输入第一个数
# if num1 > num2:
#     print(num1)
# #如果相等 输出第一个数等于第二个数
# elif num1 == num2:
#     print(num1)
# #否则输出第二个数
# else:
#     print(num2)

#2.在控制台输入三个数  打印其中最大的
#先比前两个
#用较大的去和第三个比
#得到结果
# num1 = float(input('请输入第一个数字：'))
# num2 = float(input('请输入第二个数字：'))
# num3 = float(input('请输入第三个数字：'))
# if num1 > num2:
#     #num1比较大
#     #判断num1和num3的大小 输出较大的
#     if num1>num3:
#         print(num1)
#     else:
#         print(num3)
# else:
#     #num2比较大
#     #判断num2和num3的大小 输出较大的
#     if num2>num3:
#         print(num2)
#     else:
#         print(num3)

#14:50~15:05

num1 = float(input('请输入第一个数字：'))
num2 = float(input('请输入第二个数字：'))
num3 = float(input('请输入第三个数字：'))
num4 = float(input('请输入第四个数字：'))

#假设第一个数是最大值
max_value = num1
#将最大值与第二个数比较 如果第二个数比最大值大
if max_value<num2:
    #最大值等于第二个数
    max_value = num2
#依次与第三第四个数比较
if max_value<num3:
    max_value = num3
if max_value<num4:
    max_value = num4
#输出最大值
print(max_value)













