# list01 = [
#     [0,1,2,3,4],
#     [1,28,45,6,7],
#     [20,7,3,65,2]
# ]
# 根据list01 生成list02
# 要求list02的每一行是list01的每一列
# list02 = [
#     [0,1,20],
#     [1,28,7],
#     ...
# ]
list01 = [
     [0,1,2,3,4],
     [1,28,45,6,7],
     [20,7,3,65,2]
]
# # #将第一列打印出来
# print(list01[0][0])
# print(list01[1][0])
# print(list01[2][0])
# list02=[]
# list03=[]
# list04=[]
# list05=[]
# list06=[]
# listx=[list02,list03,list04,list05,list06]
# for i in list01:
#     for ii in i[::]:
#         # list03 = (list01[i:0])
#         if ii in i[:1:]:
#             list02.append(ii)
#         if ii in i[1:2:]:
#             list03.append(ii)
#         if ii in i[2:3:]:
#             list04.append(ii)
#         if ii in i[3:4:]:
#             list05.append(ii)
#         if ii in i[4:5:]:
#             list06.append(ii)
#
# print(listx)

list02 = []
#获取list01中的第一列 形成列表放到list02中
# line = []
# for i in range(len(list01)):
#     line.append(list01[i][0])
# list02.append(line)
# line = []
# for i in range(len(list01)):
#     line.append(list01[i][1])
# list02.append(line)
# print(list02)

# for c in range(len(list01[0])):
#     line = []
#     for i in range(len(list01)):
#         line.append(list01[i][c])
#     list02.append(line)
#
# print(list02)



for c in range(len(list01[0])):
    list02.append([])
    for i in range(len(list01)):
        list02[c].append(list01[i][c])

print(list02)
#
# list01 = [
#      [0,1,2,3,4],
#      [1,28,45,6,7],
#      [20,7,3,65,2]
# ]