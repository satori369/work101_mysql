"""
gevent 协程模块示例
"""
import gevent
from gevent import monkey
monkey.patch_time()
from time import sleep

# 协程函数
def foo(a,b):
    print("Running foo ..",a,b)
    sleep(3)
    print("Foo again")

def bar(a,b):
    print("Running bar ..")
    sleep(2)
    print("Bar again")
# 生成协程对象
f = gevent.spawn(foo,1,2)
g = gevent.spawn(bar,1,2)
gevent.joinall([f,g]) # 阻塞等待f执行完
