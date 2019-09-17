# 6.打印出1000以内所有的"水仙花数"，
# 所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
# 例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
#方法1
# num = 100
# while num < 999:
#     num += 1
#     b = num // 100
#     s = num // 10 % 10
#     g = num % 10
#     if b**3 + s**3 + g**3 == b * 100 + s * 10 + g:
#       print(num)
# else:
#     print('以上是1000以内水仙花数')
#方法2
# for i in range(100,1000):
#     ge = i % 10
#     shi = i // 10 % 10
#     bai = i // 100
#     if ge**3+shi**3+bai**3 == i:
#         print(str(i)+'是水仙花数')
#方法3
for b in range(1,9):
  for s in range(0,9):
    for g in range(0,9):
        i = g + s*  10 + b * 100
        if b**3 + s**3 + g**3 == i:
            print(str(i)+'是水仙花数')
#方法4
#1     2     3
#百位  十位   个位
#123-->'123' '1' '2' '3'
for i in range(100,1000):
    #记录每一位数字的立方累加值 默认为0
    sum_number = 0
    #将数字转换为字符串 遍历获取每一个字符
    for ch in str(i):
        #讲每一位字符再转为数字 将立方值累加到sum_number
        sum_number += int(ch)**3
    #当循环结束后sum_number保存的就是各个位的累加和
    #panduan
    if sum_number == i:
        print(str(i)+'是水仙花数')

