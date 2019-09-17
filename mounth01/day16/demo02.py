import  random,time
#生成随机整数
r01=random.randint(1,100)
print(r01)
#随机列表里面的值
r02= random.choice(['布','剪刀','石头'])
print(r02)
#随机列表里的顺序
r03=[1,2,3,4,5,6,7,8,9,10]
random.shuffle(r03)
print(r03[0],r03[1],r03[2])

#睡眠模式
time.sleep(5)

print(time.time())