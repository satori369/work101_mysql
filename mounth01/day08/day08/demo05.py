# g01 = "悟空"
# g02 = "八戒"
# def fun01():
#     num1 = 100
#     print(num1)
#
#     g02 = "老朱"
#     print(g02)
#
#     global g03
#     g03 = '老沙'
#
#     #先定义了局部变量
#     #再声明全局变量 有歧义
#     #3.6版本后报错
#     # global g02
#     # g02 = '猪八戒'
#     # print(g02)
#
# fun01()
# print(g03)
# print(g02)

# def fun01():
#     a = 10
#     def inner_fun():
#         # a = 2
#         nonlocal a
#         a+=1#a = a + 1
#         print(a)
#     inner_fun()
#     print(a)
#
# fun01()
def user_info():
    uesr_name = 'shibw'
    user_age = 20
    user_email = 'shibw@tedu.cn'
    gender = '男'
    address = '北京市东城区'
    # return (uesr_name,user_age,uest_email,gender,address)
    # return user_age
    # return {'uesr_name':uesr_name,'user_age':user_age,'user_email':uesr_email,'gender':gender,'address':address}
    #locals() 收集当前的局部变量 保存到字典
    return locals()

#获取到返回的元组
print(user_info())
inofs = user_info()
#输出详细信息
print('姓名：%s,年龄：%s,邮箱：%s,性别：%s,地址：%s' % (inofs['uesr_name'],inofs['user_age'],inofs['user_email'],inofs['gender'],inofs['address']) )





