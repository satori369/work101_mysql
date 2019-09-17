import time

from mounth02.day01.linklist import Linklist

#6.67572021484375e-06


link=Linklist()
link.init_list(range(100))

st= time.time()
link.head_insert('007')
print(time.time()-st)