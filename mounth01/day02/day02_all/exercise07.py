#输入年份
#判断是否为闰年
#闰年True  :年份能被4整除 同时不能被100整除
#        year % 4 == 0  and  year % 100 != 0
          # 或者 能被400整除也是闰年
          # year % 400 == 0
#输出结果

year = int(input('请输入年份：'))
result = year % 4 == 0  and  year % 100 != 0 or year % 400 == 0
print(result)