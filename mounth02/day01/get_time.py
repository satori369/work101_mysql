import time

list=[i for i in range(1)]




sj1=time.time()
list.insert(2,20)
sj2=time.time()
print(sj1-sj2)
