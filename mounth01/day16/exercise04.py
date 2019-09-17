#使用for
tuple01=(5,3,4,18,13,51)
tp01=tuple01.__iter__()
for item in tp01:
    print(item)
# while True:
#     try:
#         item=tp01.__next__()
#         print(item)
#     except StopIteration:
#         break


dict01={'张翠山':101,'殷素素':102,'张无忌':103}
dt01=dict01.__iter__()
while True:
    try:
        item=dt01.__next__()
        print(item,dict01[item])

    except StopIteration:
        break