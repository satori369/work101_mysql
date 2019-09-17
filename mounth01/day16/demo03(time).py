import time

#获取当前时间戳 从1970年1月1日到现在的总秒数
# print(time.time())
#
# #获取当前的时间元组
# #(年,月,日,时,分,秒,一周的第几天(0 1 2),一年的第几天,夏令时)
print(time.localtime())
#
# #获取指定时间戳的时间元组
# print(time.localtime(12345678))

#时间元组变成时间戳
# time_tuple=time.localtime()
# print(time.mktime(time_tuple))

# #将时间元组转换成时间的字符串
# print(time.strftime('%y/%m/%d %H:%M:%S',time_tuple))
# print(time.strftime('%Y/%m/%d %H:%M:%S',time_tuple))
#
# #将日期字符串转换为时间元组
# print(time.strptime("19/08/21 11:31:30",'%y/%m/%d %H:%M:%S'))
