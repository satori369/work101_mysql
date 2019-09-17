
list01=[6,5,13,2,4]
# for i in list01:
#     list01.sort()
#
# print(list01)
#
# for i in list01:
#     if i <= list01[i]:


num = list01[0]
for c in range(1,len(list01)):
    if num > list01[c]:
        num,list01[c]= list01[c],num
print(list01)
