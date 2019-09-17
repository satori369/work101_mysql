"""
event 线程互斥方法演示
"""

from threading import Thread,Event

s = None
e = Event()

def 杨子荣():
    print("杨子荣前来拜山头")
    global s
    s = "天王盖地虎"
    e.set()

t = Thread(target = 杨子荣)
t.start()

print("说对口令就是自己人")
e.wait() # 等待e被set
if s == '天王盖地虎':
    print("宝塔镇河妖")
    print("确认过眼神，你是对的人")
else:
    print("打死他！")

t.join()







