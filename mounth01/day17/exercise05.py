list01=[45,34,56,48,3,18,1,8]
#传统方式
# def frlist():
#     # list02=[]
#     for item in list01:
#         if item%2==0:
#             # list02.append(item)
#             print(item)
#     # return list02
#
# re=frlist()
# for item in re:
#     print(item)


#生成器方式
# def my_range():
#     for item in list01:
#         if item %2==0:
#             yield item
#
# re=my_range()
# for item in re:
#     print(item)



# def get_even01():
#     list02 = []
#     for item in list01:
#         if item > 10:
#             list02.append(item)
#     return list02
#
# get_even01()
# for i in get_even01():
#     print(i)

def get_even02():
    for item in list01:
        if item > 10:
            yield item

re = get_even02()
for item in re:
    print(item)