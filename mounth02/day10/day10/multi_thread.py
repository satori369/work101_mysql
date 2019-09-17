from thread_test import *
import threading
import time

jobs = []
tm = time.time()
for i in range(10):
    t = threading.Thread(target=io)
    jobs.append(t)
    t.start()

for i in jobs:
    i.join()

print("multi Thread CPU:",time.time() - tm)

