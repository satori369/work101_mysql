m = int(input('输入分钟'))
h = int(input('输入小时'))
t = int(input('输入天'))

s = m * 60 + h * 3600 + t * 24 * 3600

print('总秒数:',s)
