import turtle as t
t.color('blue')
for i in range(270):
    t.fd(i)
    t.left(70)
t.done()

#大多数用进程,线程会有gil问题,只有在有IO阻塞的情况下用线程