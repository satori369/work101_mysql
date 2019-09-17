"""
    外部嵌套作用域
"""
def fun01():
    a = 10# fun02的外部嵌套变量
    def fun02():
        # print(a)  # 可以读取
        nonlocal a # 声明外部嵌套变量
        a = 200

    fun02()
    print(a)

fun01()
