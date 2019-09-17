'''
  练习3:
'''

list01=['无忌','翠山','翠翠']
# for item in enumerate(list01):
#     print(item)

def my_enumerate(iterable):
    index=0
    for item in iterable:
         yield (index,item)
         index+=1

e = my_enumerate(list01)
for item in e:
    print(item)

