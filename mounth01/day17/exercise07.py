list01=['孙悟空','白雪公主','贾宝玉']
list02=[101,102,103]

# for item in zip(list01,list02):
#     print(item)

def my_zip(l1,l2):
    for i in range(len(l1)):
        yield (l1[i],l2[i])

a=my_zip(list01,list02)
for item in a:
    print(type(item))


