# 定义一个函数 myprint  统计该函数调用的次数

count = 0

def myprint():
    #如果在函数内部直接修改全局变量 程序会认为是创建新的局部变量
    #需要先声明再赋值
    global count#将count声明为全局变量
    nonlocal count #修改外层嵌套函数内的变量
    count += 1
    print(count)




myprint()
myprint()
myprint()
myprint()
