a = input('结果1')
b = input('结果2')

# 所有语言通用思想
# temp = a
# a = b
# b = temp

a,b=b,a

print('第一个结果',a)
print('第二个结果',b)

del a, b