'''
循环嵌套
'''
#外层循环走一次 内层循环走一遍
#外层循环控制行
#内层循环控制列
for i in range(2):
    for c in range(3):
        #end=' ' 不换行 每次打印结束用空格分隔
        print('*',end=' ')
    print()#换行效果