'''判断年份
年份是否为闰年
'''

year = int(input('请输入年份'))

rn = year % 4 == 0 and year % 100 != 0 or year % 400 == 0

print(rn)




