#3行5列的二维列表
list01 = [
    [0,1,2,3,4],
    [1,28,45,6,7],
    [20,7,3,65,2]
]
# for item in list01[1]:
#     print(item,end=' ')
# for iii in list01:
#     print(iii[0])

for i in list01:
    for ii in i:
        print(ii,end=' ')


# for i in range(len(list01)):
#     for ii in list01[i]:
#         print(ii,end=' ')