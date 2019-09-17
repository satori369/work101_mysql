list=[]
while True:
    str_num = input('输入成绩')
    if str_num == '':
        break
    num= int(str_num)
    list.append(num)

print('最高分是'+str(max(list)))
print('最低分是'+str(min(list)))
print('平均分是'+str(sum(list)/len(list)))

