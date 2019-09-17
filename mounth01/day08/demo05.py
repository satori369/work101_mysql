# g01='悟空'
# g02='八戒'
# def fun01():
#     num1 =100
#     print(num1)
#
#     g02='老朱'
#     print(g02)
#
#     global g03
#     g03 ='老沙'

    #先定义了局部变量
    #再声明全局变量 有歧义
    #3.6版本后报错
    # global g02
    # g02 = '猪八戒'
    # print(g02)

# fun01()
# print(g03)
# print(g02)

# a=1
# def fun01():
#     a= 10
#     def inner_fun():
#         nonlocal a
#         a+=1#a = a + 1
#         print(a)
#     inner_fun()
#     print(a)
#
# fun01()


def user_info():
    user_name='lw'
    user_age=20
    gender ='男'
    # return user_name,user_age,gender
    return {'username':user_name,'userage':user_age,'gender':gender}

#获取到返回的元组
# print(user_info())
#输出详细信息
print('姓名:%s,年龄是%s,性别是%s'%(user_info()['username'],user_info()['userage'],user_info()['gender']))