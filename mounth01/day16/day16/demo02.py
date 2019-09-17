import random
#生成随机整数
r01 = random.randint(1, 100)
print(r01)
r02 = random.choice([1, 2, 3])
print(r02)

r03 = [1,2,3]
random.shuffle(r03)
print(r03)