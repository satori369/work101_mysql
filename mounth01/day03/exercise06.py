# num = int(input('请输入一个整数'))
# if num%2==0:
#     state = '偶数'
# else:
#     state = '奇数'
# print(state)
#条件表达式
# state = '奇数' if int num % 2  else '偶数'
# print(state) ________________PEP8

nf = int(input('输入一个年份'))
day = 29 if nf % 4 == 0 and nf % 100 != 0 or nf % 400 == 0 else 28
print(day)

