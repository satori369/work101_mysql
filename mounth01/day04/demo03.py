#累加1-100之间 能被5整除的数字
sum_number = 0
for i in range(1,101):
    if i % 5 != 0:
        #跳过本次循环 直接开始新的循环
        continue
    sum_number += 1

print(sum_number)

#打印1~20之间的数字 跳过所以偶数
# for i in range(1,21,2):
#     print(i)
for i in range(1,21):
    if i % 2 == 0:
        continue
    print(i)