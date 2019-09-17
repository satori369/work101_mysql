def myadd(num1, num2):
    result = num1 + num2
    return num1 + num2
    #要不要写return语句取决于用户是否需要再次处理函数的结果
    #如果需要再次处理就必须通过return返回结果
result = myadd(10,20)
print('结果是%d'%(result))