from thread_test import *
import time

tm = time.time()
for i in range(10):
    # count(1,1)
    io()
print("no thread IO:",time.time() - tm)
