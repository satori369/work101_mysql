def fun01():
    '''

    :return:
    '''
    a = 100
#开辟栈帧
fun01()
#栈帧销毁
#print(a)
# print()
#尝试画内存图
def fun02(p):
    '''

    :param p:
    :return:
    '''
    p = 100

a01=1
fun02(a01)
print(a01)

a02=['孙悟空']
a03=['猪八戒']

def fun03(p1,p2):
    #修改列表的元素
    p1[0] ='悟空'
    #将列表修改为字符串
    #修改栈帧中的变量
    p2 = '八戒'
fun03(a02,a03)

print(a02)
print(a03)

def fun04(p1,p2):
    # 切片赋值
    p1[:] = ['悟空']
    #浅拷贝
    temp = p2[:]
    #修改拷贝过的列表的值
    temp[:] = ['八戒']

fun04(a02,a03)
print(a02)
print(a03)

def fun01(p1,p2):
    p1='悟空'
    p2[0]='八戒'


a= 100
b=[200]
fun01(a,b)
print(a)#100
print(b)#['八戒']

#总结
#如果向函数传递一个可变的类型(列表)
#如果函数内部修改可变对象
#函数执行后,修改原列表的值
#可以不用返回值也能拿到结果