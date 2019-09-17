import time
from linklist import *

# 100  time: 5.4836273193359375e-06
# 1000 time: 5.7220458984375e-06
from mounth02.day01.linklist import insert

link = LinkList()
link.init_list(range(1000000))

st = time.time()
insert(link.head, 99999, '007')
print("time:",time.time() - st)
