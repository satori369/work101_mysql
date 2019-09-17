list01 = [3,45,8,12,36,7,3]
result_list=[]
for i in list01:
  if i > 10 :
      result_list.append(i)
print(result_list)

#获取list01中最大的数 不使用max()
# max = list01[0]
# for i in list01[1:]:
#   if i > max:
#       max = i
# print(max)
#for i in range(1,len(list01)):

#
# for i in list01:#倒序删除
#     if i %2 :
#         list01.remove(i)
# print(list01)

for i in range(len(list01)-1,-1,-1):
    if list01[i] % 2:
        print(list01[i])
        del list01[i]
print(list01)





