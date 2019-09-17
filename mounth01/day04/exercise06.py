sum_number = 0
for i in range(10,51):
    unit = i % 10
    if unit == 3 or unit== 6 or unit== 9:
        continue
    sum_number += i
print(sum_number)

#次数未知          while循环
#次数已知/有确切数据   for循环
# break 语句
#     1. 跳出循环体，后面的代码不再执行。
#     2. 可以让while语句的else部分不执行。

# continue 语句
# 跳过本次，继续下次循环。
