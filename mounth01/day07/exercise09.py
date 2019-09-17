#定义计算4

def sum0(num):
    '''
    这是计算整数每位相加的结果
    :param num: 4位整数
    :return: 每位相加的和
    '''
    result = num %10
    result += num //  10 %10
    result += num//100 %10
    result += num//1000
    return result
print(sum0(7301))
