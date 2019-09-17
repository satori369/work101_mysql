# 1.在控制台循环录入字符串 如果录入的是空字符串 退出循环
#  打印所有录入的内容
list1 = []
while True:
    str1= input('输入字符')
    if str1 == '' :
        break
    list1.append(str1)
str2 = '\n'.join(list1)
print(str2)

# 2.通过列表的方式模拟斐波那契数列
# 斐波那契数列特点 每一个值都是前两个数相加的结果
#  0 1 1 2 3 5 8 13 ...
fibs=[0,1]
for i in range(13):
    a = fibs[len(fibs)-2]+fibs[len(fibs)-1]
    fibs.append(a)
print(fibs)






