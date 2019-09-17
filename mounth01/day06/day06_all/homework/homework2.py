#斐波那契数列
fibs = [0,1]
#[0,1,1]
#[0,1,1,2]
# #[0,1,1,2,3,5,8,11...]
# first = fibs[0]
# second = fibs[1]
# for i in range(13):
#     result = first + second
#     fibs.append(result)
#     #当结果添加到列表后 将前两个数替换
#     first = second
#     second = result
# print(fibs)
for i in range(13):
    fibs.append(fibs[-1]+fibs[-2])
print(fibs)







